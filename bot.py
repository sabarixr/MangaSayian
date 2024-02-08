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
    msg = ''
    if message.content == 'recent release':
        names = get_names()
        name = names.split('\n')
        i =0
        for _ in name:
            i+=1
            if i>11:
                break
            if not _:
                msg +="........................"
                continue
            msg += f"{_}\n"
        await message.channel.send(msg)

    elif message.content.startswith('/link'):
        name_search = message.content
        print(name_search)
        title = name_search.strip("/link").strip()
        converted_title = title.lower().replace(" ", "-").replace("’", "")
        last_dash_index = converted_title.rfind('-')
        first_part = converted_title[:last_dash_index]
        last_part = converted_title[last_dash_index + 1:]
        output_title = first_part + "-chapter-" + last_part
        url = f"https://asuratoon.com/9643503911-{output_title}/"
        print(url)
        result = img_scraper(url)
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