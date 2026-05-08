import requests
import sys
from datetime import datetime, timezone

from models.results import AIAnalysisResult


class OllamaAnalyzer:
    """
    Handles local Ollama communication, prompt creation, and AI analysis.
    """

    def __init__(
        self,
        model="gemma4:e4b",
        base_url="http://localhost:11434",
        timeout=120
    ):
        self.model = model
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def analyzed_timestamp(self):
        return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    def is_ollama_reachable(self):
        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=10
            )

            return response.status_code == 200

        except requests.RequestException:
            return False

    def is_model_available(self):
        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=10
            )

            if response.status_code != 200:
                return False

            data = response.json()
            models = data.get("models", [])

            return any(model.get("name") == self.model for model in models)

        except requests.RequestException:
            return False

    def build_prompt(self, host):
        services_text = host.services_as_text()

        prompt = f"""
You are acting as a penetration tester reviewing structured network enumeration results.

Analyze the host below and provide a concise security analysis.

Verified Host Information:
IP Address: {host.ip_address}
Hostname: {host.hostname}
Domain: {host.domain}
Operating System: {host.os_type}

Open Services:
{services_text}

Unverified or Probable Information:
{self.format_unverified_info(host)}

Your response must include:
1. Apparent host role
2. High-risk services or misconfigurations
3. Suggested follow-up enumeration steps
4. Relevant CVEs or vulnerability classes, if service version data is available

Keep the analysis professional, concise, and based only on the provided information.
""".strip()

        return prompt

    def format_unverified_info(self, host):
        if not host.unverified_info:
            return "None identified"

        return "\n".join(f"- {item}" for item in host.unverified_info)

    def analyze_host(self, host, no_ai=False):
        timestamp = self.analyzed_timestamp()

        if no_ai:
            return AIAnalysisResult(
                model=self.model,
                analyzed_at_utc=timestamp,
                text="",
                skipped=True,
                reason="--no-ai flag was used"
            )

        if not self.is_ollama_reachable():
            print("[!] Warning: Ollama is not reachable. Skipping AI analysis.", file=sys.stderr)

            return AIAnalysisResult(
                model=self.model,
                analyzed_at_utc=timestamp,
                text="",
                skipped=True,
                reason="Ollama was not reachable"
            )

        if not self.is_model_available():
            print(
                f"[!] Warning: Ollama model '{self.model}' is not available. Skipping AI analysis.",
                file=sys.stderr
            )

            return AIAnalysisResult(
                model=self.model,
                analyzed_at_utc=timestamp,
                text="",
                skipped=True,
                reason=f"Model '{self.model}' was not available"
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
            analysis_text = data.get("response", "").strip()

            return AIAnalysisResult(
                model=self.model,
                analyzed_at_utc=timestamp,
                text=analysis_text,
                skipped=False
            )

        except requests.RequestException as error:
            print(f"[!] Warning: Ollama request failed: {error}", file=sys.stderr)

            return AIAnalysisResult(
                model=self.model,
                analyzed_at_utc=timestamp,
                text="",
                skipped=True,
                reason=f"Ollama request failed: {error}"
            )