from cli import parse_args, confirm_dns_targets
from scanner.host_discovery import HostDiscovery
from scanner.nmap_handler import NmapHandler
from parser.nmap_parser import NmapParser
from models.host import Host
from ai.ollama_analyzer import OllamaAnalyzer
from report.report_builder import ReportBuilder
from utils.logger import setup_logger


def main():
    logger = setup_logger()
    args = parse_args()

    print("[+] Starting enumeration tool")

    if args.has_dns_targets:
        confirmed = confirm_dns_targets(args.targets)

        if not confirmed:
            print("[!] DNS target confirmation declined. Exiting.")
            return

    discovery = HostDiscovery()
    nmap = NmapHandler()
    parser = NmapParser()

    print("[+] Expanding targets...")
    targets = discovery.expand_targets(args.targets)

    print("[+] Applying exclusions...")
    targets = discovery.apply_exclusions(targets, args.exclude)

    print(f"[+] Final targets: {targets}")

    print("[+] Discovering live hosts...")
    live_hosts = discovery.discover_live_hosts(targets)

    if not live_hosts:
        print("[!] No live hosts found. Exiting.")
        return

    hosts = []

    for target in live_hosts:
        print(f"[+] Scanning host: {target}")

        scan_result = nmap.tcp_full_scan(target)
        parsed_result = parser.parse_nmap_result(scan_result)

        host = Host(ip_address=target)
        host.update_from_nmap_result(parsed_result)

        if host.is_windows():
            print(f"[+] Windows host detected. Running SMB enumeration: {target}")
            smb_result = nmap.windows_smb_scan(target)
            parsed_smb_result = parser.parse_nmap_result(smb_result)
            host.add_command_result(parsed_smb_result)

        analyzer = OllamaAnalyzer(model=args.ai_model)
        ai_result = analyzer.analyze_host(host, no_ai=args.no_ai)
        host.set_ai_analysis(ai_result)

        hosts.append(host)

    print("[+] Building report...")
    report = ReportBuilder(hosts=hosts, output_path=args.output)
    saved_path = report.save()

    print(f"[+] Report saved to: {saved_path}")
    logger.info(f"Report saved to: {saved_path}")


if __name__ == "__main__":
    main()