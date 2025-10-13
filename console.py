from rich.console import Console
from rich.text import Text
from rich.bar import Bar

console = Console()

def update_models(models: list, current, downloaded: list, chunk_size, total_size, downloaded_size):
    chunk_size = Text(text=f"{chunk_size}GB", style="blue bold")
    size_sep = Text(text="of", style="bold")
    total_size = Text(text=f"{total_size}GB", style="blue bold")

    console.print("Chunk total size:", chunk_size, size_sep, total_size)
    console.print("")

    counter = 1
    for model in models:
        model_row = [
            Text(text=f"{counter}.", style=""), 
            Text(text=model["name"], style="bold"), 
            Text(text=model["size"], style="bold blue")
            ]
        
        if current["name"] == model["name"]:
            model_row.append(Text(text="|-> Downloading...", style="italic"))
        elif downloaded.__contains__(model["name"]):
            model_row.append(Text(text="(Completed!)", style="blue bold"))

        console.print(*model_row)
        counter += 1

    console.print("")
    console.print(Text("| Downloaded: "), Text(f"{round(downloaded_size, 2)}GB", style="bold blue"), Text("|"))