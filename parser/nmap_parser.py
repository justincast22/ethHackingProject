import re

from models.results import CommandResult


class NmapParser:
    """Parses Nmap output into structured data."""

    def parse_ports(self, raw_output):
        """Finds open ports and services."""

        services = []

        pattern = re.compile(
            r"^(\d+)\/(tcp|udp)\s+(\w+)\s+([\w\-\/\.]+)\s*(.*)$",
            re.MULTILINE
        )

        for match in pattern.finditer(raw_output):
            port = int(match.group(1))
            protocol = match.group(2)
            state = match.group(3)
            service = match.group(4)
            version = match.group(5).strip()

            if state == "open":
                services.append({
                    "port": port,
                    "protocol": protocol,
                    "service": service,
                    "version": version
                })

        return services

    def parse_hostname(self, raw_output):
        """Gets the hostname from Nmap output."""

        match = re.search(
            r"Nmap scan report for (.+)",
            raw_output
        )

        if not match:
            return "Unknown"

        value = match.group(1).strip()

        hostname_match = re.match(
            r"(.+)\s+\(([\d\.]+)\)",
            value
        )

        if hostname_match:
            return hostname_match.group(1)

        return value

    def parse_ip(self, raw_output):
        """Gets the IP address."""

        match = re.search(
            r"Nmap scan report for .*\(([\d\.]+)\)",
            raw_output
        )

        if match:
            return match.group(1)

        match = re.search(
            r"Nmap scan report for ([\d\.]+)",
            raw_output
        )

        if match:
            return match.group(1)

        return "Unknown"

    def parse_os(self, raw_output):
        """Attempts to identify the OS."""

        os_match = re.search(
            r"OS details:\s*(.+)",
            raw_output
        )

        if os_match:
            return os_match.group(1).strip()

        lowered = raw_output.lower()

        if "windows" in lowered:
            return "Windows"

        if "linux" in lowered:
            return "Linux"

        return "Unknown"

    def parse_domain(self, raw_output):
        """Looks for domain information."""

        patterns = [
            r"Domain name:\s*(.+)",
            r"DNS_Domain_Name:\s*(.+)",
            r"NetBIOS_Domain_Name:\s*(.+)"
        ]

        for pattern in patterns:
            match = re.search(
                pattern,
                raw_output,
                re.IGNORECASE
            )

            if match:
                return match.group(1).strip()

        return "Unknown"

    def parse_windows_info(self, raw_output):
        """Finds Windows-related information."""

        info = {}

        patterns = {
            "computer_name": r"Computer name:\s*(.+)",
            "domain_name": r"Domain name:\s*(.+)",
            "fqdn": r"FQDN:\s*(.+)",
            "os": r"OS:\s*(.+)"
        }

        for key, pattern in patterns.items():
            match = re.search(
                pattern,
                raw_output,
                re.IGNORECASE
            )

            if match:
                info[key] = match.group(1).strip()

        return info

    def parse_nmap_result(self, command_result):
        """Builds a parsed result object."""

        raw_output = command_result.get("stdout", "")

        return CommandResult(
            command=command_result.get("command", ""),
            stdout=raw_output,
            stderr=command_result.get("stderr", ""),
            return_code=command_result.get(
                "return_code",
                0
            ),
            parsed_data={
                "ip": self.parse_ip(raw_output),
                "hostname": self.parse_hostname(raw_output),
                "os": self.parse_os(raw_output),
                "domain": self.parse_domain(raw_output),
                "services": self.parse_ports(raw_output)
            }
        )