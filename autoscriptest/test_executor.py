from autoscriptest.script_executor import ScriptExecutor
from autoscriptest.script_parser import ScriptParser

class TestExecutor:
    def __init__(self, script_file: str):
        self.script_file = script_file

    def execute(self):
        parser = ScriptParser(self.script_file)
        commands = parser.parse()
        script = Script(self.script_file, commands)
        executor = ScriptExecutor(script)
        executor.execute()