from typing import List

class ScriptParser:
    def __init__(self, script_file: str):
        self.script_file = script_file

    def parse(self) -> List[str]:
        with open(self.script_file, 'r') as f:
            commands = [line.strip() for line in f.readlines()]
        return commands