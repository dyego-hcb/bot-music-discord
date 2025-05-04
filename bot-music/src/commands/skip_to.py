# src/commands/skip_to.py
# src/commands/skip_to.py
import discord
from discord import app_commands
from events.player import music_state
import asyncio
from discord.ui import View, Button


class MusicButton(Button):
    def __init__(self, index: int, title: str):
        super().__init__(label=title[:80], style=discord.ButtonStyle.primary, row=index % 5)
        self.index = index

    async def callback(self, interaction: discord.Interaction):
        vc: discord.VoiceClient = interaction.guild.voice_client
        if not vc or not vc.is_connected():
            await interaction.response.send_message("Bot is not connected to a voice channel.", ephemeral=True)
            return

        skipped = music_state.queue[:self.index]
        music_state.queue = music_state.queue[self.index:]

        if music_state.loop_enabled:
            music_state.queue.extend(skipped)

        if vc.is_playing():
            vc.stop()

        await interaction.response.send_message(f"⏭️ Skipped to **{self.label}**", ephemeral=True)


class MusicQueueView(View):
    def __init__(self):
        super().__init__(timeout=60) 
        for i, (_, title, _) in enumerate(music_state.queue):
            self.add_item(MusicButton(i, title))


async def skip_to_command(interaction: discord.Interaction):
    await interaction.response.defer()

    if interaction.user.voice is None:
        await interaction.followup.send("You must be connected to a voice channel first.")
        return

    if not music_state.queue:
        await interaction.followup.send("The queue is empty.")
        return

    view = MusicQueueView()

    await interaction.followup.send(
        "🎵 Choose a song to skip to:",
        view=view,
        ephemeral=True 
    )


async def setup(bot: discord.Client):
    @app_commands.command(
        name="skip_to",
        description="Skips to a specific song in the playlist via buttons."
    )
    async def skip_to(interaction: discord.Interaction):
        await skip_to_command(interaction)

    bot.tree.add_command(skip_to)
