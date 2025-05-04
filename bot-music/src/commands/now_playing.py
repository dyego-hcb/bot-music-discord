# src/commands/now_playing.py
import discord
from discord import app_commands
from events.player import music_state

async def now_playing_command(interaction: discord.Interaction):
    if not interaction.response.is_done():
        await interaction.response.defer()

    if interaction.user.voice is None:
        await interaction.response.send_message("You must be connected to a voice channel first.")
        return

    if music_state.current_song is None:
        await interaction.followup.send("No music is currently playing.")
        return

    stream_url, title, thumbnail = music_state.current_song  

    embed = discord.Embed(
        title=title,
        description=f"[Click here to open the video]({stream_url})",
        color=discord.Color.green()
    )
    embed.set_footer(text="Currently playing song")
    embed.set_image(url=thumbnail)

    await interaction.followup.send(embed=embed)


async def setup(bot: discord.Client):
    @app_commands.command(name="now_playing", description="Displays the currently playing song and its details, including title and artist.")
    async def now_playing(interaction: discord.Interaction):
        await now_playing_command(interaction)

    bot.tree.add_command(now_playing)

