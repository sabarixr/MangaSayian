from discord.ext import commands
from first_app import img_scraper
from scraper_names import get_names,get_top

def bot_commands(bot):
    @bot.event
    async def on_ready():
        print('Bot is ready!')

    @bot.command(aliases=["li_nk"])
    async def link(ctx):
        name_search = ctx.message.content
        print(name_search)
        title = (name_search.lstrip("/link").strip()).lower().replace(" ", "-").replace("’", "").rsplit('-', 1)
        output_title = f"{title[0]}-chapter-{title[1]}"
        url = f"https://asuratoon.com/9643503911-{output_title}/"
        print(url)
        result = img_scraper(url)
        await ctx.send(result)

    @bot.command(aliases=["rec_ent"])
    async def recent(ctx):
        names = get_names()
        await ctx.send(names)

    @bot.command(aliases=["che_ck"])
    async def check(ctx):
        await ctx.send("not added the code yet")

    @bot.command(aliases=["t_op"])
    async def top(ctx):
        popular = get_top()
        await ctx.send(popular)

    @bot.command(aliases=["in_fo"])
    async def info(ctx):
        await ctx.send("not added the code yet")

    @bot.command(aliases=["he_lp"])
    async def help(ctx):
        help_message = '''
        ```
        /link <name of the webtoon><chapter number>**: Get the direct link to the specified chapter of your favorite manga.

        \n/help: Need assistance? Use this command to get a list of available commands along with a brief introduction to Manga Man.

        \n/recent: Quickly access the most recently added webtoon with just a single command.

        \n/check <name of the webtoon>: Stay up-to-date with the recent chapters of a specific webtoon series.

        \n/top: Explore the currently popular manga titles with this command.

        \n/info <manga name>: Obtain detailed information about a specific manga, including its author, genres, and more!
        ```
        '''
        await ctx.send(help_message)
