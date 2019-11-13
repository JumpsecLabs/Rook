variable "snapid" {
  default	= "snap-"
}

variable "nvidia" {
  default	= "http://us.download.nvidia.com/tesla/410.104/NVIDIA-Linux-x86_64-410.104.run"
}

variable "hashcat" {
  default	= "https://hashcat.net/files/hashcat-5.1.0.tar.gz"
}

variable "ami" {
  default	= "ami-0ee246e709782b1be"
}

variable "itype" {
  default	= "p3.2xlarge"
}

variable "identity" {
  default	= "user"
}

variable "whitelistip" {
  default	= "0.0.0.0/32"
}

variable "sshkeyfile" {
  default	= "/home/user/.ssh/user"
}

variable "spotprice" {
  default	= null
}

variable "cmdp1" {
  default 	= "nohup sudo screen -dmS hashcat bash  -c 'sudo /opt/hashcat-5.1.0/hashcat -a 0 -m"
}

variable "cmdp2" {
  default = "/opt/hashes.txt /words/rockyou.txt /words/fav_wordlist.lst /words/crackstation.txt -r /words/OneRuleToRuleThemAll.rule -o 00cracked.txt; exec bash' &"
}

variable "hashmode" {
  type		= number
  default	= "1000"
}

