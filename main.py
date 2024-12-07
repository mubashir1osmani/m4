import typer

from rich.console import Console

app = typer.Typer()
console = Console()

@app.command()
def start():
	"""welcome to crossover, this is the future of chip design"""

	console.print("[bold/cyan]welcome to crossover, this is the future of chip design[bold/cyan]")

	console.print("what do you want to make today?")

	while True:
		prompt = typer.prompt("enter your module description")

		if prompt.lower() == "exit":
			console.print("bye")
			break

		console.print(f"[bold yellow]Processing your request: {prompt}...[/bold yellow]")
		console.print("[italic]Verilog code generation is coming soon!")

if __name__ == "__main__":
	app()