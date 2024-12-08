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

    git clone https://github.com/mahhesshh/DarkMonster.git
    cd dark-web-bot

Install Dependencies: Use the provided requirements.txt file to install required libraries.

     pip install -r requirements.txt

Save Your Bot Token:

  Create a file named token.exe in the project directory.
  Paste your bot token into this file and save it.

Run the Bot: Start the bot using:

     python3 main.py


Usage

 Start the Bot: Open your Telegram app and send /start to your bot to see the welcome message.
 Search for Onion Links: Use the /search <query> command to search .onion links. For example:

     /search leaked database

Receive Results: The bot will reply with a text file containing the results or notify you if no results are found.


**Advisory**

This tool is intended strictly for educational purposes and to demonstrate the use of Python with the Telegram Bot API and Tor network. Users are advised to:

   1.Comply with all applicable laws: Accessing .onion sites or performing searches on the dark web may be illegal in your jurisdiction. Ensure you fully understand and comply with local regulations before using this tool.

   2.Avoid malicious activity: This bot is not intended for accessing illegal or unethical content. Do not use this tool to engage in activities that violate privacy, laws, or ethical principles.

   3.Use responsibly: The developers of this tool do not endorse or condone misuse of the dark web. Misuse of this tool is solely the responsibility of the user.

   4.Educational only: This tool is designed as a demonstration of how to integrate Python, Telegram bots, and Tor networking. Use it as a learning resource.

**Disclaimer:** The authors are not responsible for any legal or ethical consequences resulting from the use or misuse of this tool. Use at your own risk.
