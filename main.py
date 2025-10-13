import json
import subprocess
from utils import sum_size, foreach, divide_list, gb_size, percent_of, ollama_installed, _run_cmd
from rich.text import Text
from rich.console import Console
from welcome import init_welcome

class Downloader:
    def __init__(self, models):
        self.models = models
        self.total_size = sum_size(models)
        self.downloaded = []
        self.downloaded_size = 0.00
        self.console = Console()

    def init_download(self):
        chunks = divide_list(self.models)
        foreach(chunks, self.download_chunk)

    def clear_console(self):
        subprocess.run("clear")

    def complete_download(self, model):
        self.downloaded.append(model["name"])
        self.downloaded_size += gb_size(model["size"])

    def download_chunk(self, chunk):
        self.clear_console()

        for model in chunk:
            self.update(model=model, chunk=chunk)
            _run_cmd(["ollama", "pull", model["name"]])

            self.complete_download(model)
            self.clear_console()

    def print(self, objects):
        self.console.print(*objects)

    def update(self, model, chunk):
        # Print header with info about size.
        chunk_size = Text(text=f"{round(self.downloaded_size, 2)}GB", style="blue")
        size_sep = Text(text="of", style="bold")
        total_size = Text(text=f"{self.total_size}GB", style="blue")

        percent = Text(text=f"({percent_of(self.downloaded_size, self.total_size)}%)", style="blue bold")

        self.print(["Downloaded size:", chunk_size, size_sep, total_size, percent])
        self.print("")

        foreach(chunk, lambda model_of_chunk: self.update_model_of_chunk(model_of_chunk, model))

    
    def update_model_of_chunk(self, model_of_chunk, current_model):
        model_row = [
            Text(text=f"·", style=""), 
            Text(text=model_of_chunk["name"], style="bold"), 
            Text(text=model_of_chunk["size"], style="bold blue")
        ]
        
        if current_model["name"] == model_of_chunk["name"]:
            model_row.append(Text(text="|-> Downloading...", style="italic"))
        elif self.downloaded.__contains__(model_of_chunk["name"]):
            model_row.append(Text(text="(Completed!)", style="blue bold"))

        self.print(model_row)


def main():
    with open("ollama-data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        models = data["models"]
       
        Downloader(models).init_download()


if __name__ == "__main__":
    installed = ollama_installed()

    if not installed:
        print("Please, install ollama before run this script.")
    else:
        init_welcome()
        main()
