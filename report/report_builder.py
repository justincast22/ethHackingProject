from datetime import datetime, timezone
from pathlib import Path


class ReportBuilder:
    """Builds the Markdown report."""

    def __init__(self, hosts, output_path):
        self.hosts = hosts
        self.output_path = output_path
        self.created_at = datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M UTC"
        )

    def build(self):
        """Builds the full report text."""

        lines = [
            "# Host Enumeration Report",
            "",
            f"Generated: {self.created_at}",
            "",
            "---",
            ""
        ]

        for host in self.hosts:
            lines.extend(self.build_host_section(host))

        return "\n".join(lines)

    def build_host_section(self, host):
        """Builds one host section."""

        lines = [
            f"## Host: {host.ip_address}",
            "",
            "### Verified Information",
            "",
            "| Field | Value |",
            "|---|---|",
            f"| IP Address | {host.ip_address} |",
            f"| Hostname | {host.hostname} |",
            f"| Domain | {host.domain} |",
            f"| Operating System | {host.os_type} |",
            f"| Active Services | {self.format_services(host)} |",
            (
                "| Windows-Specific Information | "
                f"{self.format_windows_info(host)} |"
            ),
            "",
            "### Unverified Information",
            ""
        ]

        if host.unverified_info:
            for item in host.unverified_info:
                lines.append(f"- {item}")
        else:
            lines.append("None identified.")

        lines.extend([
            "",
            "### AI Analysis"
        ])

        if host.ai_analysis:
            lines.extend(host.ai_analysis.to_lines())
        else:
            lines.extend([
                "> Model: N/A | Analyzed: N/A",
                "",
                "AI analysis was not performed."
            ])

        lines.extend([
            "",
            "### Command Outputs",
            ""
        ])

        if host.command_results:
            for result in host.command_results:
                lines.append(result.raw_command_output_markdown())
                lines.append("")
        else:
            lines.append("No command output recorded.")
            lines.append("")

        lines.extend([
            "---",
            ""
        ])

        return lines

    def format_services(self, host):
        """Formats services for the table."""

        if not host.services:
            return "None detected"

        services = []

        for service in host.services:
            text = (
                f"{service.get('service', 'unknown')} "
                f"({service.get('port')}/{service.get('protocol')})"
            )

            if service.get("version"):
                text += f" - {service.get('version')}"

            services.append(text)

        return "<br>".join(services)

    def format_windows_info(self, host):
        """Formats Windows info for the table."""

        if not host.windows_info:
            return "None detected"

        items = []

        for key, value in host.windows_info.items():
            clean_key = key.replace("_", " ").title()
            items.append(f"{clean_key}: {value}")

        return "<br>".join(items)

    def save(self):
        """Saves the report to disk."""

        output = Path(self.output_path)

        if output.parent != Path("."):
            output.parent.mkdir(parents=True, exist_ok=True)

        report_text = self.build()

        with open(output, "w", encoding="utf-8") as file:
            file.write(report_text)

        return str(output)