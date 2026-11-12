import json

from pathlib import Path
from typing import Any


class JSONHandler:

    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path


    def read_json(self, default: Any = None) -> Any:
        with open(self.file_path, 'r') as file:
            try:
                return json.load(file) if file.readable() else default
            except json.JSONDecodeError:
                return default


    def write_json(self, data: Any) -> None:
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)