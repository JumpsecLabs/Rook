# Rook
Rook automates the creation of AWS p3 instances for use in GPU-based password cracking. AWS p3 instances use the NVIDIA V100 GPUs, which provide the best password cracking H/s per GPU we've found. Rook is a Python wrapper around a Terraform base, automating the creation, mounting of wordlists and Hashcat installation, and will start the cracking for you.

Start to finish, execution of Rook takes between 3m50 seconds and 4m15 seconds (not including cracking time).

None of this would be possible to the great work done by the [Hashcat team](https://github.com/hashcat/hashcat).
Ideas for the automation and usage of AWS for password cracking came from: [1](https://hackernoon.com/20-hours-18-and-11-million-passwords-cracked-c4513f61fdb1),[2](https://medium.com/@lordsaibat/cracking-passwords-with-terraform-and-aws-3685cc918721),[3](https://medium.com/@iraklis/running-hashcat-v4-0-0-in-amazons-aws-new-p3-16xlarge-instance-e8fab4541e9b).


## Index
- [Statistics](#statistics)
- [Usage](#usage)
- [Future](#future)

## Statistics
Rook can create AWS instances and have Hashcat running against your hashes in 3 minutes 50 seconds.
MegaHash/Second statistics for hashtypes we encounter on internal tests - for a single NVIDIA V100 GPU. p3.8xlarge and p3.16xlarge have 4 and 8 of these GPUs respectively:

| Hash Type  | NVIDIA V100 Megahashes per Second  |
| ------------- | ------------- |
| NTLM  | 77639.0 MH/s  |
| NetNTLMv1  | 44135.5 MH/s  |
| NetNTLMv2  | 3805.4 MH/s  |
| Kerberos Type 5 (krbtgt)  | 999.4 MH/s  |

A full benchmark on the p3.2xlarge instance is available [here](stats.md). Stats more or less scale linearly on the p3.8xlarge and p3.16xlarge - working on getting stats for these.

The stats for megahashes per second are based off of pure-brute force rather than dictionaries - in reality, the stats for dictionary smart brute forcing are significantly lower due to I/O bottlenecks reading from disk into the GPU's memory.

All types of cracking take significantly longer when rules are used, as it dramatically increases the number of passwords in the dictionary. As an example, Kerberos cracking without any rules applied takes roughly 20 minutes. With rules enabled, it takes around 3 days. 

## Usage

```
Terraform AWS instances for cracking hashes

usage: rook.py [-h] [-i IDENTITY] [-t {p3.2xlarge,p3.8xlarge,p3.16xlarge}]
                [-f HASHFILE] [-m MODE] [-s SSHKEY] [--spot SPOT] [--info]
                [--destroy] [--silent] [--check-id]
                [--check-spot {p3.2xlarge,p3.8xlarge,p3.16xlarge}] [--debug]

Automates creation of AWS P3 GPU instances to crack password hashes. Example command usage:
./rook.py -t p3.2xlarge -f /tmp/krbtgt.txt -i pentest-user -s /path/to/ssh/key

optional arguments:
  -h, --help            show this help message and exit
  -i IDENTITY, --identity IDENTITY
                        AWS Identity to use. Make sure SSH key on local machine is the same name.
  -t {p3.2xlarge,p3.8xlarge,p3.16xlarge}, --type {p3.2xlarge,p3.8xlarge,p3.16xlarge}
                        Type of instance to use. Choices are small ($3.589/h), medium ($14.356/h), and large ($28.712/h).
  -f HASHFILE, --hashfile HASHFILE
                        Location of hashes to crack.
  -m MODE, --mode MODE  The Hashcat hashmode to crack the type of hashes.
  -s SSHKEY, --ssh SSHKEY
                        Path to SSH private key file used to connect to the instance.
  --spot SPOT           Spot price to bid at for AWS P3 instances.
  --info                Print Hashcat hashtypes and AWS instance costs and exit.
  --destroy             Destroy instances that you have created. NOTE: This does not destroy instances that others in the company have created.
  --silent              Don't prompt for user input when running Rook. Make sure you've got everything right!
  --check-id            Check what the AWS Keypair name is for your account (--identity).
  --check-spot {p3.2xlarge,p3.8xlarge,p3.16xlarge}
                        Check the current spot price for the requested instance type.
```

Example usage:

`./rook.py -t p3.2xlarge -f /home/user/docs/krbtgt.txt -m 13100 -i user -s /home/user/.ssh/pentest-user`

This will create an AWS P3 instance, provision it to run Hashcat. It will then copy the krbtgt.txt file over SSH to the remote server, and run Hashcat in a screen against this krbtgt.txt file with mode 13100. Cracking takes too long to run as an syncronous process, so the screen is necessary. To check for status of hashes, SSH into the instance. Rook will just spit out the command for you to run so you can copy paste to SSH.
To destroy instances, it's much simpler, just do:

`./rook.py --destroy`

You can also check your AWS keypair name in case you forget with the --check-id option. Checking AWS spot instance prices can be done with the --check-spot flag and the instance you want to check.

For spot instances, if you run Rook without the --spot instance flag, it will automatically bid for the lowest price with the NORMAL instance price as the price max. This means you'll get the cheapest usage possible all the way until it costs the normal usage amount. If Rook is run with the --spot flag, it will go up to the amount you specify, and terminate if no spot instances are available at that price.

While spot instances sound fantastic, in reality there is reasonable competition for AWS p3 instances, and they're listed as 20% vulnerable to service disruption due to high demand. As such, running it with spot-requests may mean that you end up with an unfulfilled spot request due to lack of service availability in the pool.

## Future
Looking forward, what we want to implement in releases after 1.0.
- Dockerfile support
- More robust pre-execution setup and automation of local configuration
- Streamlined security group creation depending on location of the user running the script
- Tidy up the code
- Better conditional execution
- Sub-modules for creating wordlist volumes
