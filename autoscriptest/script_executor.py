from dataclasses import dataclass
from typing import List

@dataclass
class Script:
    name: str
    commands: List[str]

class ScriptExecutor:
    def __init__(self, script: Script):
        self.script = script

    def execute(self):
        for command in self.script.commands:
            print(f"Executing command: {command}")