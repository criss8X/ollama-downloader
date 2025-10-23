import re
import subprocess

def _run_cmd(command):
    try:
        subprocess.run(
            args=command,
            check=True,
            capture_output=True
        )

        return True

    except:
        return False

def gb_size(size):
    match = re.match(r"^(\d+(?:\.\d+)?)([A-Za-z]+)$", size.strip())
    
    if match:
        value = float(match.group(1))
        unit = match.group(2).upper()

        match unit:
            case "MB":
                return value / 1024

            case "GB":
                return value

    else:
        raise ValueError("Invalid format.") 

def percent_of(part, total):
    return round(part / total * 100, 2)

def sum_size(models):
    return round(sum(map(lambda model: gb_size(model["size"]),models)), 2)

def divide_list(list, size=5):
    return [list[i:i + size] for i in range(0, len(list), size)]


def foreach(iterable: list, fn: lambda item: (item)):
    for item in iterable:
        fn(item)

import shutil

def ollama_installed() -> bool:
    path = shutil.which("ollama")

    if not path:
        return False

    try:
        subprocess.run(
            ["ollama", "--version"],
            capture_output=True,
            check=True
        )

        return True
    except:
        return False