# src/commands/pause.py
import discord
from discord import app_commands

async def pause_command(interaction: discord.Interaction):
    await interaction.response.defer()

    if interaction.user.voice is None or interaction.guild.voice_client is None:
        await interaction.followup.send("You must be connected to a voice channel and the bot must be playing music.")
        return

    vc: discord.VoiceClient = interaction.guild.voice_client

    if vc.is_playing():
        vc.pause()
        await interaction.followup.send("Music has been paused.")
    else:
        await interaction.followup.send("There's no music playing right now.")

async def setup(bot: discord.Client):
    @app_commands.command(
        name="pause",
        description="Pauses the currently playing song, allowing you to resume playback later."
    )
    async def pause(interaction: discord.Interaction):
        await pause_command(interaction)

    bot.tree.add_command(pause)
