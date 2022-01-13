import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(prettyspace):
    if prettyspace.author == client.user:
        return

    if prettyspace.content.startswith('$hello'):
        await prettyspace.channel.send('Hello!')

client.run(os.getenv('TOKEN'))