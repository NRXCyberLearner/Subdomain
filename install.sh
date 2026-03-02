#!/bin/bash
# NRX Subdomain Scanner - Installation Script
# Created by NRX Cyber Learner

clear
echo "╔════════════════════════════════════════════════════════╗"
echo "║     🔧 NRX Subdomain Scanner - Installation Script    ║"
echo "║           Created by: NRX Cyber Learner               ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Check if running on Termux or Linux
if [ -d "/data/data/com.termux" ]; then
    echo "📱 Termux detected!"
    pkg update -y
    pkg upgrade -y
    pkg install python -y
    pkg install git -y
else
    echo "💻 Linux system detected!"
    sudo apt update
    sudo apt install python3 python3-pip git -y
fi

# Install Python packages
echo ""
echo "📦 Installing Python packages..."
pip3 install requests colorama

# Download wordlist
echo ""
echo "📁 Downloading wordlist..."
mkdir -p wordlists
wget -q https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-5000.txt -O wordlists/subdomains.txt


echo ""
echo "✅ Installation complete!"
echo ""
echo "📌 Usage:"
echo "   python nrx_scanner.py -d example.com"
echo ""
echo "👑 Happy Hacking from NRX Cyber Learner!"
