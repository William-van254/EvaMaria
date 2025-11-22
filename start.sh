
# 1. New: Install the missing web server library (aiohttp)
pip install aiohttp

# 2. Original: Install the main bot dependencies
pip3 install -U -r requirements.txt

# 3. Start the bot (and web server)
echo "Starting Bot...."
python3 web_server.py &
python3 bot.py
