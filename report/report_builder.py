from datetime import datetime, timezone


class ReportBuilder:
    """
    Builds the final Markdown enumeration report.
    """

    def __init__(self, hosts, output_path):
        self.hosts = hosts
        self.output_path = output_path
        self.created_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    def build(self):
        lines = []

        lines.append("# Host Enumeration Report")
        lines.append("")
        lines.append(f"Generated: {self.created_at}")
        lines.append("")
        lines.append("---")
        lines.append("")

        for host in self.hosts:
            lines.extend(self.build_host_section(host))

        return "\n".join(lines)

    def build_host_section(self, host):
        lines = []

        lines.append(f"## Host: {host.ip_address}")
        lines.append("")

        lines.append("### Verified Information")
        lines.append("")
        lines.append("| Field | Value |")
        lines.append("|---|---|")
        lines.append(f"| IP Address | {host.ip_address} |")
        lines.append(f"| Hostname | {host.hostname} |")
        lines.append(f"| Domain | {host.domain} |")
        lines.append(f"| Operating System | {host.os_type} |")
        lines.append(f"| Active Services | {self.format_services(host)} |")
        lines.append("")

        lines.append("### Unverified Information")
        lines.append("")

        if host.unverified_info:
            for item in host.unverified_info:
                lines.append(f"- {item}")
        else:
            lines.append("None identified.")

        lines.append("")

        if host.ai_analysis:
            lines.append(host.ai_analysis.to_markdown())
        else:
            lines.append("### AI Analysis")
            lines.append("> Model: N/A | Analyzed: N/A")
            lines.append("")
            lines.append("AI analysis was not performed.")
            lines.append("")

        lines.append("")
        lines.append("### Command Outputs")
        lines.append("")

        if host.command_results:
            for result in host.command_results:
                lines.append(result.raw_command_output_markdown())
                lines.append("")
        else:
            lines.append("No command output recorded.")
            lines.append("")

        lines.append("---")
        lines.append("")

        return lines

    def format_services(self, host):
        if not host.services:
            return "None detected"

        service_parts = []

        for service in host.services:
            version = service.get("version", "")

            text = (
                f"{service.get('service', 'unknown')} "
                f"({service.get('port')}/{service.get('protocol')})"
            )

            if version:
                text += f" - {version}"

            service_parts.append(text)

        return "<br>".join(service_parts)

    def save(self):
        report_content = self.build()

        with open(self.output_path, "w", encoding="utf-8") as file:
            file.write(report_content)

        return self.output_path