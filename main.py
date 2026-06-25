‏import discord
‏from discord.ext import commands, tasks
‏import os

‏TOKEN = os.getenv("TOKEN")
‏VOICE_CHANNEL_ID = 1515629459045093389

‏intents = discord.Intents.default()
‏bot = commands.Bot(command_prefix="!", intents=intents)

‏async def join_voice():
‏    channel = bot.get_channel(VOICE_CHANNEL_ID)

‏    if channel is None:
‏        print("Voice channel not found")
‏        return

‏    try:
‏        if not bot.voice_clients:
‏            await channel.connect()
‏            print("Connected")
‏    except Exception as e:
‏        print(e)

‏@bot.event
‏async def on_ready():
‏    print(f"Logged in as {bot.user}")
‏    await join_voice()

‏@tasks.loop(minutes=1)
‏async def keep_connected():
‏    if not bot.voice_clients:
‏        await join_voice()

‏@bot.event
‏async def setup_hook():
‏    keep_connected.start()

‏bot.run(TOKEN)
