import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("!pc เพื่อเริ่มใช้งาน"))
    print(f"Login As {bot.user}")

# เรียกใช้งานบอท !pc
@bot.command()
async def pc(ctx):
    emBed = discord.Embed(title="Python Care", description="Python Care ตัวช่วยที่จะทำให้คุณหา Method ที่ใช้งานในบ่อยครั้งในการเรียนวิชา PSIT", color=0x6F9DC3)
    emBed.set_thumbnail(url="https://cdn.discordapp.com/attachments/901727442887143424/902060735973163059/voe.png")
    emBed.add_field(name="พิมพ์ !หัวข้อข้างล่าง ", value='string')
    emBed.set_footer(text="Created by 2P1B", icon_url="https://cdn.discordapp.com/attachments/895008902712807494/902127838344380446/image-removebg-preview.png")
    await ctx.send(embed=emBed)

initial_extensions = []

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])
    
if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)


bot.run("OTAxODQ5OTMwNjg2MTQ0NTcy.YXV3Mw.yYz_19O9F-r-s3G155b0IW6Y4cs")
