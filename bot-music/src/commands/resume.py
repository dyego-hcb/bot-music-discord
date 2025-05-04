# src/commands/resume.py
import discord
from discord import app_commands

async def resume_command(interaction: discord.Interaction):
    await interaction.response.defer()

    if interaction.user.voice is None or interaction.guild.voice_client is None:
        await interaction.followup.send("You must be connected to a voice channel and the bot must be paused.")
        return

    vc: discord.VoiceClient = interaction.guild.voice_client

    if vc.is_paused():
        vc.resume()
        await interaction.followup.send("Music has been resumed.")
    else:
        await interaction.followup.send("There's no paused music to resume.")

async def setup(bot: discord.Client):
    @app_commands.command(
        name="resume",
        description="Resumes the currently paused music playback, allowing you to continue enjoying your playlist."
    )
    async def resume(interaction: discord.Interaction):
        await resume_command(interaction)

    bot.tree.add_command(resume)
