import discord
import os
import random
from discord.ext import commands, tasks


class Cazzeggio(commands.Cog):
    def __init__(self, bot):
      self.bot = bot

    @commands.command('defacto')
    async def _defacto(self, ctx: commands.Context):
       """Usa l'intercalare del Sommo"""
       responses = ['DI FACTO', 'di facto']
       await ctx.send(random.choice(responses))
       
    @commands.command('conoscitore')
    async def _conoscitore(self, ctx: commands.Context):
       """Ripropone citazioni del Conoscitore Italiano"""
       responses = ['de facto, di facto', 'fanculizzati','Tra il lusco e il brusco,tra il serio e il profano,tra il serio e il faceto']
       await ctx.send(random.choice(responses))

    @commands.command('ciao')
    async def _ciao(self,ctx: commands.Context):
       """Saluta come Janos"""
       responses = ['tua madre colione', 'ollare', 'babbabia', 'cazzo vuoi?']
       await ctx.send(random.choice(responses))

    @commands.command(aliases=['auguri','buonanno'])
    async def _auguri(self,ctx: commands.Context):
       """Esplicita la sua felicità,ricambiando"""
       responses = ['fanculizzati', 'un bel paio di palle','fottiti']
       await ctx.send(random.choice(responses))

    @commands.command('spia')
    async def _spia(self,ctx: commands.Context):
       """Questo comando non esiste ihihih"""
       responses = ['✈️Sono un fottuto aereo✈️', 'scusate mi stanno chiamando📞','🔇🎧','🎶Bitches along my dick 🎶']
       await ctx.send(random.choice(responses)) 

def setup(bot):
  bot.add_cog(Cazzeggio(bot))       