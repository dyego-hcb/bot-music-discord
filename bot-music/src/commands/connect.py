# src/commands/connect.py
import discord
from discord import app_commands

async def connect_command(interaction: discord.Interaction):
    await interaction.response.defer()
    
    if interaction.user.voice is None:
        await interaction.followup.send("You must be connected to a voice channel first.")
        return

    channel = interaction.user.voice.channel
    try:
        await channel.connect()
        await interaction.followup.send(f"Connected to {channel.name}.")
    except Exception as e:
        await interaction.followup.send(f"Failed to connect to {channel.name}: {e}")

async def setup(bot: discord.Client):
    @app_commands.command(name="connect", description="Make the bot join your voice channel.")
    async def connect(interaction: discord.Interaction):
        await connect_command(interaction)

    bot.tree.add_command(connect)

