from pydantic import BaseSettings


class Settings(BaseSettings):
    """The settings for the bot.

    Attributes:
        bot_token: The bot token to use for the bot.
    """

    bot_token: str

    class Config:
        """Inner class for configuring where Pydantic loads settings.

        Attributes:
            env_file: The file to load environment variables from. Defaults to `.env`.
            env_file_encoding: The encoding of the environment file. Defaults to UTF-8.
            fields: The fields to load from the environment file. Defaults to every field's name in screaming snake case
                (`bot_token` to `BOT_TOKEN`, etc.).
        """

        env_file = ".env"
        env_file_encoding = "utf-8"

        fields = {
            "bot_token": {"env": "BOT_TOKEN"},
        }
