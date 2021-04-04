from {{cookiecutter.project_slug}}.core.settings import settings
from {{cookiecutter.project_slug}}.utils.custom_logger import logger

{% if cookiecutter.use_typer_cli|lower == 'y' %}
import typer

app = typer.Typer()

{%- endif %}

{% if cookiecutter.use_typer_cli|lower == 'y' %}
@app.command(){%- endif %}
def main():
    logger.info(f"Starting '{{ cookiecutter.project_name }}' {settings.version}")
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")


if __name__ == "__main__":
    main()
