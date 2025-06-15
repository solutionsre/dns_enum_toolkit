#!/bin/bash

echo "[+] Installing required tools..."

sudo apt update && sudo apt install -y amass dnsrecon dnsenum nmap theharvester golang-go

echo "[+] Installing Go-based tools..."

go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
go install -v github.com/LukaSikic/subzy@latest

echo '[+] Make sure your PATH includes $GOPATH/bin:'
echo '    export PATH=$PATH:$(go env GOPATH)/bin'
