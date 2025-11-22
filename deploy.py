#!/usr/bin/env python3

import argparse
import os
import sys
import subprocess
from typing import LiteralString

COMMANDS = ['install', 'local']

class DeployScript:
    """Class for the workbench deploy script"""
    
    def __init__(self):
        self._command = self._get_command()
        self._python, self._pip = self._ensure_venv()
        self._install_requirements()

    def run(self):
        handle_func = getattr(self, f"_command_{self._command.lower()}")
        handle_func()

    def _get_command(self) -> str:
        parser = argparse.ArgumentParser(description="Workbench deploy script.")
        parser.add_argument("command", type=str, choices=COMMANDS, help="Deploy command")

        args = parser.parse_args()
        return args.command

    def _ensure_venv(self) -> tuple[LiteralString, LiteralString]:
        """Checks if local venv exists, creates if not."""
        if not os.path.exists(".venv"):
            print("Creating local virtual environment (.venv)...")
            subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        return os.path.join(".venv", "bin", "python"), os.path.join(".venv", "bin", "pip")
    
    def _install_requirements(self):
        """Installs dependencies from requirements.txt."""
        print("Installing dependencies...")
        command = [self._pip, "install", "-r", "requirements.txt"]
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
    
    def _command_local(self):
        print("Running local flask server in debug mode...")
        command = [self._python, "-m", "flask", "--app", "api.app", "run", "--debug"]
        try:
            subprocess.run(command, check=True)
        except KeyboardInterrupt:
            print("\nServer stopped.")

    def _command_install(self):
        print("Python modules installed.")

if __name__ == '__main__':
    script = DeployScript()
    script.run()