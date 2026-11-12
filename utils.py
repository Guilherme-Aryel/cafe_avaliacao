import os
import subprocess


def clear_terminal() -> None:
    # 'nt' é o nome interno para Windows, 'posix' cobre Linux e macOS
    
    subprocess.run(
        ["cmd", "/c", "cls"]
        if os.name == 'nt' else ["clear"],
        check=False
    )