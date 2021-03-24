import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def hello(name: str = "No Name Provided"):
    typer.echo(f"Hello, {name}")
