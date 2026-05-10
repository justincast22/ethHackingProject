from ai.ollama_analyzer import OllamaAnalyzer
from cli import confirm_dns_targets, parse_args
from models.host import Host
from parser.nmap_parser import NmapParser
from report.report_builder import ReportBuilder
from scanner.host_discovery import HostDiscovery
from scanner.nmap_handler import NmapHandler
from utils.logger import setup_logger


def scan_host(target, nmap, parser, analyzer, no_ai):
    """Scans one host and returns a Host object."""

    print(f"\n[+] Scanning host: {target}")

    host = Host(ip_address=target)

    # Run the normal scans first.
    quick_result = nmap.tcp_quick_scan(target)
    parsed_quick = parser.parse_nmap_result(quick_result)
    host.update_from_nmap_result(parsed_quick)

    full_result = nmap.tcp_full_scan(target)
    parsed_full = parser.parse_nmap_result(full_result)
    host.update_from_nmap_result(parsed_full)

    os_result = nmap.os_detection_scan(target)
    parsed_os = parser.parse_nmap_result(os_result)
    host.update_from_nmap_result(parsed_os)

    # Run extra checks if the host looks like Windows.
    if host.is_windows():
        print("[+] Windows host found. Running extra enumeration.")

        smb_result = nmap.windows_smb_scan(target)
        parsed_smb = parser.parse_nmap_result(smb_result)
        host.add_command_result(parsed_smb)
        host.update_windows_info(
            parser.parse_windows_info(smb_result.get("stdout", ""))
        )

        netbios_result = nmap.netbios_scan(target)
        parsed_netbios = parser.parse_nmap_result(netbios_result)
        host.add_command_result(parsed_netbios)
        host.update_windows_info(
            parser.parse_windows_info(netbios_result.get("stdout", ""))
        )

        ad_result = nmap.active_directory_scan(target)
        parsed_ad = parser.parse_nmap_result(ad_result)
        host.add_command_result(parsed_ad)
        host.update_windows_info(
            parser.parse_windows_info(ad_result.get("stdout", ""))
        )

    ai_result = analyzer.analyze_host(host, no_ai=no_ai)
    host.set_ai_analysis(ai_result)

    return host


def main():
    """Runs the enumeration tool."""

    logger = setup_logger()
    args = parse_args()

    print("[+] Starting enumeration tool")

    if args.has_dns_targets:
        if not confirm_dns_targets(args.targets):
            print("[!] DNS confirmation declined. Exiting.")
            return

    discovery = HostDiscovery()
    nmap = NmapHandler(timeout=args.timeout)
    parser = NmapParser()
    analyzer = OllamaAnalyzer(
        model=args.ai_model,
        timeout=args.ai_timeout
    )

    print("[+] Expanding targets...")
    targets = discovery.expand_targets(args.targets)

    print("[+] Applying exclusions...")
    targets = discovery.apply_exclusions(targets, args.exclude)

    if not targets:
        print("[!] No targets left after exclusions.")
        return

    print(f"[+] Final targets: {targets}")

    print("[+] Checking live hosts...")
    live_hosts = discovery.discover_live_hosts(targets)

    if not live_hosts:
        print("[!] No live hosts found.")
        return

    hosts = []

    for target in live_hosts:
        host = scan_host(
            target,
            nmap,
            parser,
            analyzer,
            args.no_ai
        )

        hosts.append(host)

    print("\n[+] Building report...")
    report = ReportBuilder(
        hosts=hosts,
        output_path=args.output
    )

    saved_path = report.save()

    print(f"[+] Report saved to: {saved_path}")
    logger.info("Report saved to: %s", saved_path)


if __name__ == "__main__":
    main()