from {{cookiecutter.project_slug}}.core.settings import settings
from {{cookiecutter.project_slug}}.utils.custom_logger import logger
from {{cookiecutter.project_slug}}.commands import hello
import typer





app = typer.Typer()
app.add_typer(hello.app, name="hello")

@app.command()
def demo():
    logger.info(f"Starting 'Name of the project' {settings.version}")
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")

def main():
    app()

if __name__ == "__main__":
    main()

