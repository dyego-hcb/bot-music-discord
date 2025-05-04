# src/commands/loop.py
import discord
from discord import app_commands
from events.player import music_state

async def loop_command(interaction: discord.Interaction):
    await interaction.response.defer()

    if interaction.user.voice is None:
        await interaction.followup.send("You must be connected to a voice channel first.")
        return

    music_state.loop_enabled = not music_state.loop_enabled

    if music_state.loop_enabled:
        await interaction.followup.send("🔁 Loop **activated**. Songs will repeat.")
    else:
        await interaction.followup.send("⏹️ Loop **deactivated**. Songs will not repeat.")

async def setup(bot: discord.Client):
    @app_commands.command(
        name="loop",
        description="Toggles music loop mode: when active, the current queue loops forever."
    )
    async def loop(interaction: discord.Interaction):
        await loop_command(interaction)

    bot.tree.add_command(loop)
