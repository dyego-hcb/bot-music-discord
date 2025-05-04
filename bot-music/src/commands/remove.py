# src/commands/remove.py
import discord
from discord import app_commands


async def remove_command(interaction: discord.Interaction):
    await interaction.response.defer()
    
    if interaction.user.voice is None:
        await interaction.response.send_message("You must be connected to a voice channel first.")
        return
    
    await interaction.followup.send("Command Removed")

async def setup(bot: discord.Client):
    @app_commands.command(name="remove", description="Removes a specified song from the current music queue, allowing you to manage your playlist.")
    async def remove(interaction: discord.Interaction):
        await remove_command(interaction)

    bot.tree.add_command(remove)

