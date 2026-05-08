import ipaddress
import socket
import logging
from scanner.nmap_handler import NmapHandler


class HostDiscovery:
    """
    Handles target expansion and host availability checks.
    """

    def __init__(self):
        self.nmap = NmapHandler(timeout=120)

    def expand_targets(self, targets):
        expanded_targets = []

        for target in targets:
            try:
                if "/" in target:
                    network = ipaddress.ip_network(target, strict=False)

                    for ip in network.hosts():
                        expanded_targets.append(str(ip))

                else:
                    expanded_targets.append(target)

            except ValueError:
                expanded_targets.append(target)

        return expanded_targets

    def resolve_dns(self, target):
        try:
            return socket.gethostbyname(target)
        except socket.gaierror:
            logging.warning(f"Could not resolve DNS target: {target}")
            return None

    def apply_exclusions(self, targets, exclusions):
        if not exclusions:
            return targets

        expanded_exclusions = set(self.expand_targets(exclusions))
        final_targets = []

        for target in targets:
            if target not in expanded_exclusions:
                final_targets.append(target)

        return final_targets

    def discover_live_hosts(self, targets):
        live_hosts = []

        for target in targets:
            print(f"[+] Checking if host is alive: {target}")

            result = self.nmap.run_command([
                "nmap",
                "-sn",
                target
            ])

            if "Host is up" in result["stdout"]:
                live_hosts.append(target)
                print(f"[+] Host is up: {target}")
            else:
                print(f"[-] Host appears down: {target}")

        return live_hosts