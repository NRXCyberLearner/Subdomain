# 🔥 NRX Subdomain Scanner v2.0

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0-brightgreen">
  <img src="https://img.shields.io/badge/Python-3.x-blue">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Kali%20Linux-red">
</p>

<p align="center">
  <b>Created with ❤️ by 👑 NRX Cyber Learner 👑</b>
</p>

## 📋 Description
A powerful subdomain scanner that works on both Termux and Kali Linux. Find subdomains of any website using multiple techniques.

## ✨ Features
- 🚀 Multi-threaded scanning
- 🔍 Certificate Transparency (crt.sh) integration
- 📊 Multiple output formats (TXT, JSON, CSV)
- 🎨 Colorful output with status codes
- 💾 Save results automatically
- 📱 Works on Termux & Kali Linux

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
apt install python git -y
```
```bash 
python nrx_scanner.py -d example. com
```
### kali installation:
```bash 
sudo apt update
```
```bash 
sudo apt install python3 python3-pip git
```
```bash 
git clone https://github.com/NRXCyberLearner/Subdomain.git
```
```bash 
cd Subdomain
```
```bash 
python3 nrx_scanner.py -d example. com
``` 




## 🎯 **Usage Commands**

```bash
# Basic scan
python3 nrx_scanner.py -d google.com

# With wordlist
python3 nrx_scanner.py -d google.com -w wordlists/subdomains.txt

# With 100 threads and JSON output
python3 nrx_scanner.py -d google.com -t 100 -o json

# Save to CSV
python3 nrx_scanner.py -d google.com -o csv

# Help
python3 nrx_scanner.py -h
