from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.style import Style

def init_welcome():
    console = Console()
    
    title = Text("Ollama Downloader", style="bold white on magenta")
    
    # Thank you message content
    message = Text.from_markup(
        "Quiero agradecerte de corazón [bold magenta]Claudia[/bold magenta] por la gran ayuda y apoyo hacia mí 👾, "
        "a pesar de que tienes bastante trabajo arriba. Eres increíble [bold magenta]♥[/bold magenta]\n\n"
        "[bold magenta]Ahora sí, vamo a intalar eso ->[/bold magenta]"
    )
    
    welcome_panel = Panel(
        message,
        title=title,
        title_align="center",
        border_style=Style(color="magenta", bold=True),
        padding=(1, 4),
        subtitle="[bold magenta]Presiona Enter para continuar[/bold magenta]",
        subtitle_align="right"
    )
    
    console.print("\n")
    console.print(welcome_panel)
    console.print("\n")
    
    input()

