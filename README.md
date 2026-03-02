# 🔥 NRX Subdomain Scanner v2.0

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0-brightgreen">
  <img src="https://img.shields.io/badge/Python-3.x-blue">
  
</p>

<p align="center">
  <b>Created with ❤️ by 👑 NRX Cyber Learner 👑</b>
</p>

## 📋 Description
A powerful subdomain scanner that works on both Termux and . Find subdomains of any website using multiple techniques.

## ✨ Features
- 🚀 Multi-threaded scanning
- 🔍 Certificate Transparency (crt.sh) integration
- 📊 Multiple output formats (TXT, JSON, CSV)
- 🎨 Colorful output with status codes
- 💾 Save results automatically
- 📱 Works on Termux 

## 🔧 Installation

### On Termux:
```bash
pkg update && pkg upgrade
```
```bash 
pkg install python git
```
```bash
git clone https://github.com/NRXCyberLearner/Subdomain.git
```
```bash 
cd Subdomain
```
```bash
chmod +x install.sh
```
``` bash
./install.sh
```


## 🎯 **Usage Commands**

```bash
# Basic scan
python nrx_scanner.py -d google.com

# With wordlist
python nrx_scanner.py -d google.com -w wordlists/subdomains.txt

# With 100 threads and JSON output
python nrx_scanner.py -d google.com -t 100 -o json

# Save to CSV
python nrx_scanner.py -d google.com -o csv

# Help
python nrx_scanner.py -h
