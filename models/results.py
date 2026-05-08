class CommandResult:
    """
    Stores one executed command, raw output, errors, and parsed data.
    """

    def __init__(self, command, stdout="", stderr="", return_code=0, parsed_data=None):
        self.command = command
        self.stdout = stdout
        self.stderr = stderr
        self.return_code = return_code
        self.parsed_data = parsed_data or {}

    def raw_command_output_markdown(self):
        markdown = []

        markdown.append(f"Command: `{self.command}`")
        markdown.append("```")

        if self.stdout:
            markdown.append(self.stdout.strip())

        if self.stderr:
            markdown.append("\n[stderr]")
            markdown.append(self.stderr.strip())

        if not self.stdout and not self.stderr:
            markdown.append("[No output]")

        markdown.append("```")

        return "\n".join(markdown)


class AIAnalysisResult:
    """
    Stores AI analysis metadata and response text.
    """

    def __init__(self, model, analyzed_at_utc, text, skipped=False, reason=None):
        self.model = model
        self.analyzed_at_utc = analyzed_at_utc
        self.text = text
        self.skipped = skipped
        self.reason = reason

    def to_markdown(self):
        lines = []

        lines.append("### AI Analysis")
        lines.append(
            f"> Model: {self.model} | Analyzed: {self.analyzed_at_utc}"
        )
        lines.append("")

        if self.skipped:
            lines.append(f"AI analysis was skipped: {self.reason}")
        else:
            lines.append(self.text.strip())

        return "\n".join(lines)