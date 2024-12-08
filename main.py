from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests
import re
import random
import os

# Helper functions for scraping from Ahmia, DuckDuckGo, and Torch

def tor_session():
    """Create a session that routes traffic through Tor."""
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return session

def scrape_ahmia(query):
    """Scrape Ahmia for the given query."""
    query = query.replace(" ", "+")
    url = f"https://ahmia.fi/search/?q={query}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return re.findall(r"\w+\.onion", response.text)
    except Exception as e:
        print(f"Error scraping Ahmia: {e}")
    return []

def scrape_duckduckgo(query):
    """Scrape DuckDuckGo for the given query via Tor."""
    query = query.replace(" ", "+")
    url = f"https://3g2upl4pq6kufc4m.onion/html?q={query}"
    session = tor_session()
    try:
        response = session.get(url)
        if response.status_code == 200:
            return re.findall(r"\w+\.onion", response.text)
    except Exception as e:
        print(f"Error scraping DuckDuckGo: {e}")
    return []

def scrape_torch(query):
    """Scrape Torch for the given query via Tor."""
    query = query.replace(" ", "+")
    url = f"http://xmh57jrzrnw6insl.onion/?q={query}"
    session = tor_session()
    try:
        response = session.get(url)
        if response.status_code == 200:
            return re.findall(r"\w+\.onion", response.text)
    except Exception as e:
        print(f"Error scraping Torch: {e}")
    return []

def save_results(query, results):
    """Save results to a .txt file and return the filename."""
    filename = f"search_results_{query.replace(' ', '_')}_{random.randint(1, 9999)}.txt"
    with open(filename, "w") as file:
        for result in results:
            file.write(result + "\n")
    return filename

# Function to load the bot token securely from a file
def get_bot_token(file_path="token.exe"):
    """Read the bot token from a file."""
    try:
        with open(file_path, "r") as file:
            token = file.read().strip()  # Remove any extra whitespace
            if not token:
                raise ValueError("Token file is empty.")
            return token
    except FileNotFoundError:
        raise FileNotFoundError(f"The token file '{file_path}' does not exist. Please create it and add your bot token.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the token: {e}")

# Telegram bot handlers

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command."""
    await update.message.reply_text(
        "Welcome! Use the following commands:\n"
        "/search <query> - Search for onion links."
    )

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /search command."""
    query = ' '.join(context.args)
    if not query:
        await update.message.reply_text("Please provide a search query. Example: /search leaked database")
        return

    await update.message.reply_text(f"Searching for: {query}...\nThis may take some time.")

    # Scrape from Ahmia, DuckDuckGo, and Torch
    ahmia_results = scrape_ahmia(query)
    duckduckgo_results = scrape_duckduckgo(query)
    torch_results = scrape_torch(query)

    # Combine and deduplicate results
    all_results = list(set(ahmia_results + duckduckgo_results + torch_results))

    if all_results:
        # Save results to a file
        result_file = save_results(query, all_results)
        with open(result_file, "rb") as file:
            await update.message.reply_document(file)
        os.remove(result_file)
    else:
        await update.message.reply_text("No results found from any source.")

# Main function to run the bot

def main():
    """Run the bot."""
    # Load the token from token.exe
    bot_token = get_bot_token("token.exe")
    application = Application.builder().token(bot_token).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("search", search))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
