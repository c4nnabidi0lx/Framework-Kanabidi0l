## kanabidi0l mad3d (v1.0.0)
an advanced, lightweight offensive recon framework engineered for mobile environments like kali nethunter and termux. built entirely in pure python 3 without heavy external dependencies, utilizing a professional ansi color scheme and strict vertical spacing optimization for low-resolution mobile screens. mad3d by cannabidi0lx. [1] 
------------------------------
## features

* web fuzzer with bruteforce: directory and hidden path scanner powered by native http structures. handles success and restriction flags directly.
* portscanner advanced: raw tcp port scanner using low-level socket engines. equipped with aggressive timeouts to skip filtered gates and automatically grab active service banners.
* capture headers for host: deep passive server fingerprinting. extracts backend web server names, core technologies in use, and tests compliance against clickjacking flaws.

------------------------------
## installation and setup

apt update && apt upgrade -y
apt install python3 python3-pip -y
git clone https://github.com
cd kanabidiol
pip3 install requests

------------------------------
## usage

python3 kanabidiol.py

## controls

* ctrl + c: terminates running mass port scans or brute-force processes without breaking the terminal shell.
* option 4: closes all active system threads and performs a clean garbage memory flush before exiting the execution loop.

------------------------------
## screenshots## main interactive menu## passive fingerprinting analysis
------------------------------
## legal disclaimer
this tool is strictly developed for educational purposes, authorized security auditing, and local penetration testing. the author holds zero liability for infrastructure damage, malicious usage, or unauthorized target scanning. always secure written permission prior to conducting digital exploitation.
------------------------------
