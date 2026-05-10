class Host:
    """Stores information about one host."""

    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.hostname = "Unknown"
        self.domain = "Unknown"
        self.os_type = "Unknown"
        self.services = []
        self.windows_info = {}
        self.unverified_info = []
        self.command_results = []
        self.ai_analysis = None

    def update_from_nmap_result(self, nmap_result):
        """Updates the host with parsed Nmap data."""

        data = nmap_result.parsed_data

        hostname = data.get("hostname")
        domain = data.get("domain")
        os_type = data.get("os")
        services = data.get("services", [])

        if hostname and hostname != "Unknown":
            self.hostname = hostname

        if domain and domain != "Unknown":
            self.domain = domain

        if os_type and os_type != "Unknown":
            self.os_type = os_type

        self._add_services(services)
        self.command_results.append(nmap_result)

    def _add_services(self, new_services):
        """Adds new services without duplicates."""

        existing = {
            (service["port"], service["protocol"])
            for service in self.services
        }

        for service in new_services:
            key = (service["port"], service["protocol"])

            if key not in existing:
                self.services.append(service)
                existing.add(key)

    def add_command_result(self, command_result):
        """Adds a command result to the host."""

        self.command_results.append(command_result)

    def update_windows_info(self, info):
        """Adds Windows-specific information."""

        if not info:
            return

        self.windows_info.update(info)

        if "domain_name" in info and self.domain == "Unknown":
            self.domain = info["domain_name"]

        if "os" in info and self.os_type == "Unknown":
            self.os_type = info["os"]

    def add_unverified_info(self, info):
        """Adds unverified information."""

        if info:
            self.unverified_info.append(info)

    def is_windows(self):
        """Checks if the host looks like Windows."""

        os_value = self.os_type.lower()

        if "windows" in os_value:
            return True

        for service in self.services:
            service_name = service.get("service", "").lower()
            port = service.get("port")

            if port in [137, 138, 139, 445]:
                return True

            if "smb" in service_name or "netbios" in service_name:
                return True

            if "microsoft-ds" in service_name:
                return True

        return False

    def set_ai_analysis(self, analysis):
        """Stores the AI analysis result."""

        self.ai_analysis = analysis

    def services_as_text(self):
        """Formats services as plain text."""

        if not self.services:
            return "None detected"

        lines = []

        for service in self.services:
            line = (
                f"{service.get('port')}/{service.get('protocol')} "
                f"{service.get('service')}"
            )

            if service.get("version"):
                line += f" - {service.get('version')}"

            lines.append(line)

        return "\n".join(lines)

    def windows_info_as_text(self):
        """Formats Windows information as plain text."""

        if not self.windows_info:
            return "None detected"

        lines = []

        for key, value in self.windows_info.items():
            clean_key = key.replace("_", " ").title()
            lines.append(f"{clean_key}: {value}")

        return "\n".join(lines)