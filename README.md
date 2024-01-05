Currently requires env var named TOKEN containing your discord bot token from the developer portal: https://discord.com/developers/applications

If you want to replace with a locally stored token file, create a token.txt file in the directory with the bot and place only your bot token in the file. Replace the ``BOT_TOKEN = os.getenv('TOKEN')`` line with ``BOT_TOKEN = token_file.read()`` directly **ABOVE** this line, add the line ``token_file = open("token.txt")``. The bot should now launch using your token. 

Be sure the ``.gitignore`` file in your directory contains the token.txt (or whatever you named it) file prior to uploading it online, or discord may automatically reset your token.
