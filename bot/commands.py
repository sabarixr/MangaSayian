import discord
from .funtions.scraper_names import get_top

def bot_commands(bot):
    @bot.event
    async def on_ready():
        print('Bot is ready!')

    class MangaView(discord.ui.View):
        def __init__(self, manga_data):
            super().__init__()
            self.current_page = 0
            self.page_size = 5
            self.manga_data = manga_data

            # Disable the previous button on the first page
            self.children[0].disabled = True

            # Disable the next button if there's only one page
            if len(self.manga_data) <= self.page_size:
                self.children[1].disabled = True

        def generate_embeds(self):
            start_index = self.current_page * self.page_size
            end_index = start_index + self.page_size
            embeds = []

            for manga in self.manga_data[start_index:end_index]:
                embed = discord.Embed(
                    title=manga.get('title', 'No Title'),
                    color=discord.Color.blue()
                )
                embed.set_thumbnail(url="https://toonily.com/wp-content/uploads/2020/06/TBATE2024cover_tapas-175x238.jpg")
                embed.add_field(name='Rating', value=manga.get('rating', 'N/A'), inline=True)
                embed.add_field(name='Viewers', value=manga.get('viewers', 'N/A'), inline=True)
                embed.add_field(name='Chapters', value=', '.join(manga.get('chapters', [])) or 'No Chapters', inline=False)
                embeds.append(embed)

            return embeds

        @discord.ui.button(label="Previous", style=discord.ButtonStyle.primary)
        async def previous_button_callback(self, button, interaction):
            self.current_page -= 1

            # Disable the previous button on the first page
            if self.current_page == 0:
                button.disabled = True

            # Enable the next button as we are moving back from a non-final page
            self.children[1].disabled = False

            embeds = self.generate_embeds()
            await interaction.response.edit_message(embeds=embeds, view=self)

        @discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
        async def next_button_callback(self, button, interaction):
            self.current_page += 1

            # Disable the next button on the last page
            if (self.current_page + 1) * self.page_size >= len(self.manga_data):
                button.disabled = True

            # Enable the previous button as we are moving forward from the first page
            self.children[0].disabled = False

            embeds = self.generate_embeds()
            await interaction.response.edit_message(embeds=embeds, view=self)

    @bot.slash_command(name="top", description="Shows trending manhwas")
    async def top(interaction: discord.Interaction):
        try:
            manga_data = get_top()
            print(manga_data)
            print("it is here")

            if not isinstance(manga_data, list):
                await interaction.response.send_message("Error: Expected a list of manga data.")
                return

            if not manga_data:
                await interaction.response.send_message("No manga data available.")
                return

            view = MangaView(manga_data)
            embeds = view.generate_embeds()
            await interaction.response.send_message(embeds=embeds, view=view)

        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {str(e)}")
