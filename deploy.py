#!/usr/bin/env python3

import argparse
import os
import sys
import subprocess
from typing import LiteralString

COMMANDS = ['local']

class DeployScript:
    """Class for the workbench deploy script"""
    
    def __init__(self):
        self._command = self._get_command()
        self._python, self._pip = self._ensure_venv()

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

    def run(self):
        print(f'command: {self._command}')
    

if __name__ == '__main__':
    script = DeployScript()
    script.run()