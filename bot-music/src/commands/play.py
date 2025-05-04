# src/commands/play.py
import discord
import asyncio
from discord import app_commands
from yt_dlp import YoutubeDL
from events.player import music_state 

def get_audio_source(url: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'extract_flat': 'in_playlist',
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info['url'], info.get('title', 'Unknown Title'), info["thumbnails"][len(info["thumbnails"]) - 5]['url']

async def play_next(interaction: discord.Interaction, vc: discord.VoiceClient):
    if len(music_state.queue) > 0:
        url, title, thumbnail = music_state.queue.pop(0)

        if music_state.loop_enabled:
            music_state.queue.append((url, title, thumbnail))
        
        if vc.is_playing():
            vc.stop()

        vc.play(discord.FFmpegPCMAudio(url), after=lambda e: asyncio.run(play_next(vc)))
    else:
        print("Queue is empty, stopping.")
        await vc.disconnect() 

async def play_command(interaction: discord.Interaction, link: str):
    global music_state
        
    await interaction.response.defer()

    if interaction.user.voice is None:
        await interaction.followup.send("You must be connected to a voice channel first.")
        return

    voice_channel = interaction.user.voice.channel

    if interaction.guild.voice_client is None:
        try:
            await voice_channel.connect()
            await interaction.followup.send(f"Connected to {voice_channel.name}.")
        except Exception as e:
            await interaction.followup.send(f"Failed to connect to {voice_channel.name}: {e}")
            return

    vc: discord.VoiceClient = interaction.guild.voice_client

    if vc.is_playing():
        await interaction.followup.send("Music is already playing. Adding to queue.")
        stream_url, title, thumbnail = get_audio_source(link)
        music_state.queue.append((stream_url, title, thumbnail))

        embed = discord.Embed(
            title=title,
            description=f"[Click here to open the video]({link})",
            color=discord.Color.orange()
        )
        embed.set_footer(text="Added to queue")
        embed.set_image(url=thumbnail)

        await interaction.followup.send(embed=embed)
        return

    try:
        stream_url, title, thumbnail = get_audio_source(link)
        vc.play(discord.FFmpegPCMAudio(stream_url), after=lambda e: asyncio.run(play_next(interaction, vc)))

        embed = discord.Embed(
            title=title,
            description=f"[Click here to open the video]({link})",
            color=discord.Color.green()
        )
        embed.set_footer(text="Now playing")
        embed.set_image(url=thumbnail)

        await interaction.followup.send(embed=embed)

        music_state.current_song = (stream_url, title, thumbnail)

    except Exception as e:
        await interaction.followup.send(f"Failed to play audio: {e}")

async def setup(bot: discord.Client):
    @app_commands.command(name="play", description="Play a song from a YouTube link or other source.")
    @app_commands.describe(link="The URL of the song you want to play.")
    async def play(interaction: discord.Interaction, link: str):
        await play_command(interaction, link)

    bot.tree.add_command(play)
