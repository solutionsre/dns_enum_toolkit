#!/bin/bash

echo "[+] Checking and installing required tools..."

# Function to check and install APT tools
install_apt_tool() {
  TOOL=$1
  if ! command -v "$TOOL" &>/dev/null; then
    echo "[*] Installing $TOOL..."
    sudo apt install -y "$TOOL"
  else
    echo "[✓] $TOOL is already installed."
  fi
}

# Function to check and install Go-based tools
install_go_tool() {
  TOOL=$1
  PACKAGE=$2
  if ! command -v "$TOOL" &>/dev/null; then
    echo "[*] Installing $TOOL..."
    go install -v "$PACKAGE"
  else
    echo "[✓] $TOOL is already installed."
  fi
}

# Update package list
sudo apt update

# Install APT tools
install_apt_tool amass
install_apt_tool dnsrecon
install_apt_tool dnsenum
install_apt_tool nmap
install_apt_tool theharvester
install_apt_tool golang-go
install_apt_tool dnx
install_apt_tool nuclei

# Ensure Go binaries are in PATH
export PATH=$PATH:$(go env GOPATH)/bin

# Install Go-based tools
install_go_tool httpx github.com/projectdiscovery/httpx/cmd/httpx@latest
install_go_tool dnsx github.com/projectdiscovery/dnsx/cmd/dnsx@latest
install_go_tool nuclei github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
install_go_tool subzy github.com/LukaSikic/subzy@latest

echo ""
echo "[✓] All tools checked and installed as needed."
echo "[!] If any Go tool isn't recognized, add this to your shell config:"
echo '    export PATH=$PATH:$(go env GOPATH)/bin'
