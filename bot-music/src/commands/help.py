# src/commands/help.py
import discord
from discord import app_commands

command_descriptions = {
    "ping": "Returns the current latency of the bot.",
    "connect": "Make the bot join your voice channel.",
    "play": "Starts playing a song from a link.",
    "pause": "Pauses the currently playing song.",
    "resume": "Resumes the paused song.",
    "skip": "Skips the current song.",
    "clear": "Clears the song queue.",
    "loop": "Toggles the repeat of the current song.",
    "shuffle": "Shuffles the song queue.",
    "now_playing": "Displays the song currently playing.",
    "queue": "Displays the list of songs in the queue.",
    "remove": "Removes a specific song from the queue.",
    "search": "Searches for a song based on a provided term.",
    "back": "Goes back to the previous song in the queue.",
    "skip_to": "Skips to a specific song in the queue.",
}


async def help_command(interaction: discord.Interaction):
    await interaction.response.defer()

    help_message = "Here are the available commands:\n\n"
    for command, description in command_descriptions.items():
        help_message += f"`/{command}`: {description}\n"

    await interaction.followup.send(help_message)

async def setup(bot: discord.Client):
    @app_commands.command(name="help", description="Lists all available commands and their descriptions.")
    async def help(interaction: discord.Interaction):
        await help_command(interaction)

    bot.tree.add_command(help)
