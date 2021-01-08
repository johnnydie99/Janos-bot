import discord
from discord.ext import commands, tasks


class Utile(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(pass_context=True, aliases=['c', 'canc'])
  @commands.has_permissions(manage_guild=True)
  async def cancella(self,ctx: commands.Context, righe=10):
     """Cancella fino a un massimo di 10 righe"""
     await ctx.channel.purge(limit=righe + 1)

def setup(bot):
  bot.add_cog(Utile(bot))       