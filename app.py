import discord
from discord import client
from discord import embeds
from discord.ext import commands
from discord import message

client = commands.Bot(command_prefix=".")

@client.event

async def on_ready():
    print(f"Logged in as { client.user} ")

@client.command()
async def hello(ctx):
    await ctx.send(f"hey! {ctx.author.mention}")

@client.command(pass_context=True)
async def poll(ctx,*,message):
    embed=discord.Embed(title="preferred way of investing", description=message, color=0x3498db)
    # embed.set_footer(text="created by Aditya")
    msg = await ctx.send(embed=embed)

    await msg.add_reaction("🅰")
    await msg.add_reaction("🅱")
    await msg.add_reaction("©")
    
    
    await ctx.msg.delete()

client.run("ODkwMTg1NjcyMTcyOTEyNjUw.YUsIAw.umhIvL6ACx05KyPL5cSM769Mfak")
