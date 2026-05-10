import logging
import subprocess


class NmapHandler:
    """Runs Nmap commands and returns the results."""

    def __init__(self, timeout=300):
        self.timeout = timeout

    def run_command(self, command):
        """Runs a command and returns stdout/stderr."""

        try:
            logging.info("Running command: %s", " ".join(command))

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
        """Runs a quick TCP scan."""

        command = [
            "nmap",
            "-sT",
            "-T4",
            "--top-ports",
            "1000",
            target
        ]

        return self.run_command(command)

    def tcp_full_scan(self, target):
        """Runs a full TCP scan."""

        command = [
            "nmap",
            "-sT",
            "-sV",
            "-sC",
            "-p-",
            target
        ]

        return self.run_command(command)

    def os_detection_scan(self, target):
        """Runs OS detection."""

        command = [
            "nmap",
            "-O",
            target
        ]

        return self.run_command(command)

    def windows_smb_scan(self, target):
        """Runs SMB enumeration scripts."""

        command = [
            "nmap",
            "-sT",
            "-p",
            "139,445",
            "--script",
            (
                "smb-os-discovery,"
                "smb-enum-shares,"
                "smb-enum-users,"
                "smb-security-mode"
            ),
            target
        ]

        return self.run_command(command)

    def netbios_scan(self, target):
        """Runs NetBIOS enumeration."""

        command = [
            "nmap",
            "-sT",
            "-p",
            "137,138,139",
            "--script",
            "nbstat",
            target
        ]

        return self.run_command(command)

    def active_directory_scan(self, target):
        """Checks for Active Directory related services."""

        command = [
            "nmap",
            "-sT",
            "-p",
            "53,88,135,139,389,445,464,636,3268,3269",
            "--script",
            "ldap-rootdse,smb-os-discovery",
            target
        ]

        return self.run_command(command)