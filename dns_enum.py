import os
import subprocess
from datetime import datetime

def run_command(command, description=""):
    print(f"\n[+] {description}...")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running: {command}")
        print(e)

def make_dirs(domain):
    base_dir = f"recon/{domain}"
    os.makedirs(base_dir, exist_ok=True)
    os.chdir(base_dir)
    return base_dir

def run_recon(domain):
    base_dir = make_dirs(domain)

    # Step 1: theHarvester
    run_command(f"theHarvester -d {domain} -b all -f theHarvester_{domain}.html", "Running theHarvester")

    # Step 2: Amass Passive
    run_command(f"amass enum -passive -d {domain} -o amass_passive.txt", "Running Amass Passive")

    # Step 3: Amass Active Brute
    run_command(f"amass enum -active -brute -d {domain} -o amass_active.txt", "Running Amass Active Brute")

    # Step 4: dnsenum
    run_command(f"dnsenum {domain} -o dnsenum_report.xml", "Running dnsenum")

    # Step 5: dnsrecon
    run_command(f"dnsrecon -d {domain} -a -b --xml dnsrecon_output.xml", "Running dnsrecon")

    # Step 6: Resolve subdomains
    run_command("cat amass_passive.txt amass_active.txt | sort -u > all_subdomains.txt", "Merging subdomains")
    run_command("cat all_subdomains.txt | dnsx -a -aaaa -cname -silent -o resolved.txt", "Resolving with dnsx")

    # Step 7: Port scanning with nmap
    run_command("nmap -iL resolved.txt -Pn -sS -T4 -p 80,443,8080,8443 -oA nmap_scan", "Running nmap port scan")

    # Step 8: Check for live HTTP services
    run_command("cat resolved.txt | httpx -status-code -title -tech-detect -ip -silent -o httpx.txt", "Running httpx")

    # Step 9: Vulnerability scanning with nuclei
    run_command("cat httpx.txt | nuclei -severity high,critical -silent -o nuclei.txt", "Running nuclei")

    # Step 10: DNSSEC zone walking (optional)
    run_command(f"nmap -sSU -p 53 --script dns-nsec-enum --script-args dns-nsec-enum.domains={domain} {domain}", "Running NSEC zone walk with nmap")

    print(f"\n[✓] Recon complete. Results saved in: {base_dir}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 dns_enum_toolkit.py example.com")
        sys.exit(1)

    domain = sys.argv[1]
    start_time = datetime.now()
    print(f"\n[📡] Starting DNS Enumeration for {domain} at {start_time}")
    run_recon(domain)
    print(f"\n[✅] Finished in: {datetime.now() - start_time}")
