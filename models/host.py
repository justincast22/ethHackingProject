class Host:
    """
    Represents one enumerated host.
    """

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
        data = nmap_result.parsed_data

        self.hostname = data.get("hostname", self.hostname)
        self.domain = data.get("domain", self.domain)
        self.os_type = data.get("os", self.os_type)
        self.services = data.get("services", self.services)

        self.command_results.append(nmap_result)

    def add_command_result(self, command_result):
        self.command_results.append(command_result)

    def add_unverified_info(self, info):
        if info:
            self.unverified_info.append(info)

    def is_windows(self):
        os_value = self.os_type.lower()

        return (
            "windows" in os_value
            or any(service["port"] in [139, 445] for service in self.services)
            or any("microsoft-ds" in service["service"].lower() for service in self.services)
        )

    def set_ai_analysis(self, analysis):
        self.ai_analysis = analysis

    def services_as_text(self):
        if not self.services:
            return "None detected"

        lines = []

        for service in self.services:
            version = service.get("version", "")

            line = (
                f"{service['port']}/{service['protocol']} "
                f"{service['service']}"
            )

            if version:
                line += f" - {version}"

            lines.append(line)

        return "\n".join(lines)
    