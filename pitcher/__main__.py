import asyncio

from pitcher.bot import PitcherBot


async def async_main() -> None:
    """Asynchronous entry point for the bot."""

    bot = PitcherBot()

    await bot.start(bot.settings.bot_token)


def main() -> None:
    """Synchronous wrapper for the asynchronous entry point.

    This is needed because `asyncio.run` cannot be called from a Poetry script, so we need to call it from a function.
    """

    asyncio.run(async_main())


if __name__ == "__main__":
    main()
