import ipaddress
import logging
import socket

from scanner.nmap_handler import NmapHandler


class HostDiscovery:
    """Handles target expansion and live host checks."""

    def __init__(self):
        self.nmap = NmapHandler(timeout=120)

    def expand_targets(self, targets):
        """Expands CIDR ranges into individual IPs."""

        expanded = []

        for target in targets:
            try:
                if "/" in target:
                    network = ipaddress.ip_network(
                        target,
                        strict=False
                    )

                    for ip in network.hosts():
                        expanded.append(str(ip))
                else:
                    expanded.append(target)

            except ValueError:
                expanded.append(target)

        return expanded

    def resolve_dns(self, target):
        """Resolves a DNS name to an IP."""

        try:
            return socket.gethostbyname(target)

        except socket.gaierror:
            logging.warning(
                "Could not resolve target: %s",
                target
            )

            return None

    def apply_exclusions(self, targets, exclusions):
        """Removes excluded targets from the scan list."""

        if not exclusions:
            return targets

        excluded = set(self.expand_targets(exclusions))
        final_targets = []

        for target in targets:
            resolved = self.resolve_dns(target)

            if target in excluded or resolved in excluded:
                print(f"[-] Excluding target: {target}")
                continue

            final_targets.append(target)

        return final_targets

    def discover_live_hosts(self, targets):
        """Checks which hosts are online."""

        live_hosts = []

        for target in targets:
            print(f"[+] Checking host: {target}")

            result = self.nmap.run_command(
                ["nmap", "-sn", target]
            )

            if "Host is up" in result["stdout"]:
                live_hosts.append(target)
                print(f"[+] Host is up: {target}")

            else:
                print(f"[-] Host appears down: {target}")

        return live_hosts