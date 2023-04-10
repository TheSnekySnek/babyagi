import subprocess
import sys

def execute_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE)
    return result.stdout.decode()