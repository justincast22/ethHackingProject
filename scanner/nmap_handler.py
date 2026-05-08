import subprocess
import logging


class NmapHandler:
    """
    Handles running Nmap commands and returning raw output.
    """

    def __init__(self, timeout=300):
        self.timeout = timeout

    def run_command(self, command):
        try:
            logging.info(f"Running command: {' '.join(command)}")

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )

            return {
                "command": " ".join(command),
                "stdout": result.stdout,
                "stderr": result.stderr,
                "return_code": result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                "command": " ".join(command),
                "stdout": "",
                "stderr": "Command timed out",
                "return_code": -1
            }

        except Exception as error:
            return {
                "command": " ".join(command),
                "stdout": "",
                "stderr": str(error),
                "return_code": -1
            }

    def tcp_quick_scan(self, target):
        # TCP Connect Scan (does not require sudo)
        command = ["nmap", "-sT", "-T4", "--top-ports", "1000", target]
        return self.run_command(command)

    def tcp_full_scan(self, target):
        # Full TCP Connect Scan with service/version detection
        command = ["nmap", "-sT", "-sV", "-sC", "-p-", target]
        return self.run_command(command)

    def os_detection_scan(self, target):
        # OS detection may still require sudo/root on some systems
        command = ["nmap", "-O", target]
        return self.run_command(command)

    def windows_smb_scan(self, target):
        command = [
            "nmap",
            "-sT",
            "-p",
            "139,445",
            "--script",
            "smb-os-discovery,smb-enum-shares,smb-enum-users",
            target
        ]

        return self.run_command(command)