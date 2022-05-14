from discord.ext import commands
import os
import discord
from dotenv import load_dotenv

client = commands.Bot(command_prefix='?', help_command=None)

#print to console that Bot is logged in
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#when messge with correct prefix (?) and then bot will respond
@client.command(name='ping')
async def ping_command(ctx):
    await ctx.channel.send('pong')


@client.event
async def on_message_join(memeber):
    channel = client.get_channel()
    embed=discord.Embed(color=0xFFEA00)
    embed.title = 'Welcome {memeber.name}'
    embed.description = 'Thank you for joining {memeber.guild.name}'
    embed.set_thumbnail(url = memeber.avatar_url)
    await channel.send(embed=embed)

#load env file and use token to run bot
load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))