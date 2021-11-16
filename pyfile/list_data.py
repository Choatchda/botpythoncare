import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="do ")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("!pc เพื่อเริ่มใช้งาน"))
    print(f"Login As {bot.user}")


@bot.event
async def on_message(message):

    # ลิสต์
    if message.content == "!list":
        emBed = discord.Embed(title="List", description="Listคือ ชุดข้อมูลแบบคอลเล็คชันที่มีการเรียงลำดับ และสามารถแก้ไขได้ จะใช้เครื่องหมาย []", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value="text =['apple', 'banana', 'cherry']")
        emBed.add_field(name="ผลลัพธ์", value="apple, banana, cherry")
        await message.channel.send(embed=emBed)

    # ลิสต์เมธอด append
    elif message.content == "!list append":
        emBed = discord.Embed(title="Append", description="Method ที่เพิ่มสมาชิกใน List", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value="text =['apple', 'banana', 'cherry']\nx = text.clear()\nprint(x)") 
        emBed.add_field(name="ผลลัพธ์", value=['apple', 'banana', 'cherry', 'orange'])
        await message.channel.send(embed=emBed)


    
    await bot.process_commands(message)

bot.run("OTAxODQ5OTMwNjg2MTQ0NTcy.YXV3Mw.yYz_19O9F-r-s3G155b0IW6Y4cs")
