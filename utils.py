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

def total_size(models):
    return round(sum(map(lambda model: gb_size(model["size"]),models)), 2)

def join(list: list, sep):
    result = ""

    for item in list:
        result += f"{item}{sep}"
    
    return result

def flatten(biglist: list):
    list = []

    for item in biglist:
        for subitem in item:
            list.append(subitem)
    return list