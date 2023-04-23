from os import remove
from contextlib import suppress

from moviepy.editor import AudioFileClip
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from pydub import AudioSegment
from disnake import File
from disnake.interactions import ApplicationCommandInteraction
from disnake.ext.commands import slash_command, InteractionBot
from disnake.ext.commands.cog import Cog


class Pitcher(Cog):
    """Cog that provides functionality for pitching stuff."""

    @slash_command(description="Pitch a video's audio by a factor.")
    async def pitch(
        self, inter: ApplicationCommandInteraction, video_link: str, pitch_factor: float
    ) -> None:
        """Pitch a video.

        Args:
            inter: The interaction that invoked this command.
            video_link: The link to the video to pitch.
            pitch_factor: The factor to pitch the video by (e.g. 0.5 for half speed, 2 for double speed).
        """

        await inter.response.defer(ephemeral=True)

        if pitch_factor < 0.1 or pitch_factor > 5:
            await inter.followup.send("Pitch factor must be between 0.1 and 5.")
            return

        try:
            audio_path = await Pitcher.download_audio(video_link)
        except RegexMatchError:
            await inter.followup.send("Invalid video link.")
            return

        pitched_path = await Pitcher.pitch_audio(audio_path, pitch_factor)

        await inter.followup.send(file=File(pitched_path))

        with suppress(FileNotFoundError):
            remove(audio_path)
            remove(pitched_path)

    @staticmethod
    async def download_audio(link: str) -> str:
        """Download a YouTube video's audio from a link.

        Args:
            link: The link to the video to download.
            path: The path to save the audio to.

        Returns:
            The path to the downloaded audio.
        """

        audio_video_path = (
            YouTube(link).streams.filter(only_audio=True).first().download()
        )

        if not audio_video_path.endswith(".mp3"):
            path = await Pitcher.audio_only_video_to_mp3(
                audio_video_path, audio_video_path[:-4] + ".mp3"
            )

        remove(audio_video_path)

        return path

    @staticmethod
    async def audio_only_video_to_mp3(path: str, output_path: str) -> str:
        """Convert an audio-only video to an MP3.

        Args:
            path: The path to the video to convert.
            output_path: The path to save the MP3 to.

        Returns:
            The path to the converted MP3.
        """

        clip = AudioFileClip(path)
        clip.write_audiofile(output_path, verbose=False, logger=None)

        return output_path

    @staticmethod
    async def pitch_audio(path: str, factor: float) -> str:
        """Pitch an audio file.

        Args:
            path: The path to the audio file to pitch.
            factor: The factor to pitch the audio by.

        Returns:
            The path to the pitched audio file.
        """

        if not path.endswith(".mp3"):
            raise ValueError("Audio file must be an MP3.")

        audio = AudioSegment.from_mp3(path)
        audio = audio._spawn(
            audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * factor)}
        )

        audio.export(path, format="mp3")

        return path


def setup(bot: InteractionBot) -> None:
    """Load the Pitcher cog."""
    bot.add_cog(Pitcher())
