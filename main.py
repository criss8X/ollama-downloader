import json
from console import update_models
import time
from subprocess import run
import utils as utils

def download_chunk(models, chunk_size, total_size, downloaded_size):
    run("clear")
    
    downloaded = []
    for model in models:
        update_models(models, model, downloaded, chunk_size, total_size, downloaded_size)
        time.sleep(1)

        downloaded.append(model["name"])
        run("clear")


def divide_list(list, size=5):
    return [list[i:i + size] for i in range(0, len(list), size)]


def main():
    with open("ollama-data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        models = data["models"]
        chunks = divide_list(models)

        downloaded_size = 0.00
        total_size = utils.total_size(models)

        for chunk in chunks:
            chunk_size = utils.total_size(chunk)
            download_chunk(chunk, chunk_size, total_size, downloaded_size)

            downloaded_size += chunk_size


if __name__ == "__main__":
    main()
