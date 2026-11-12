import os
import subprocess


def clear_terminal():
    # 'nt' é o nome interno para Windows, 'posix' cobre Linux e macOS
    if os.name == 'nt':
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)