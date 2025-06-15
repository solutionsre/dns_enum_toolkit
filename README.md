# 🧰 DNS Enumeration Toolkit

A powerful and automated toolkit for DNS and subdomain enumeration, built with Python and Bash. It integrates the best open-source tools like Amass, DNSRecon, DNSenum, theHarvester, Nmap, Nuclei, and more — perfect for red teamers, bug bounty hunters, and security researchers.

---

## 🚀 Features

- ✅ Passive & active subdomain enumeration
- ✅ DNS brute-forcing with custom wordlists
- ✅ DNSSEC NSEC zone walking
- ✅ Live host and port detection (httpx + nmap)
- ✅ Vulnerability scanning (nuclei)
- ✅ Subdomain takeover detection (subzy)
- ✅ Easy installation with tool checker
- ✅ Optional virtualenv setup for clean Python environment

---
## 🌟 Project Goals

-Simplify reconnaissance using industry-standard tools
-Automate subdomain enumeration, DNS analysis, and vulnerability scanning
-Promote responsible use of open-source cybersecurity tools
-Empower the global infosec and bug bounty community

---
## 📂 Directory Structure
The dns_enum_toolkit/ directory contains the main Python script, installer, and requirements file for running DNS enumeration. The recon/ folder is automatically created per target domain to store all scan results.
```markdown


dns_enum_toolkit/
├── dns_enum_toolkit.py       # Main Python script
├── install.sh                # One-click installer for all dependencies
├── requirements.txt          # Python dependencies (optional)
└── recon/                    # Auto-created per domain (contains output)

```
## 📂 How to make it Running 


**Step 1: Before Running `dns_enum.py`, first run the following to make the prerequisites ready-**
Grants execution permission to the installer script and runs it with superuser rights to install all required dependencies.
```markdown
sudo chmod +x install.sh
sudo ./install.sh
```
**Step 2: This sequence sets up a clean Python virtual environment and installs all required packages from requirements.txt without affecting system Python**
```markdown
sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Step 3: Run the Main File**
```markdown
python3 dns_enum.py <url>

```

## 📤 Output
```markdown
All recon data will be stored under:
recon/example.com/
├── amass_passive.txt    # Passive subdomains from Amass
├── amass_active.txt     # Active subdomains from Amass brute force
├── all_subdomains.txt   # Combined and sorted subdomain list
├── resolved.txt         # Resolved (live) subdomains via dnsx
├── httpx.txt            # Live HTTP services and technologies
├── nuclei.txt           # Vulnerability scan results from nuclei
├── nmap_scan.nmap       # Nmap scan results for open ports
├── dnsenum_report.xml   # XML output from dnsenum
├── dnsrecon_output.xml  # XML output from dnsrecon
└── theHarvester_example.html   # HTML report from theHarvester

```

# 📊 DNS Recon Summary Report Generator

`generate_report.py` is a standalone Python script that analyzes output files from the `dns_enum_toolkit` and generates a concise, human-readable summary report of subdomains, live hosts, HTTP responses, and discovered vulnerabilities.

---

## ⚠️ Legal Disclaimer
This toolkit is intended for authorized security assessments and research only.
Do not scan any systems or domains without explicit permission. Use responsibly.

## 📬 Feedback & Suggestions

Have ideas, suggestions, or spotted a bug?  
Feel free to reach out via email: **uj.dharewa@gmail.com**

