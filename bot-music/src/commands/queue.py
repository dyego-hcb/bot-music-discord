# src/commands/quee.py
import discord
from discord import app_commands
from events.player import music_state

async def queue_command(interaction: discord.Interaction):
    await interaction.response.defer()

    if interaction.user.voice is None:
        await interaction.response.send_message("You must be connected to a voice channel first.")
        return

    embed = discord.Embed(
        title="Current Queue",
        color=discord.Color.blue()
    )

    if music_state.current_song:
        stream_url, title, thumbnail = music_state.current_song
        embed.add_field(name="🎶 Now Playing", value=f"[{title}]", inline=False)
        embed.set_thumbnail(url=thumbnail)
    else:
        embed.add_field(name="🎶 Now Playing", value="No music is currently playing.", inline=False)

    if hasattr(music_state, "queue") and music_state.queue:
        upcoming_list = ""
        for i, (url, title, _) in enumerate(music_state.queue, start=1):
            upcoming_list += f"{i}. [{title}]\n"

        embed.add_field(name="🎧 Upcoming", value=upcoming_list, inline=False)
    else:
        embed.add_field(name="🎧 Upcoming", value="No songs in the queue.", inline=False)

    await interaction.followup.send(embed=embed)


async def setup(bot: discord.Client):
    @app_commands.command(name="queue", description="Displays the current music queue, showing the list of upcoming songs to be played.")
    async def queue(interaction: discord.Interaction):
        await queue_command(interaction)

    bot.tree.add_command(queue)
