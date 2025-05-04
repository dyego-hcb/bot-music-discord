# src/main.py
import discord
from discord.ext import commands
from config import config
import os

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True


class MyBotMusic(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)
        self.synced = False

    def get_message(self, en_message, pt_message):
        return pt_message if config["app"]["lang"] == "pt" else en_message

    async def setup_hook(self):
        all_load = True
        commands_dir = "commands"
        for filename in os.listdir(commands_dir):
            if filename.endswith(".py"):
                command_name = filename[:-3]
                try:
                    await self.load_extension(f"commands.{command_name}")
                    print(
                        self.get_message(
                            f"Command {command_name} loaded successfully.",
                            f"Comando {command_name} carregado com sucesso.",
                        )
                    )
                except Exception as e:
                    all_load = False
                    print(
                        self.get_message(
                            f"Failed to load command {command_name}: {e}",
                            f"Falha ao carregar comando {command_name}: {e}",
                        )
                    )
        if all_load:
            print("All Commands Have Been Loaded !!")
        else:
            print("Some Commands Have Not Been Loaded !!")

    async def on_ready(self):
        if not self.synced:
            print(f"Attempting to sync commands globally...")
            await self.tree.sync()
            print("Global commands synchronized successfully.")
            self.synced = True
            print(
                self.get_message(
                    f"Commands synchronized globally.",
                    f"Comandos sincronizados globalmente.",
                )
            )

        print(
            self.get_message(
                f"Bot connected as {self.user}.", f"Bot conectado como {self.user}."
            )
        )
        await self.change_presence(activity=discord.Game(name=config["app"]["playing"]))


bot = MyBotMusic()

if __name__ == "__main__":
    bot.run(config["app"]["token"])
