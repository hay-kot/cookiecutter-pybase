from pathlib import Path

from pydantic import BaseModel

{% if cookiecutter.use_rich|lower == 'y' %}
from rich import traceback
traceback.install()
{%- endif %}

APP_VERSION = "{{ cookiecutter.version }}"
CWD = Path(__file__).parent

class AppSettings(BaseModel):
    """A Base settings class that you can use to establish
    a base set of 'global' variables that can easily be imported
    across your application

    Args:
        BaseModel ([type]): [description]
    """

    # Helpful Paths
    BASE_DIR: Path = CWD.parent
    HOME_DIR: Path = Path.home()

    # Global Verbose for CLIs
    verbose: bool = False

    # Maybe useful?
    version: str = APP_VERSION


settings = AppSettings()