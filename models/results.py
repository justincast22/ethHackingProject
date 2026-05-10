from dataclasses import dataclass, field


@dataclass
class CommandResult:
    """Stores command output and parsed data."""

    command: str
    stdout: str
    stderr: str
    return_code: int
    parsed_data: dict = field(default_factory=dict)

    def raw_command_output_markdown(self):
        """Formats the command output for the report."""

        output = [
            f"Command: `{self.command}`",
            "```"
        ]

        if self.stdout:
            output.append(self.stdout.strip())

        if self.stderr:
            output.append("")
            output.append("[stderr]")
            output.append(self.stderr.strip())

        output.append("```")

        return "\n".join(output)


@dataclass
class AIAnalysisResult:
    """Stores AI analysis information."""

    model: str
    analyzed_at: str
    text: str

    def to_lines(self):
        """Formats AI analysis for the report."""

        return [
            f"> Model: {self.model} | Analyzed: {self.analyzed_at}",
            "",
            self.text
        ]