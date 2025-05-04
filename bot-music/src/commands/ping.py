# src/commands/ping.py
import discord
from discord import app_commands


async def ping_command(interaction: discord.Interaction, client: discord.Client):
    await interaction.response.defer()

    latency = client.latency * 1000
    
    await interaction.followup.send(f"Pong! API Latency is `{latency:.2f}ms 🛰️`")

async def setup(bot: discord.Client):
    @app_commands.command(name="ping", description="Get the ping of the bot.")
    async def ping(interaction: discord.Interaction):
        await ping_command(interaction, bot)

    bot.tree.add_command(ping)
