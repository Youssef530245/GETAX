
import socket
import dns.resolver
import os
import pyfiglet


print()
def display_center(text):
    # Get terminal width
    terminal_width = os.get_terminal_size().columns
    
    # Calculate left padding to center the text
    left_padding = (terminal_width - len(text)) // 3
    
    # Display text with padding
    print(" " * left_padding + text)

def main():
    text = "  >> GETAX <<  "
    banner = pyfiglet.figlet_format(text)
    display_center(banner)
    display_center("------------------------------------")
    display_center("---- Made by:Eng Youssef Mohamed ---")
    display_center("------------------------------------")
    display_center("------------------------------------")
    display_center("----   github.com/Youssef530245 ----")
    display_center("------------------------------------")
    print() 
    print()
    print()
if __name__ == "__main__":
    main()



#------------------------------------------------------#
def get_ip_addresses(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        ip_addresses = [ip.address for ip in result]
    except dns.resolver.NoAnswer:
        ip_addresses = []
    return ip_addresses

def main():
    print()
    url = input(". Enter the website URL: ")
    print()
    # Extract domain from the URL
    if "://" in url:
        domain = url.split("://")[1].split('/')[0]
    else:
        domain = url.split('/')[0]
    
    # Get IP addresses
    ip_addresses = get_ip_addresses(domain)
    
    if ip_addresses:
        print(f". IP addresses for {domain}:")
        print()
        for ip in ip_addresses:
            print(".",ip)
            print()
    else:
        print(f"No IP addresses found for {domain}.")

if __name__ == "__main__":
    main()
