import argparse
import ipaddress
import socket
from datetime import datetime, timezone


def split_list(value):
    """Splits comma-separated input."""

    if not value:
        return []

    return [item.strip() for item in value.split(",") if item.strip()]


def is_ip(value):
    """Checks if a value is an IP address."""

    try:
        ipaddress.ip_address(value)
        return True

    except ValueError:
        return False


def is_cidr(value):
    """Checks if a value is CIDR notation."""

    try:
        ipaddress.ip_network(value, strict=False)
        return "/" in value

    except ValueError:
        return False


def is_dns(value):
    """Checks if a value looks like a DNS name."""

    return not is_ip(value) and not is_cidr(value)


def default_report_name():
    """Creates the default report file name."""

    now = datetime.now(timezone.utc)
    date_time = now.strftime("%Y%m%d_%H%M")

    return f"host_enumeration_report_{date_time}_UTC.md"


def get_dns_server():
    """Gets the current DNS server."""

    try:
        with open("/etc/resolv.conf", "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("nameserver"):
                    return line.split()[1]

    except FileNotFoundError:
        pass

    try:
        return socket.gethostbyname(socket.gethostname())

    except socket.gaierror:
        return "Unknown"


def confirm_dns_targets(targets):
    """Asks before scanning DNS targets."""

    dns_targets = [target for target in targets if is_dns(target)]

    print("\n[!] DNS target detected.")
    print("[!] DNS names can resolve differently depending on DNS settings.")
    print(f"[+] DNS target(s): {', '.join(dns_targets)}")
    print(f"[+] Current DNS server/address: {get_dns_server()}")

    answer = input("Proceed with DNS targets? (y/N): ").strip().lower()

    return answer == "y"


def parse_args():
    """Parses command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Network enumeration tool for Ethical Hacking.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Examples:
  python main.py 192.168.1.10
  python main.py 192.168.1.0/24
  python main.py test.local --no-ai
  python main.py 192.168.1.0/24 --exclude 192.168.1.1
  python main.py 192.168.1.10 -o reports/test_report.md
  python main.py 192.168.1.10 --ai-model gemma4:e2b

Only scan systems you own or have permission to test.
"""
    )

    parser.add_argument(
        "targets",
        help="IP, DNS name, CIDR subnet, or comma-separated list."
    )

    parser.add_argument(
        "--exclude",
        default="",
        help="Target(s) to exclude from scope."
    )

    parser.add_argument(
        "-o",
        "--output",
        default=default_report_name(),
        help="Custom Markdown report path."
    )

    parser.add_argument(
        "--no-ai",
        action="store_true",
        help="Skip Ollama AI analysis."
    )

    parser.add_argument(
        "--ai-model",
        default="gemma4:e4b",
        help="Ollama model to use. Default: gemma4:e4b"
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=300,
        help="Nmap timeout in seconds. Default: 300"
    )

    parser.add_argument(
        "--ai-timeout",
        type=int,
        default=120,
        help="Ollama timeout in seconds. Default: 120"
    )

    args = parser.parse_args()

    args.targets = split_list(args.targets)
    args.exclude = split_list(args.exclude)
    args.has_dns_targets = any(is_dns(target) for target in args.targets)

    return args