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

```markdown
## 📂 Directory Structure

```The dns_enum_toolkit/ directory contains the main Python script, installer, and requirements file for running DNS enumeration. The recon/ folder is automatically created per target domain to store all scan results.

dns_enum_toolkit/
├── dns_enum_toolkit.py       # Main Python script
├── install.sh                # One-click installer for all dependencies
├── requirements.txt          # Python dependencies (optional)
└── recon/                    # Auto-created per domain (contains output)
