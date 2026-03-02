#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════╗
║              NRX SUBDOMAIN SCANNER v2.0                      ║
║         Created by 👑 NRX Cyber Learner 👑                   ║
║     GitHub: https://github.com/nrxcl/subdomain-scanner       ║
║                                                              ║
║     📱 Works on: Termux | Kali Linux | Ubuntu | Windows     ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import requests
import argparse
import json
import time
from datetime import datetime
import concurrent.futures
from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform colors
init(autoreset=True)

# Banner with NRX Cyber Learner branding
BANNER = f"""
{Fore.CYAN}╔{'═'*60}╗
{Fore.CYAN}║{Fore.YELLOW}              🔥 NRX SUBDOMAIN SCANNER v2.0 🔥              {Fore.CYAN}║
{Fore.CYAN}║{Fore.GREEN}                                                              {Fore.CYAN}║
{Fore.CYAN}║{Fore.MAGENTA}             Created by: 👑 NRX Cyber Learner 👑            {Fore.CYAN}║
{Fore.CYAN}║{Fore.BLUE}         📱 Termux | 💻 Kali Linux | 🪟 Windows              {Fore.CYAN}║
{Fore.CYAN}║{Fore.RED}         🔗 GitHub: NRX-Cyber-Learner/SubScanner              {Fore.CYAN}║
{Fore.CYAN}╚{'═'*60}╝{Style.RESET_ALL}
"""

# Help Menu
HELP_MENU = f"""
{Fore.CYAN}╔{'═'*60}╗
{Fore.CYAN}║{Fore.YELLOW}                      📚 HELP MENU 📚                        {Fore.CYAN}║
{Fore.CYAN}╠{'═'*60}╣{Style.RESET_ALL}

{Fore.GREEN}📌 BASIC USAGE:{Style.RESET_ALL}
  {Fore.WHITE}python nrx_scanner.py -d <domain>{Style.RESET_ALL}
  
{Fore.GREEN}🎯 COMMAND LINE ARGUMENTS:{Style.RESET_ALL}

  {Fore.YELLOW}-d, --domain{Style.RESET_ALL}        {Fore.CYAN}Target domain (required){Style.RESET_ALL}
                        Example: -d google.com
                        
  {Fore.YELLOW}-w, --wordlist{Style.RESET_ALL}      {Fore.CYAN}Path to subdomain wordlist file{Style.RESET_ALL}
                        Example: -w wordlists/subdomains.txt
                        Default: Built-in wordlist
                        
  {Fore.YELLOW}-t, --threads{Style.RESET_ALL}       {Fore.CYAN}Number of threads for scanning{Style.RESET_ALL}
                        Example: -t 50
                        Default: 20
                        Range: 1-500
                        
  {Fore.YELLOW}-o, --output{Style.RESET_ALL}        {Fore.CYAN}Output format for results{Style.RESET_ALL}
                        Example: -o json
                        Options: txt, json, csv
                        Default: txt
                        
  {Fore.YELLOW}-s, --save{Style.RESET_ALL}          {Fore.CYAN}Save results to file{Style.RESET_ALL}
                        Example: -s results.txt
                        Default: Auto-generated filename
                        
  {Fore.YELLOW}-p, --protocol{Style.RESET_ALL}      {Fore.CYAN}Protocol to use (http/https){Style.RESET_ALL}
                        Example: -p https
                        Default: http
                        
  {Fore.YELLOW}-T, --timeout{Style.RESET_ALL}       {Fore.CYAN}Timeout in seconds{Style.RESET_ALL}
                        Example: -T 5
                        Default: 3
                        
  {Fore.YELLOW}-v, --verbose{Style.RESET_ALL}       {Fore.CYAN}Verbose output{Style.RESET_ALL}
                        Example: -v
                        Shows all requests including errors
                        
  {Fore.YELLOW}--no-color{Style.RESET_ALL}          {Fore.CYAN}Disable colored output{Style.RESET_ALL}
                        Example: --no-color
                        
  {Fore.YELLOW}--no-banner{Style.RESET_ALL}         {Fore.CYAN}Hide banner{Style.RESET_ALL}
                        Example: --no-banner
                        
  {Fore.YELLOW}--source-scan{Style.RESET_ALL}       {Fore.CYAN}Enable source scanning (crt.sh){Style.RESET_ALL}
                        Example: --source-scan
                        
  {Fore.YELLOW}-h, --help{Style.RESET_ALL}          {Fore.CYAN}Show this help menu{Style.RESET_ALL}

{Fore.GREEN}💡 EXAMPLES:{Style.RESET_ALL}

  {Fore.WHITE}1. Basic scan:{Style.RESET_ALL}
     {Fore.CYAN}python nrx_scanner.py -d example.com{Style.RESET_ALL}
     
  {Fore.WHITE}2. Advanced scan with wordlist:{Style.RESET_ALL}
     {Fore.CYAN}python nrx_scanner.py -d example.com -w wordlist.txt -t 100 -o json{Style.RESET_ALL}
     
  {Fore.WHITE}3. Fast scan with source checking:{Style.RESET_ALL}
     {Fore.CYAN}python nrx_scanner.py -d example.com -t 200 --source-scan -v{Style.RESET_ALL}
     
  {Fore.WHITE}4. Save results to specific file:{Style.RESET_ALL}
     {Fore.CYAN}python nrx_scanner.py -d example.com -s myresults.txt{Style.RESET_ALL}
     
  {Fore.WHITE}5. HTTPS scan with 5 second timeout:{Style.RESET_ALL}
     {Fore.CYAN}python nrx_scanner.py -d example.com -p https -T 5{Style.RESET_ALL}

{Fore.GREEN}📊 OUTPUT FORMATS:{Style.RESET_ALL}
  {Fore.YELLOW}txt{Style.RESET_ALL}  - Simple text file with URLs and status codes
  {Fore.YELLOW}json{Style.RESET_ALL} - JSON format for parsing with other tools
  {Fore.YELLOW}csv{Style.RESET_ALL}  - CSV format for Excel/Spreadsheets

{Fore.GREEN}⚡ PERFORMANCE TIPS:{Style.RESET_ALL}
  • Use {Fore.YELLOW}-t 100{Style.RESET_ALL} for faster scanning
  • Use {Fore.YELLOW}--source-scan{Style.RESET_ALL} to find more subdomains
  • Use {Fore.YELLOW}-p https{Style.RESET_ALL} for HTTPS-only sites
  • Adjust {Fore.YELLOW}--timeout{Style.RESET_ALL} for slow networks

{Fore.GREEN}⚠️  DISCLAIMER:{Style.RESET_ALL}
  This tool is for educational purposes only.
  Only use on domains you have permission to test.
  
{Fore.CYAN}╠{'═'*60}╣
{Fore.CYAN}║{Fore.MAGENTA}           👑 NRX Cyber Learner - Happy Hacking! 👑          {Fore.CYAN}║
{Fore.CYAN}╚{'═'*60}╝{Style.RESET_ALL}
"""

class NRXSubdomainScanner:
    def __init__(self, args):
        self.args = args
        self.found_subdomains = []
        self.live_subdomains = []
        self.start_time = time.time()
        self.total_checked = 0
        self.errors = 0
        
    def print_banner(self):
        """Print tool banner"""
        if not self.args.no_banner:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(BANNER)
            print(f"{Fore.CYAN}[⏰] Scan Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}\n")
        
    def print_help(self):
        """Print help menu"""
        print(HELP_MENU)
        sys.exit(0)
        
    def check_dependencies(self):
        """Check if required packages are installed"""
        try:
            import requests
            import colorama
            return True
        except ImportError as e:
            print(f"{Fore.RED}[✗] Missing dependency: {e}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[!] Run: pip install requests colorama{Style.RESET_ALL}")
            return False
            
    def load_wordlist(self, wordlist_file):
        """Load subdomain wordlist"""
        try:
            if wordlist_file and os.path.exists(wordlist_file):
                with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
                    wordlist = [line.strip() for line in f if line.strip()]
                print(f"{Fore.GREEN}[✓] Loaded {len(wordlist)} subdomains from {wordlist_file}{Style.RESET_ALL}")
                return wordlist
            else:
                if wordlist_file:
                    print(f"{Fore.YELLOW}[!] Wordlist {wordlist_file} not found, using default wordlist{Style.RESET_ALL}")
                else:
                    print(f"{Fore.YELLOW}[!] No wordlist provided, using default wordlist{Style.RESET_ALL}")
                
                # Default wordlist
                return ["www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "webdisk", 
                       "ns2", "cpanel", "whm", "autodiscover", "autoconfig", "m", "imap", "test", 
                       "ns", "blog", "pop3", "dev", "www2", "admin", "forum", "news", "vpn", 
                       "ns3", "mail2", "new", "mysql", "old", "lists", "support", "mobile", 
                       "mx", "static", "docs", "beta", "shop", "sql", "secure", "demo", 
                       "cp", "calendar", "wiki", "web", "media", "email", "images", "img", 
                       "www1", "intranet", "portal", "video", "sip", "dns2", "api", "cdn", 
                       "stats", "dns1", "help", "vps", "apps", "mx1", "pma", "mx2", "adminer",
                       "server", "backup", "cloud", "remote", "exchange", "owa", "remoteaccess"]
        except Exception as e:
            print(f"{Fore.RED}[✗] Error loading wordlist: {e}{Style.RESET_ALL}")
            return []
            
    def check_subdomain(self, subdomain, domain):
        """Check if subdomain exists and is live"""
        protocol = self.args.protocol
        url = f"{protocol}://{subdomain}.{domain}"
        
        try:
            # Set timeout and headers to avoid blocking
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) NRXCyberScanner/2.0'
            }
            response = requests.get(url, timeout=self.args.timeout, headers=headers, allow_redirects=True)
            
            self.total_checked += 1
            
            if response.status_code < 400 or response.status_code in [401, 403, 404]:
                result = {
                    'subdomain': f"{subdomain}.{domain}",
                    'url': url,
                    'status_code': response.status_code,
                    'server': response.headers.get('Server', 'Unknown'),
                    'content_length': len(response.content),
                    'title': self.get_page_title(response.text)
                }
                
                # Color coding based on status code
                if not self.args.no_color:
                    if response.status_code < 300:
                        status_color = Fore.GREEN
                    elif response.status_code < 400:
                        status_color = Fore.YELLOW
                    else:
                        status_color = Fore.RED
                else:
                    status_color = ""
                
                print(f"{Fore.CYAN}[✓]{Style.RESET_ALL} {url} {status_color}[{response.status_code}]{Style.RESET_ALL} - {result['title'][:30]}")
                
                return result
            elif self.args.verbose:
                print(f"{Fore.RED}[✗]{Style.RESET_ALL} {url} [{response.status_code}]")
                
        except requests.ConnectionError:
            self.errors += 1
            if self.args.verbose:
                print(f"{Fore.RED}[!]{Style.RESET_ALL} {url} - Connection Error")
        except requests.Timeout:
            self.errors += 1
            if self.args.verbose:
                print(f"{Fore.RED}[!]{Style.RESET_ALL} {url} - Timeout")
        except Exception as e:
            self.errors += 1
            if self.args.verbose:
                print(f"{Fore.RED}[!]{Style.RESET_ALL} {url} - {str(e)[:30]}")
                
        return None
        
    def get_page_title(self, html):
        """Extract page title from HTML"""
        try:
            start = html.find('<title>') + 7
            end = html.find('</title>', start)
            if start > 6 and end > start:
                return html[start:end].strip()
        except:
            pass
        return "No Title"
        
    def scan_with_multiple_sources(self, domain):
        """Scan using multiple sources (Certificate Transparency, etc.)"""
        if not self.args.source_scan:
            return []
            
        print(f"{Fore.YELLOW}[*] Scanning using multiple sources...{Style.RESET_ALL}")
        
        # Source 1: crt.sh (Certificate Transparency)
        try:
            url = f"https://crt.sh/?q=%25.{domain}&output=json"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for item in data:
                    name = item.get('name_value', '')
                    if name:
                        for sub in name.split('\n'):
                            if sub.endswith(f".{domain}") and sub not in self.found_subdomains:
                                self.found_subdomains.append(sub)
                                print(f"{Fore.MAGENTA}[CT]{Style.RESET_ALL} Found: {sub}")
        except:
            pass
            
        print(f"{Fore.GREEN}[✓] Found {len(self.found_subdomains)} subdomains from sources{Style.RESET_ALL}")
        return self.found_subdomains
        
    def save_results(self, domain):
        """Save scan results to file"""
        if not self.live_subdomains:
            print(f"{Fore.YELLOW}[!] No results to save{Style.RESET_ALL}")
            return None
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if self.args.save:
            filename = self.args.save
        else:
            filename = f"NRX_scan_{domain}_{timestamp}.{self.args.output}"
        
        try:
            if self.args.output == "txt":
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"# NRX Subdomain Scanner Results\n")
                    f.write(f"# Target: {domain}\n")
                    f.write(f"# Date: {datetime.now()}\n")
                    f.write(f"# Found: {len(self.live_subdomains)} live subdomains\n")
                    f.write(f"{'='*50}\n\n")
                    
                    for sub in self.live_subdomains:
                        f.write(f"{sub['url']} [{sub['status_code']}] - {sub['title']}\n")
                        
            elif self.args.output == "json":
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump({
                        'target': domain,
                        'scan_date': str(datetime.now()),
                        'total_found': len(self.live_subdomains),
                        'scan_time': f"{time.time() - self.start_time:.2f}s",
                        'results': self.live_subdomains
                    }, f, indent=4)
                    
            elif self.args.output == "csv":
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("URL,Status Code,Server,Title,Content Length\n")
                    for sub in self.live_subdomains:
                        f.write(f"{sub['url']},{sub['status_code']},{sub['server']},{sub['title']},{sub['content_length']}\n")
                        
            print(f"{Fore.GREEN}[✓] Results saved to: {filename}{Style.RESET_ALL}")
            return filename
            
        except Exception as e:
            print(f"{Fore.RED}[✗] Error saving results: {e}{Style.RESET_ALL}")
            return None
        
    def run_scan(self):
        """Main scan function"""
        domain = self.args.domain
        
        self.print_banner()
        
        # Check dependencies
        if not self.check_dependencies():
            sys.exit(1)
            
        print(f"{Fore.YELLOW}[🎯] Target Domain: {Fore.WHITE}{domain}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[⚡] Threads: {self.args.threads}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[📁] Protocol: {self.args.protocol}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[⏱️] Timeout: {self.args.timeout}s{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[📊] Output Format: {self.args.output}{Style.RESET_ALL}\n")
        
        # Load wordlist
        wordlist = self.load_wordlist(self.args.wordlist)
        
        if not wordlist:
            print(f"{Fore.RED}[✗] No wordlist to scan{Style.RESET_ALL}")
            return
            
        # First, try to find from certificate sources
        if self.args.source_scan:
            print(f"\n{Fore.CYAN}[🔍] Phase 1: Gathering subdomains from public sources...{Style.RESET_ALL}")
            self.scan_with_multiple_sources(domain)
        
        # Then brute force with wordlist
        print(f"\n{Fore.CYAN}[🔍] Phase 2: Brute-forcing with wordlist...{Style.RESET_ALL}")
        
        total = len(wordlist)
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.args.threads) as executor:
            # Submit all tasks
            future_to_sub = {executor.submit(self.check_subdomain, sub, domain): sub for sub in wordlist}
            
            # Process completed tasks
            for i, future in enumerate(concurrent.futures.as_completed(future_to_sub), 1):
                result = future.result()
                if result:
                    self.live_subdomains.append(result)
                
                # Progress indicator
                if not self.args.no_color and i % 50 == 0:
                    progress = (i / total) * 100
                    print(f"{Fore.BLUE}[📊] Progress: {i}/{total} ({progress:.1f}%) checked{Style.RESET_ALL}")
        
        # Final results
        elapsed_time = time.time() - self.start_time
        print(f"\n{Fore.GREEN}{'='*50}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[✅] SCAN COMPLETED!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[📊] Total subdomains checked: {self.total_checked}")
        print(f"{Fore.YELLOW}[📊] Live subdomains found: {len(self.live_subdomains)}")
        print(f"{Fore.YELLOW}[⚠️]  Errors encountered: {self.errors}")
        print(f"{Fore.YELLOW}[⏱️] Time taken: {elapsed_time:.2f} seconds")
        
        # Save results
        if self.live_subdomains:
            filename = self.save_results(domain)
            if filename:
                print(f"{Fore.GREEN}[📁] Results saved in: {filename}{Style.RESET_ALL}")
            
            # Show live subdomains
            print(f"\n{Fore.CYAN}[📋] Live Subdomains:{Style.RESET_ALL}")
            for idx, sub in enumerate(self.live_subdomains, 1):
                print(f"{Fore.CYAN}[{idx}]{Style.RESET_ALL} {sub['url']} {Fore.GREEN}[{sub['status_code']}]{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}[!] No live subdomains found{Style.RESET_ALL}")
            
        return self.live_subdomains

def main():
    """Main function with argument parsing"""
    parser = argparse.ArgumentParser(
        description='🔥 NRX Subdomain Scanner - Created by NRX Cyber Learner',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        add_help=False  # We'll handle help manually
    )
    
    # Basic arguments
    parser.add_argument('-d', '--domain', help='Target domain (e.g., google.com)')
    parser.add_argument('-w', '--wordlist', help='Path to subdomain wordlist file')
    parser.add_argument('-t', '--threads', type=int, default=20, help='Number of threads (default: 20)')
    parser.add_argument('-o', '--output', choices=['txt', 'json', 'csv'], default='txt', help='Output format (default: txt)')
    parser.add_argument('-s', '--save', help='Save results to specific file')
    parser.add_argument('-p', '--protocol', choices=['http', 'https'], default='http', help='Protocol to use (default: http)')
    parser.add_argument('-T', '--timeout', type=int, default=3, help='Timeout in seconds (default: 3)')
    
    # Feature flags
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--source-scan', action='store_true', help='Enable source scanning (crt.sh)')
    parser.add_argument('--no-color', action='store_true', help='Disable colored output')
    parser.add_argument('--no-banner', action='store_true', help='Hide banner')
    
    # Help argument
    parser.add_argument('-h', '--help', action='store_true', help='Show this help menu')
    
    args = parser.parse_args()
    
    # Show help menu if requested or no domain provided
    if args.help or not args.domain:
        scanner = NRXSubdomainScanner(args)
        scanner.print_help()
    
    # Validate threads
    if args.threads < 1 or args.threads > 500:
        print(f"{Fore.RED}[✗] Threads must be between 1 and 500{Style.RESET_ALL}")
        sys.exit(1)
    
    # Create scanner instance
    scanner = NRXSubdomainScanner(args)
    
    # Run scan
    try:
        scanner.run_scan()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Scan interrupted by user{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[✗] Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == "__main__":
    main()
