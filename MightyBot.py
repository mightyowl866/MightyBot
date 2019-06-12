import discord
import random


#   MightyBot is made by MightyOwl86.


client = discord.Client()

h_mario_quotes = ['"You know what they say! All toasters, toast toast!"',
                  '"Nice of the princess to invite us over for a picnic, eh Luigi?"',
                  '"Dear pesky plumbers,The Koopalings and I have taken over the Mushroom Kingdom! The princess is now a permanent guest at one of my seven Koopa Hotels. I dare you to find her if you can!"',
                  '"We gotta find the princess!"',
                  '"Its hard to see through those clouds. I hope we can get rid of em! ***Get the hint?***"',
                  "Hey you! Get off of my cloud!"]




itgoodlist = ['Its GOOD!','Ehhhhhh kinda','HOLY ***FUCK*** THATS GOOD','***n o***','e w']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

#-----------Message Commands----------------------------------------------------------------#

    if message.content.startswith('?hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('?uplog'):
        await message.channel.send('Added updog.')

    if message.content.startswith('?jojo'):
        await message.channel.send('AWAKEN MY PILLARMEN!', file=discord.File('pillarmen.jpg'))

    if message.content.startswith('?mfdoom'):
        await message.channel.send('MF Doom.')

    if message.content.startswith('?my'):
        await message.channel.send('name jeff')

    if message.content.startswith('?hotelmario'):
        await message.channel.send(random.choice(h_mario_quotes))

    if message.content.startswith('?itgood'):
        await message.channel.send(random.choice(itgoodlist))

    if message.content.startswith('?fe'):
        await message.channel.send('Fe stands for Fire Emblem. In other words, a ***BAD GAME***')
##################################################################################################################

    if "584851456272629770" in message.content:
        await message.channel.send('Yo thats me')
    if 'updog'.lower() in message.content:
        await message.channel.send('***GOT EM***')
    if 'todd'.lower() in message.content:
        await message.channel.send('',file=discord.File('todd.jpg'))
    if 'skyrim'.lower() in message.content:
        await message.channel.send('',file=discord.File('happy_todd.jpg'))
    if 'fallout 76'.lower() in message.content:
        await message.channel.send('',file=discord.File('angry_todd.jpg'))
    if 'it just works'.lower() in message.content:
        await message.channel.send('https://www.youtube.com/watch?v=J6bfVlKoczQ', file=discord.File('todd.jpg'))
    if 'fallout 4'.lower() in message.content:
        await message.channel.send(' ', file=discord.File('todd.jpg'))



    if 'oblivion'.lower() in message.content:
        await message.channel.send('HaHa remember Oblivion guys? Nevermind that, please buy Skyrim.',file=discord.File('angry_todd.jpg'))
#-------------------------------------------------------------------------------------------#






client.run('NTg0ODUxNDU2MjcyNjI5Nzcw.XPlyEg.fi-LJFNaI7Em6--eIuCkGOoVfWQ')