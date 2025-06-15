import os
import sys

def generate_report(domain):
    base_path = f"recon/{domain}"
    if not os.path.exists(base_path):
        print(f"[-] Recon folder for domain '{domain}' does not exist.")
        return

    os.chdir(base_path)
    report_path = f"summary_{domain}.txt"
    with open(report_path, "w") as report:
        report.write(f"DNS Enumeration Report for {domain}\n")
        report.write("=" * 50 + "\n\n")

        # Count total subdomains
        if os.path.exists("all_subdomains.txt"):
            subs = open("all_subdomains.txt").read().splitlines()
            report.write(f"🔸 Total Subdomains Found: {len(subs)}\n")

        # Count resolved hosts
        if os.path.exists("resolved.txt"):
            resolved = open("resolved.txt").read().splitlines()
            report.write(f"🔸 Live Hosts (DNS Resolved): {len(resolved)}\n")

        # Analyze httpx results
        if os.path.exists("httpx.txt"):
            httpx_lines = open("httpx.txt").read().splitlines()
            http_200 = [line for line in httpx_lines if "200" in line]
            http_500 = [line for line in httpx_lines if "500" in line]
            report.write(f"🔹 Web Servers (200 OK): {len(http_200)}\n")
            report.write(f"🔸 Web Errors (500): {len(http_500)}\n")

        # Analyze nuclei findings
        if os.path.exists("nuclei.txt"):
            nuclei = open("nuclei.txt").read().splitlines()
            report.write(f"🔴 Vulnerabilities Detected: {len(nuclei)}\n")
            if nuclei:
                report.write("⚠️ Top Critical Findings:\n")
                for line in nuclei[:5]:
                    report.write(f"  - {line}\n")

        report.write("\n✅ Recommendations:\n")
        report.write("- Secure and monitor all subdomains.\n")
        report.write("- Investigate HTTP errors (500s).\n")
        report.write("- Patch all CVEs reported by nuclei.\n")
        report.write("- Limit exposed services and ports.\n")
        report.write("- Use HTTPS and monitor SSL/TLS certs.\n")

    print(f"[✓] Summary report generated: {base_path}/{report_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate_report.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    generate_report(domain)