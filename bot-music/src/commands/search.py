# src/commands/search.py
import discord
from discord import app_commands
from youtubesearchpython import VideosSearch  
from events.discord.song_selector import SongSelectView 


async def search_command(interaction: discord.Interaction, query: str):
    await interaction.response.defer()

    if interaction.user.voice is None:
        await interaction.response.send_message("You must be connected to a voice channel first.")
        return

    video_search = VideosSearch(query, limit=10)
    
    results = video_search.result()

    if not isinstance(results, dict):
        await interaction.followup.send("Failed to retrieve results.")
        return
    
    videos = results.get("result")

    if not videos:
        await interaction.followup.send("No results found.")
        return
    
    view = SongSelectView(videos)
    await interaction.followup.send("Here are the top 10 results. Click a button to choose:", view=view)


async def setup(bot: discord.Client):
    @app_commands.command(name="search", description="Searches for songs or playlists from YouTube.")
    @app_commands.describe(query="The search term to find songs or videos on YouTube.")
    async def search(interaction: discord.Interaction, query: str):
        await search_command(interaction, query)

    bot.tree.add_command(search)
