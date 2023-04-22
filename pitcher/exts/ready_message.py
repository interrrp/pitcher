from disnake.ext.commands.cog import Cog

from ..bot import PitcherBot


class ReadyMessage(Cog):
    """A cog that prints a fancy message to the terminal when the bot is ready."""

    def __init__(self, bot: PitcherBot) -> None:
        """Initialize the bot.

        Args:
            bot: The bot instance.
        """

        self.bot = bot

    @Cog.listener()
    async def on_ready(self) -> None:
        """Called when the bot is ready. Print a fancy message to the terminal."""

        console = self.bot.console

        console.clear()
        console.print(
            f"""
 [green]🤖 Pitcher is ready![/green]
  | [gray]Running as[/gray] [i]{self.bot.user}[/i]
  | [gray]on[/gray] [i]{len(self.bot.guilds)}[/i] servers
  | [gray]with[/gray] [i]{len(self.bot.slash_commands)}[/i] commands   
"""
        )


def setup(bot: PitcherBot) -> None:
    """Load the `ReadyMessage` cog.

    Args:
        bot: The bot instance.
    """

    bot.add_cog(ReadyMessage(bot))
