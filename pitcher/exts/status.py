from disnake import Activity, ActivityType
from disnake.ext.commands import InteractionBot
from disnake.ext.commands.cog import Cog


class StatusCog(Cog):
    """Cog to set the status of the bot."""

    def __init__(self, bot: InteractionBot) -> None:
        """Initialize the bot.

        Args:
            bot: The bot instance.
        """

        self.bot = bot

    @Cog.listener()
    async def on_ready(self) -> None:
        """Called when the bot is ready. Set the status of the bot."""

        await self.bot.change_presence(
            activity=Activity(
                type=ActivityType.watching,
                name=f"{len(self.bot.guilds)} servers",
            )
        )


def setup(bot: InteractionBot) -> None:
    """Load the `StatusCog` cog.

    Args:
        bot: The bot instance.
    """

    bot.add_cog(StatusCog(bot))
