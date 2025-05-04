# src/commands/shuffle.py
import discord
import random
from discord import app_commands
from events.player import music_state  # Importa o estado global da música

async def shuffle_command(interaction: discord.Interaction):
    await interaction.response.defer()

    if interaction.user.voice is None:
        await interaction.response.send_message("You must be connected to a voice channel first.")
        return

    if not music_state.queue:
        await interaction.followup.send("The queue is currently empty, nothing to shuffle.")
        return

    random.shuffle(music_state.queue)

    await interaction.followup.send("The queue has been shuffled! 🎶")

async def setup(bot: discord.Client):
    @app_commands.command(
        name="shuffle",
        description="Randomizes the order of songs in the current playlist, providing a fresh listening experience."
    )
    async def shuffle(interaction: discord.Interaction):
        await shuffle_command(interaction)

    bot.tree.add_command(shuffle)
