# DJ Music Bot

## Descrição

DJ Music Bot é um bot do Discord desenvolvido para facilitar o controle de reprodução de músicas em servidores. Ele permite que os usuários toquem, pausem, pulem músicas e muito mais, diretamente de seus canais de voz no Discord.

## Funcionalidades

Este bot possui os seguintes comandos:

- **`/ping`**: Retorna a latência atual do bot.
- **`/connect`**: Faz o bot entrar no canal de voz em que o usuário está.
- **`/play`**: Começa a tocar uma música a partir de um link fornecido.
- **`/pause`**: Pausa a música que está sendo reproduzida.
- **`/resume`**: Retoma a música pausada.
- **`/skip`**: Pula a música que está sendo tocada.
- **`/clear`**: Limpa a fila de músicas.
- **`/loop`**: Alterna o repetição da música atual.
- **`/shuffle`**: Embaralha a fila de músicas.
- **`/now_playing`**: Exibe a música que está tocando no momento.
- **`/queue`**: Exibe a lista de músicas na fila.
- **`/remove`**: Remove uma música específica da fila.
- **`/search`**: Pesquisa por uma música com base em um termo fornecido.
- **`/back`**: Volta para a música anterior na fila.
- **`/skip_to`**: Pula para uma música específica na fila.

## Como Usar

### Pré-requisitos

1. Python 3.8 ou superior.
2. Biblioteca `discord.py`.
3. Conta no Discord e um servidor onde você possa adicionar o bot.

### Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/SEU_USUARIO/DJ-Music-Bot.git
   cd DJ-Music-Bot
   ```

2. Crie e ative o ambiente virtual:

   - **Linux/macOS**:

     ```bash
     python3 -m venv bot_musica
     source bot_musica/bin/activate
     ```

   - **Windows**:
     ```powershell
     python -m venv bot_musica
     .\bot_musica\Scripts\activate
     ```

3. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure o bot no Discord:

   - Crie um aplicativo no [Discord Developer Portal](https://discord.com/developers/applications).
   - Obtenha o token do bot e adicione-o no arquivo `config.json`.

   Exemplo de `config.json`:

   ```json
   {
     "token": "SEU_TOKEN_DO_BOT",
     "prefix": "!"
   }
   ```

5. Execute o bot:

   ```bash
   python main.py
   ```

### Comandos

O bot possui uma série de comandos que podem ser usados pelos administradores do servidor ou membros com permissões para interagir com o bot.

- **`/help`**: Exibe todos os comandos disponíveis e suas descrições.

### Contribuindo

1. Faça um fork deste repositório.
2. Crie uma nova branch para suas alterações (`git checkout -b minha-alteracao`).
3. Faça suas alterações e commit (`git commit -am 'Adiciona nova funcionalidade'`).
4. Faça um push para a branch (`git push origin minha-alteracao`).
5. Abra um Pull Request para revisar suas alterações.

### Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Nota**: Caso algum comando não funcione como esperado, verifique se as dependências estão corretamente instaladas e se o bot tem as permissões necessárias no servidor do Discord.

---

# DJ Music Bot

## Description

DJ Music Bot is a Discord bot developed to facilitate music playback control in servers. It allows users to play, pause, skip songs, and much more directly in their voice channels on Discord.

## Features

This bot includes the following commands:

- **`/ping`**: Returns the current latency of the bot.
- **`/connect`**: Makes the bot join the voice channel the user is in.
- **`/play`**: Starts playing a song from a provided link.
- **`/pause`**: Pauses the currently playing song.
- **`/resume`**: Resumes the paused song.
- **`/skip`**: Skips the current song.
- **`/clear`**: Clears the song queue.
- **`/loop`**: Toggles repeat of the current song.
- **`/shuffle`**: Shuffles the song queue.
- **`/now_playing`**: Displays the current playing song.
- **`/queue`**: Displays the list of songs in the queue.
- **`/remove`**: Removes a specific song from the queue.
- **`/search`**: Searches for a song based on a given term.
- **`/back`**: Goes back to the previous song in the queue.
- **`/skip_to`**: Skips to a specific song in the queue.

## How to Use

### Prerequisites

1. Python 3.8 or higher.
2. The `discord.py` library.
3. A Discord account and a server where you can add the bot.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/DJ-Music-Bot.git
   cd DJ-Music-Bot
   ```

2. Create and activate the virtual environment:

   - **Linux/macOS**:

     ```bash
     python3 -m venv bot_musica
     source bot_musica/bin/activate
     ```

   - **Windows**:
     ```powershell
     python -m venv bot_musica
     .\bot_musica\Scripts\activate
     ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the bot on Discord:

   - Create an application on the [Discord Developer Portal](https://discord.com/developers/applications).
   - Obtain the bot token and add it to the `config.json` file.

   Example `config.json`:

   ```json
   {
     "token": "YOUR_BOT_TOKEN",
     "prefix": "!"
   }
   ```

5. Run the bot:

   ```bash
   python main.py
   ```

### Commands

The bot includes a variety of commands that can be used by server administrators or members with appropriate permissions to interact with the bot.

- **`/help`**: Displays all available commands and their descriptions.

### Contributing

1. Fork this repository.
2. Create a new branch for your changes (`git checkout -b my-change`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin my-change`).
5. Open a Pull Request to review your changes.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.

---

**Note**: If any command doesn't work as expected, check if the dependencies are correctly installed and ensure that the bot has the necessary permissions in the Discord server.

---
