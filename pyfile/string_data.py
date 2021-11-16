import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="do ")


# ลองใช้ islower
@bot.command()
async def islower(ctx, *, par):
    x = par.islower()
    emBed = discord.Embed(title="ลองใช้ islower", description="", color=0x6F9DC3)
    emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.islower()\nprint(x)' .format(par))
    emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
    await ctx.channel.send(embed=emBed)

# ลองใช้ count
@bot.command()
async def count(ctx, *, par):
    x = par.count("money")
    emBed = discord.Embed(title="ลองใช้ islower", description="", color=0x6F9DC3)
    emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.count(money)\nprint(x)' .format(par))
    emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
    await ctx.channel.send(embed=emBed)

# ลองใช้ capitalize
@bot.command()
async def cap(ctx, *, par):
    x = par.capitalize()
    emBed = discord.Embed(title="ลองใช้ islower", description="", color=0x6F9DC3)
    emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.capitalize()\nprint(x)' .format(par))
    emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
    await ctx.channel.send(embed=emBed)

@bot.event
async def on_message(message):

    # เกี่ยวกับบอท
    if message.content == "!pc":
        emBed = discord.Embed(title="Python Care", description="Python Care ตัวช่วยที่จะทำให้คุณหา Method ที่ใช้งานในบ่อยครั้งในการเรียนวิชา PSIT", color=0x6F9DC3)
        emBed.set_thumbnail(url="https://cdn.discordapp.com/attachments/901727442887143424/902060735973163059/voe.png")
        emBed.add_field(name="พิมพ์ !หัวข้อข้างล่าง ", value='string')
        emBed.set_footer(text="Created by 2P1B", icon_url="https://cdn.discordapp.com/attachments/895008902712807494/902127838344380446/image-removebg-preview.png")
        await message.channel.send(embed=emBed)

    # สตริง
    elif message.content == "!string":
        emBed = discord.Embed(title="String", description="String Method ที่ใช้บ่อยในการทำโจทย์\nพิมพ์ !string ตามด้วยชื่อ Method เพื่อเรียกดู", color=0x6F9DC3)
        emBed.add_field(name="capitalize", value='เปลี่ยนตัวแรกให้เป็นตัวพิมพ์ใหญ่', inline=False)
        emBed.add_field(name="islower", value='เช็คว่าเป็นตัวพิมพ์เล็กทั้งหมดไหม', inline=False)
        emBed.add_field(name="count", value='นับจำนวนตัวอักษรในข้อความ', inline=False)
        await message.channel.send(embed=emBed)

    # สตริงเมธอด islower
    elif message.content == "!string islower":
        emBed = discord.Embed(title="string.islower", description="เช็คตัวอักษรทั้งหมดในข้อความว่าเป็นตัวพิมพ์เล็กหรือไม่ถ้าใช่จะ Return ค่าออกมาเป็น True", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "hello world!"\nx = txt.islower()\nprint(x)')
        emBed.add_field(name="ผลลัพธ์", value='True')
        emBed.add_field(name="ลองใช้ islower", value='โดยการพิม do islower (ข้อความที่ต้องการ)', inline=False)
        await message.channel.send(embed=emBed)

    # สตริงเมธอด capitalize
    elif message.content == "!string capitalize":
        emBed = discord.Embed(title="string.capitalize", description="เปลี่ยนตัวอักษรตัวเเรกของประโยคให้เป็นตัวใหญ่เเล้วเปลี่ยนตัวอักษรที่เหลือเป็นตัวเล็ก", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "hello World!"\nx = txt.capitalize()\nprint(x)')
        emBed.add_field(name="ผลลัพธ์", value='Hello world!')
        emBed.add_field(name="ลองใช้ capitalize", value='โดยการพิม do cap (ข้อความที่ต้องการ)', inline=False)
        await message.channel.send(embed=emBed)

    # สตริงเมธอด count
    elif message.content == "!string count":
        emBed = discord.Embed(title="string.count", description="แสดงจำนวนของตัวอักษรที่เราเจอในข้อความตามที่เรากำหนดให้หาใน count", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Psit is veryhard hard"\nx = txt.count("hard")\nprint(x)')
        emBed.add_field(name="ผลลัพธ์", value='2')
        emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าว่าจะให้เริ่มนับตั้งเเต่ตำเเหน่งไหนและหยุดนับที่ตำแหน่งไหน', inline=False)
        emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Psit is veryeasy easy" \n x = txt.count("easy", 10, 17)\nprint(x)')
        emBed.add_field(name="ผลลัพธ์", value='1')
        emBed.add_field(name="ลองใช้ count", value='โดยการพิม do count (ข้อความที่ต้องการ) *count จะมีค่า = "money"', inline=False)
        await message.channel.send(embed=emBed)
    
    await bot.process_commands(message)

bot.run("OTAxODQ5OTMwNjg2MTQ0NTcy.YXV3Mw.yYz_19O9F-r-s3G155b0IW6Y4cs")
