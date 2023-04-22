from rich.console import Console
from disnake.ext.commands import InteractionBot

from .settings import Settings


class PitcherBot(InteractionBot):
    """The bot class that provides all functionality to the bot.

    Attributes:
        settings: The settings for the bot. This is loaded from the `.env` file and the environment.
        console: The Rich console used for logging and the ready message.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the bot and load all extensions."""

        super().__init__(*args, **kwargs)

        self.settings = Settings()
        self.console = Console()

        self.load_extensions("pitcher/exts")
