import ipaddress
import re

class IPAddressAnalyzer:
    def __init__(self, filename='ip.txt'):
        self.filename = filename
        self.valid_public_ips = []
        self.valid_private_ips = []
        self.unique_domains = set()
        self.unique_ips = set()

    def read_and_process_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = re.split(r'[\s,\t]+', line)
                    if len(parts) == 2:
                        ip, domain = parts
                        self.process_entry(ip, domain)
                    else:
                        print(f"Unexpected format or missing information in line: '{line}'")
        except FileNotFoundError:
            print(f"The file {self.filename} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def process_entry(self, ip, domain):
        try:
            ip_obj = ipaddress.ip_address(ip)
            self.unique_ips.add(ip)
            if ip_obj.is_private:
                self.valid_private_ips.append(f"{ip} - {domain}")
            else:
                self.valid_public_ips.append(f"{ip} - {domain}")
            self.unique_domains.add(domain)
        except ValueError:
            print(f"Invalid IP address found: {ip}")

    def display_valid_ips(self):
        print("Valid Public IPs:")
        for ip in self.valid_public_ips:
            print(ip)
        print("Valid Private IPs:")
        for ip in self.valid_private_ips:
            print(ip)

    def display_unique_domains(self):
        print("Unique Domains:")
        for domain in self.unique_domains:
            print(domain)

    def display_unique_ips(self):
        print("Unique Public and Private IPs:")
        for ip in self.unique_ips:
            print(ip)

if __name__ == "__main__":
    ip_analyzer = IPAddressAnalyzer()
    ip_analyzer.read_and_process_file()
    ip_analyzer.display_valid_ips()
    ip_analyzer.display_unique_domains()
    ip_analyzer.display_unique_ips()
