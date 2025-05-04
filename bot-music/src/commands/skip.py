# src/commands/skip.py
import asyncio
import discord
from discord import app_commands
from commands.play import play_next
from events.player import music_state  

async def skip_command(interaction: discord.Interaction):
    if interaction.user.voice is None:
        await interaction.response.send_message("You must be connected to a voice channel first.")
        return

    vc: discord.VoiceClient = interaction.guild.voice_client

    if vc is None or not vc.is_playing():
        await interaction.response.send_message("No music is currently playing.")
        return

    if len(music_state.queue) > 0:
        await interaction.response.send_message("Skipped to next song.")
        vc.stop()

        url, title, thumbnail = music_state.queue[0]
        embed = discord.Embed(
            title=title,
            description=f"[Click here to open the video]({url})",
            color=discord.Color.green()
        )
        embed.set_footer(text="Now playing")
        embed.set_image(url=thumbnail)

        await interaction.followup.send(embed=embed)
    else:
        await interaction.followup.send("Queue is empty, no music to skip to.")

async def setup(bot: discord.Client):
    bot.tree.add_command(
        app_commands.Command(
            name="skip",
            description="Skips the currently playing song, allowing you to move to the next track in the playlist.",
            callback=skip_command,
        )
    )
