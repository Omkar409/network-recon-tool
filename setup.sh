#!/bin/bash
# Setup script for Network Reconnaissance Tool
# Run this in Kali Linux

echo "=========================================="
echo "  Network Recon Tool - Setup"
echo "=========================================="

# Check if running as root (optional but recommended for some features)
if [ "$EUID" -ne 0 ]; then 
    echo "[!] Note: Some features work better with sudo"
fi

# Create project directory
PROJECT_DIR="$HOME/network-recon-tool"
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

echo "[+] Installing dependencies..."
sudo apt update -qq
sudo apt install -y python3 python3-pip nmap -qq 2>/dev/null

# Create virtual environment
echo "[+] Setting up Python environment..."
python3 -m venv venv 2>/dev/null || echo "venv already exists"
source venv/bin/activate

# Install Python packages
echo "[+] Installing Python packages..."
pip install -q colorama argparse 2>/dev/null

echo ""
echo "=========================================="
echo "  Setup Complete!"
echo "=========================================="
echo ""
echo "Usage:"
echo "  source venv/bin/activate"
echo "  python3 network_recon.py -t <target>"
echo ""
echo "Examples:"
echo "  python3 network_recon.py -t 192.168.1.1"
echo "  python3 network_recon.py -t scanme.nmap.org -p 1-1000"
echo "  python3 network_recon.py -t 192.168.1.1 -p 22,80,443 -T 50"
echo ""
