# src/commands/clear.py
import discord
from discord import app_commands

from events.player import music_state

async def clear_command(interaction: discord.Interaction):
    await interaction.response.defer()

    if interaction.user.voice is None:
        await interaction.response.send_message("You must be connected to a voice channel first.")
        return
    
    vc: discord.VoiceClient = interaction.guild.voice_client
    if vc is not None:
        music_state.queue.clear() 
        music_state.current_song = None
        vc.stop()  
        await vc.disconnect() 
        await interaction.followup.send("Playback stopped and queue cleared.")
    else:
        await interaction.followup.send("No music is currently playing.")

async def setup(bot: discord.Client):
    @app_commands.command(name="clear", description="Clears the current playlist and stops any currently playing music.")
    async def clear(interaction: discord.Interaction):
        await clear_command(interaction)

    bot.tree.add_command(clear)
