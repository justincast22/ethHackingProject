import re
from models.results import CommandResult


class NmapParser:
    """
    Parses raw Nmap output into structured information.
    """

    def parse_ports(self, raw_output):
        services = []

        port_pattern = re.compile(
            r"^(\d+)\/(tcp|udp)\s+(\w+)\s+([\w\-\/\.]+)\s*(.*)$",
            re.MULTILINE
        )

        for match in port_pattern.finditer(raw_output):
            port = int(match.group(1))
            protocol = match.group(2)
            state = match.group(3)
            service_name = match.group(4)
            version = match.group(5).strip()

            if state == "open":
                services.append({
                    "port": port,
                    "protocol": protocol,
                    "service": service_name,
                    "version": version
                })

        return services

    def parse_hostname(self, raw_output):
        match = re.search(r"Nmap scan report for (.+)", raw_output)

        if not match:
            return "Unknown"

        value = match.group(1).strip()

        # Example: example.com (192.168.1.10)
        hostname_match = re.match(r"(.+)\s+\(([\d\.]+)\)", value)

        if hostname_match:
            return hostname_match.group(1)

        return value

    def parse_ip(self, raw_output):
        match = re.search(r"Nmap scan report for .*\(([\d\.]+)\)", raw_output)

        if match:
            return match.group(1)

        match = re.search(r"Nmap scan report for ([\d\.]+)", raw_output)

        if match:
            return match.group(1)

        return "Unknown"

    def parse_os(self, raw_output):
        os_match = re.search(r"OS details:\s*(.+)", raw_output)

        if os_match:
            return os_match.group(1).strip()

        guess_match = re.search(r"Running:\s*(.+)", raw_output)

        if guess_match:
            return guess_match.group(1).strip()

        # Basic service-based guesses
        lowered = raw_output.lower()

        if "microsoft-ds" in lowered or "netbios" in lowered or "smb" in lowered:
            return "Windows"

        if "ssh" in lowered:
            return "Linux/Unix"

        return "Unknown"

    def parse_domain(self, raw_output):
        domain_match = re.search(r"Domain name:\s*(.+)", raw_output, re.IGNORECASE)

        if domain_match:
            return domain_match.group(1).strip()

        workgroup_match = re.search(r"Workgroup:\s*(.+)", raw_output, re.IGNORECASE)

        if workgroup_match:
            return workgroup_match.group(1).strip()

        return "Unknown"

    def parse_nmap_result(self, command_result):
        raw_output = command_result.get("stdout", "")

        return CommandResult(
            command=command_result.get("command", ""),
            stdout=raw_output,
            stderr=command_result.get("stderr", ""),
            return_code=command_result.get("return_code", 0),
            parsed_data={
                "ip": self.parse_ip(raw_output),
                "hostname": self.parse_hostname(raw_output),
                "os": self.parse_os(raw_output),
                "domain": self.parse_domain(raw_output),
                "services": self.parse_ports(raw_output)
            }
        )