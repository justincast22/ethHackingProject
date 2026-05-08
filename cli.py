import argparse
import socket
import ipaddress
from datetime import datetime, timezone


def is_ipv4(value):
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def is_cidr(value):
    try:
        ipaddress.ip_network(value, strict=False)
        return True
    except ValueError:
        return False


def is_dns_name(value):
    return not is_ipv4(value) and not is_cidr(value)


def split_comma_list(value):
    if not value:
        return []

    return [item.strip() for item in value.split(",") if item.strip()]


def default_output_name():
    now = datetime.now(timezone.utc)
    return f"host_enumeration_report_{now.strftime('%Y%m%d_%H%M')}_UTC.md"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Python-based network enumeration tool for Ethical Hacking Final Project.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Examples:
  python main.py 192.168.1.10
  python main.py 192.168.1.0/24
  python main.py scanme.nmap.org --no-ai
  python main.py 192.168.1.0/24 --exclude 192.168.1.1,192.168.1.50
  python main.py 192.168.1.10 -o reports/test_report.md
  python main.py 192.168.1.10 --ai-model gemma4:e2b
"""
    )

    parser.add_argument(
        "targets",
        help="Target IP, DNS name, CIDR subnet, or comma-separated list."
    )

    parser.add_argument(
        "--exclude",
        default="",
        help="Hosts/subnets/DNS records to exclude from scope. Supports comma-separated values."
    )

    parser.add_argument(
        "-o",
        "--output",
        default=default_output_name(),
        help="Custom output Markdown report path."
    )

    parser.add_argument(
        "--no-ai",
        action="store_true",
        help="Skip Ollama AI analysis."
    )

    parser.add_argument(
        "--ai-model",
        default="gemma4:e4b",
        help="Ollama model to use for AI analysis. Default: gemma4:e4b"
    )

    args = parser.parse_args()

    args.targets = split_comma_list(args.targets)
    args.exclude = split_comma_list(args.exclude)

    args.has_dns_targets = any(is_dns_name(target) for target in args.targets)

    return args


def get_dns_server():
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        return "Unknown"


def confirm_dns_targets(targets):
    dns_targets = [target for target in targets if is_dns_name(target)]

    print("\n[!] DNS target detected.")
    print("[!] DNS records can resolve differently depending on your DNS server.")
    print(f"[+] DNS targets: {', '.join(dns_targets)}")
    print(f"[+] Current DNS/server-related address: {get_dns_server()}")

    choice = input("Proceed with DNS-based targets? (y/N): ").strip().lower()

    return choice == "y"