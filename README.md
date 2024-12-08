**DarkMonster**
***A Dark Web Scrapping Telegram Bot***

A Telegram bot that searches .onion websites using Tor-based search engines (Ahmia, DuckDuckGo, and Torch) and provides results to users in a secure and simple way.

* Features
   Search .onion links from multiple sources via Tor.
   Combine, deduplicate, and save results into a file for download.
   Easy setup with secure bot token storage.
   Runs via Telegram commands.

* Prerequisites
   Python 3.10 or higher: Ensure Python is installed.
   Tor: Install and ensure the Tor service is running.

For Linux/Ubuntu:

    sudo apt install tor
    sudo service tor start

For macOS:

    brew install tor
    brew services start tor

For Windows
    download and install the Tor Browser.


Telegram Bot:

    Create a bot on Telegram via BotFather.
    Copy the bot token provided.


  

***Installation***

  Clone the Repository:

    git clone https://github.com/your-repo/dark-web-bot.git
    cd dark-web-bot

Install Dependencies: Use the provided requirements.txt file to install required libraries.

     pip install -r requirements.txt

Save Your Bot Token:

  Create a file named token.exe in the project directory.
  Paste your bot token into this file and save it.

Run the Bot: Start the bot using:

     python3 bot.py


Usage

 Start the Bot: Open your Telegram app and send /start to your bot to see the welcome message.
 Search for Onion Links: Use the /search <query> command to search .onion links. For example:

     /search leaked database

Receive Results: The bot will reply with a text file containing the results or notify you if no results are found.
