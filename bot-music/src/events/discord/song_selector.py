# src/events/discord/song_selector.py
import discord
from config import config 
from commands.play import play_command

class SongSelectView(discord.ui.View):
    def __init__(self, videos, timeout=60):
        super().__init__(timeout=timeout)
        self.selected_url = None
        self._interaction = None
        self.music_emoji = config["emojis"]["music"]

        for idx, video in enumerate(videos, start=1): 
            title = video['title']
            url = video['link']
            label = f"{idx}. {title}"
            if len(label) > 80:
                label = label[:77] + "..."
            
            button = discord.ui.Button(
                label=label,
                style=discord.ButtonStyle.secondary,
                emoji=self.music_emoji,  
                custom_id=f"song_{idx}"  
            )

            button.callback = self._create_callback(url)
            self.add_item(button)

    def _create_callback(self, url):
        async def callback(interaction: discord.Interaction):
            self.selected_url = url
            self._interaction = interaction
            await play_command(self._interaction, url)
            self.stop() 
        return callback
