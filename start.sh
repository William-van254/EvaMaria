
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py

# This command starts the fake web server in the background (&)
python3 web_server.py &

# This command starts the main bot process
python3 bot.py

