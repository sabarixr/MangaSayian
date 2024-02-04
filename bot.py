import discord
from discord.ext import commands
from first_app import img_scraper
from scraper_names import get_names

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print('Bot is ready!')

@bot.event
async def on_message(message):
    if message.author == bot.user:  # To avoid the bot processing its own messages
        return

    if message.content == 'recent release':
        names = get_names()
        name = names.split('\n')
        for _ in name:
            if not _:
                continue
            await message.channel.send(_)

    elif message.content.startswith('/link'):
        name_search = message.content.split(' ')
        if len(name_search) < 3:
            await message.channel.send('Please enter the name of the manga and chapter')
        else:
            manga_name = name_search[1]
            chapter = name_search[2]
            result = img_scraper(manga_name, chapter)
            await message.channel.send(result)

    elif message.content == 'help':
        help_message = '''
        /recent release - for getting the recent release
        /search <name> - to check whether there is a manga of that name [under development]
        /help - for getting help about this bot
        /link <name> - for getting the ad-free link of manga
        '''
        await message.channel.send(help_message)

bot.run("MTIwMzQyMjcxNDQ0Mjk0MDQ4Ng.GCUGDm.zAL126OawaD6BKLGkFuA-VqomK7SU5KupFdCE8")