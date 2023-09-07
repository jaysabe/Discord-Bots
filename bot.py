import os

import discord
# from discord.ext import commands
from dotenv import load_dotenv

# environment variable
load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
intents = discord.Intents(messages=True, guilds=True, message_content=True) # changed to cover for gild role and message_contents role

client = discord.Client(intents=intents)

#Will convert this into keymap soon TODO:
# set server and channel variables
server1 = 1138259376109539338  # original server
channel1 = 1138267923987845150  # original server channel id
channel2 = 1139373875956813854  # new server channel


async def fwd_message(des_channel, author, message):
    print("tested TRUE")
    if des_channel is None:  # used for testing
        print(f"Invalid channel ID: {des_channel}")
        return
    # Forward message content along with author's name
    print(f"{author} posted new resource: {message} , des_channel: {des_channel}, {channel2}")  # for testing purposes
    content = f"{author} posted new student resource: {message}"
    await des_channel.send(content)


@client.event
# Message when bot runs without errors
async def on_ready():
    print(f"Bot is ready! 😁 Welcome {client.user.name} operator.")


@client.event
async def on_message(message):
    # Check server and channel ids before running
    if message.guild.id == server1 and message.channel.id == channel1:
        await run_bot(message)
    else:  # Have the 'sleep' function here?
        print(f"Post detected in '{message.channel}' . No further actions needed. ")


async def run_bot(message):
    embedded_links = [embed.url for embed in message.embeds if embed.type == "link" or embed.type == "video"
                      or embed.type == "article"]
    # attached_files = [attachment.url for attachment in message.attachments] -Here for later patches
    if embedded_links:
        print("embedded link detected")
        # Set variables:
        author_name = message.author.name
        message_content = message.content
        des_channel = client.get_channel(channel2)
        # testing mechanic first (from 1 txt channel to another (same server)
        await fwd_message(des_channel, author_name, message_content)

client.run(TOKEN)
