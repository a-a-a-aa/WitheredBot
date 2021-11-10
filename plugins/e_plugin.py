from discord.ext import commands
from requests import get

from .help_func import embed_help
from discord import Embed


class E(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def explain(self, ctx, word=""):
        if str(word).strip() == "":
            await ctx.send(embed=await (embed_help("explain [Word]")))
        else:
            data = get(
                f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            ).json()
            try:
                meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
                dict_embed = Embed(title=data[0]["word"], description=meaning)
            except:
                dict_embed = Embed(
                    title=data["title"] or "NaN", description=data["message"] or "not valid"
                )
            finally:
                await ctx.send(embed=dict_embed)


def setup(bot):
    return E(bot)