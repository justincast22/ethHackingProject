import sys
from datetime import datetime, timezone

import requests

from models.results import AIAnalysisResult


class OllamaAnalyzer:
    """Handles local Ollama analysis."""

    def __init__(
        self,
        model="gemma4:e4b",
        base_url="http://localhost:11434",
        timeout=120
    ):
        self.model = model
        self.base_url = base_url
        self.timeout = timeout

    def analyze_host(self, host, no_ai=False):
        """Runs AI analysis for one host."""

        analyzed_at = datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M UTC"
        )

        if no_ai:
            return AIAnalysisResult(
                model="N/A",
                analyzed_at=analyzed_at,
                text="AI analysis was skipped because --no-ai was used."
            )

        if not self.is_ollama_running():
            print(
                "[!] Ollama is not running. Skipping AI analysis.",
                file=sys.stderr
            )

            return AIAnalysisResult(
                model=self.model,
                analyzed_at=analyzed_at,
                text="AI analysis was skipped because Ollama was unavailable."
            )

        if not self.model_exists():
            print(
                f"[!] Ollama model not found: {self.model}",
                file=sys.stderr
            )

            return AIAnalysisResult(
                model=self.model,
                analyzed_at=analyzed_at,
                text=f"AI analysis was skipped because {self.model} was not found."
            )

        prompt = self.build_prompt(host)

        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=self.timeout
            )

            response.raise_for_status()
            data = response.json()

            return AIAnalysisResult(
                model=self.model,
                analyzed_at=analyzed_at,
                text=data.get("response", "").strip()
            )

        except requests.RequestException as error:
            print(
                f"[!] Ollama request failed: {error}",
                file=sys.stderr
            )

            return AIAnalysisResult(
                model=self.model,
                analyzed_at=analyzed_at,
                text="AI analysis was skipped because the Ollama request failed."
            )

    def is_ollama_running(self):
        """Checks if Ollama is reachable."""

        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=5
            )

            return response.status_code == 200

        except requests.RequestException:
            return False

    def model_exists(self):
        """Checks if the selected model is installed."""

        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=5
            )

            response.raise_for_status()
            data = response.json()

            models = data.get("models", [])

            for model in models:
                if model.get("name") == self.model:
                    return True

            return False

        except requests.RequestException:
            return False

    def build_prompt(self, host):
        """Builds the prompt sent to Ollama."""

        services = host.services_as_text()
        windows_info = host.windows_info_as_text()

        return f"""
Act as a penetration tester reviewing enumeration results.

Give a short security analysis for this host.

Verified information:
IP Address: {host.ip_address}
Hostname: {host.hostname}
Domain: {host.domain}
Operating System: {host.os_type}

Services:
{services}

Windows Information:
{windows_info}

Include:
1. Likely role of the host
2. High-risk services or possible misconfigurations
3. Follow-up enumeration steps
4. Possible CVEs or vulnerability classes if versions are shown

Keep the answer concise.
""".strip()