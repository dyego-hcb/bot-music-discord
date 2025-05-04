# src/commands/back.py

import asyncio
import discord
from discord import app_commands
from commands.play import play_next
from events.player import music_state

async def back_command(interaction: discord.Interaction):
    await interaction.response.defer()

    if interaction.user.voice is None:
        await interaction.response.send_message("You must be connected to a voice channel first.")
        return

    if not music_state.loop_enabled:
        await interaction.followup.send("Loop is not enabled. You cannot go back.")
        return

    if len(music_state.queue) < 1:
        await interaction.followup.send("There is not enough music in the queue to go back.")
        return

    vc: discord.VoiceClient = interaction.guild.voice_client

    last_song = music_state.queue.pop(-1)
    music_state.queue.insert(1, last_song)
    music_state.current_song = last_song

    await interaction.followup.send("Rewinding to the previous song in the loop.")

    vc.stop()  

    await play_next(interaction, vc)


async def setup(bot: discord.Client):
    @app_commands.command(name="back", description="Rewinds the currently playing song or skips back to the previous track in the playlist.")
    async def back(interaction: discord.Interaction):
        await back_command(interaction)

    bot.tree.add_command(back)
