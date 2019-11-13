#!/usr/bin/python3

import sys
import argparse
import os
import boto3
import json
import datetime
import shutil
import subprocess
from pathlib import Path
from bson import json_util

def banner():
    print("""

     ██████╗  ██████╗  ██████╗ ██╗  ██╗
     ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
     ██████╔╝██║   ██║██║   ██║█████╔╝ 
     ██╔══██╗██║   ██║██║   ██║██╔═██╗ 
     ██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
Terraform AWS instances for cracking hashes
    """)

def parse_args():
    parser = argparse.ArgumentParser(description="Automates creation of AWS P3 GPU instances to crack password hashes. Example command usage:\n./Rook.py -t p3.2xlarge -f /tmp/krbtgt.txt -i pentest-user -s /path/to/ssh/key", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-i","--identity",help="AWS Identity to use. Make sure SSH key on local machine is the same name.",action='store')
    parser.add_argument("-t","--type",help="Type of instance to use. Choices are small ($3.589/h), medium ($14.356/h), and large ($28.712/h).", choices=['p3.2xlarge','p3.8xlarge','p3.16xlarge'], action='store')
    parser.add_argument("-f","--hashfile",help="Location of hashes to crack.", action='store')
    parser.add_argument("-m","--mode",help="The Hashcat hashmode to crack the type of hashes.",type=int, action='store')
    parser.add_argument("-s","--ssh",dest="sshkey",help="Path to SSH private key file used to connect to the instance.", action='store')
    parser.add_argument("--spot",dest="spot",help="Spot price to bid at for AWS P3 instances.",type=float, action='store')
    parser.add_argument("--info",help="Print Hashcat hashtypes and AWS instance costs and exit.", action='store_true')
    parser.add_argument("--destroy",dest="destroy",help="Destroy instances that you have created. NOTE: This does not destroy instances that others in the company have created.", action='store_true')
    parser.add_argument("--silent",help="Don't prompt for user input when running Rook. Make sure you've got everything right!", action="store_true")
    parser.add_argument("--check-id",dest="idcheck",help="Check what the AWS Keypair name is for your account (--identity).", action="store_true")
    parser.add_argument("--check-spot",dest="spotcheck",help="Check the current spot price for the requested instance type.",choices=['p3.2xlarge','p3.8xlarge','p3.16xlarge'], action="store")
    parser.add_argument("--debug",dest="debug", action="store_true")
    return parser.parse_args()

def presetup():
    home = str(Path.home())
    if os.path.exists('terraform') is False:
        print("[!] Terraform executable is not present. The file can be downloaded from here https://releases.hashicorp.com/terraform/0.12.10/terraform_0.12.10_linux_amd64.zip")
        print("[!] Exiting...")
        sys.exit(1)
    if os.path.exists(home + '/.aws/credentials') is False:
        print("[!] No AWS credentials present. Running aws configure now. Region should be eu-west-2")
        subprocess.call("aws", "configure")
        print("[!] You can now run Rook!")
        sys.exit(0)
    if os.path.exists('./.terraform/') is False:
        print("[+] Performing first time Terraform setup. Please wait while correct packages are built.")
        subprocess.call(['./terraform', 'init'])
        print("[+] Terraform initialisation complete, please re-run to create your instance.")
        sys.exit(0)

"""
Codeblock should go here for a checking module of Rook. This checking module should run all queries to AWS that require  AWS credentials to be configured, or fetch the latest spot price history.
- AWS describe key pairs
- Check keypair fingerprints against one another
- Check spot price history
- Check if any instances are currently running for the user
- 

ec2 = boto3.client('ec2')
response = ec2.describe_key_pairs()
parsing = json.dumps(response['KeyPairs'][0]['KeyName'], sort_keys=True, indent=4)
print(parsing)

Stuff like that
"""
def check():
    args = parse_args()
    now = datetime.datetime.now()
    ec2 = boto3.client('ec2')
    if args.idcheck:
        awsid = ec2.describe_key_pairs()
        print("[+] AWS Identity keypair name is: " + awsid['KeyPairs'][0]['KeyName'])
        sys.exit(0)
    if args.spotcheck:
        spothist = ec2.describe_spot_price_history(
                Filters=[
                    {
                        'Name': 'product-description',
                        'Values': [
                            'Linux/UNIX',
                        ]
                    },
                ],
                InstanceTypes=[args.spotcheck],
                StartTime=(now.strftime("%Y-%m-%d")),
        )
        
        def convert_timestamp(item_date_object):
                if isinstance(item_date_object, (datetime.date, datetime.datetime)):
                            return item_date_object.timestamp()
        spotparse = json.dumps(spothist['SpotPriceHistory'], default=convert_timestamp, indent=4)
        print("[+] Getting spot prices for " + args.spotcheck + " instances in eu-west-2b.\n")
        print(spotparse)
        sys.exit(0)

def main():
    args = parse_args()
    tf = ['./terraform']
    parser = argparse.ArgumentParser()
    if args.spotcheck or args.idcheck:
        check()
    if args.destroy:
        tf.extend(['destroy'])
        print("[-] Rook is going to destroy your p3 instances.")
        subprocess.call(tf)
        sys.exit(0)
    if (args.type is None) or args.type and (args.hashfile is None or args.mode is None or args.identity is None or args.sshkey is None):
        print("[!] Missing arguments: Hashfile path, hash mode, AWS identity and SSH key path all required.")
        sys.exit(1)
    else:
        try:
            shutil.copyfile(args.hashfile,'files/hashes.txt')
        except:
            print("[!] Unable to locate hashfile at specified path.")
            sys.exit(1)
        if os.path.exists(args.sshkey) is False:
            print("[!] Unable to locate SSH key file at specified path.")
            sys.exit(1)
        b = ["apply", "-var=identity={}".format(args.identity), "-var=hashmode={}".format(args.mode), "-var=itype={}".format(args.type), "-var=sshkeyfile={}".format(args.sshkey)]
        if args.spot:
            b.append("-var=spotprice={}".format(args.spot))
            print("[+] Bidding for spot instance at max price of " + str(args.spot) + ".")
        if args.silent:
            b.append("--auto-approve")
        tf.extend(b)
        print("[+] Creating Rook instance to crack passwords with an AWS " + args.type + " instance. Please wait...")
        # Enable debugging
        if args.debug:
            list1 = ' '.join(tf)
            print(list1)
        # Execution
        subprocess.call(tf)
        return

if __name__ == "__main__":
    banner()
    presetup()
    main()
