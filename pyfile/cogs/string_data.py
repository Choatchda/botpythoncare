import discord
from discord.ext import commands

class string_data(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # # ลองใช้เมธอด String 
    @commands.command()
    async def islower(self, ctx, *, par):
        x = par.islower()
        emBed = discord.Embed(title="ลองใช้ islower", description="", color=0x6F9DC3)
        emBed.add_field(name="ตัวอย่างโค้ด", value='text = "{0}"\nx = text.islower()\nprint(x)' .format(par))
        emBed.add_field(name="ผลลัพธ์", value='{0}' .format(x))
        await ctx.channel.send(embed=emBed)

    
    # รับข้อความจาก User ใน Topic ต่างๆ
    @commands.Cog.listener("on_message")
    async def on_message(self, message):

         #  String 
        if message.content == "!string":
            emBed = discord.Embed(title="String", description="String ในภาษาไพทอน จะถูกล้อมไปด้วย Single Quote\
            หรือ Double Quote\nString Method ที่ใช้บ่อยในการทำโจทย์พิมพ์ !string ตามด้วยชื่อ Method เพื่อเรียกดู", color=0x6F9DC3)
            emBed.add_field(name="capitalize", value='เปลี่ยนตัวแรกให้เป็นตัวพิมพ์ใหญ่')
            emBed.add_field(name="islower", value='เช็คว่าเป็นตัวพิมพ์เล็กทั้งหมดไหม')
            emBed.add_field(name="count", value='นับจำนวนตัวอักษรในข้อความ')
            emBed.add_field(name="center", value='ทำหน้าที่จัด String ให้อยู่ตรงกลาง')
            emBed.add_field(name="find", value='หาตำเเหน่งของ String')
            emBed.add_field(name="index", value='บอกตำเเหน่งของ String')
            emBed.add_field(name="isalnum", value='เช็คว่ามีตัวอักษรหรือตัวเลขไหม')
            emBed.add_field(name="isalpha", value='เช็คว่าเป็นตัวอักษรไหม')
            emBed.add_field(name="isupper", value='เช็คว่าเป็นตัวพิมพ์ใหญ่ทั้งหมดไหม')
            emBed.add_field(name="isnumeric", value='เช็คว่าเป็นตัวเลขไหม')
            emBed.add_field(name="ljust", value='ทำให้ String อยู่ฝั่งซ้าย')
            emBed.add_field(name="lower", value='เเปลง String ตัวใหญ๋ให้เป็นตัวเล็ก')
            emBed.add_field(name="lstrip", value='ทำหน้าที่เอาช่องว่างด้านซ้ายของstringออก')
            emBed.add_field(name="replace", value='เเทนที่ String เก่าด้วย String ใหม่')
            emBed.add_field(name="rfind", value='หาตำเเหน่ง String จากทางด้านขวา')
            emBed.add_field(name="rjust", value='ทำให้ String อยู่ฝั่งขวา')
            emBed.add_field(name="strip", value='ทำหน้าที่นำช่องว่างทั้้งซ้ายเเละขวาออก')
            emBed.add_field(name="split", value='เปลี่ยน String เป็น List')
            emBed.add_field(name="swapcase", value='สลับ String ตัวเล็กให้เป็นตัวใหญ่เเละสลับ String ตัวใหญ่ให้เป็นตัวเล็ก')
            emBed.add_field(name="upper", value='เปลี่ยน String ให้เป็นตัวใหญ่ทั้งหมด')
            emBed.add_field(name="rsplit", value='hoh')
            await message.channel.send(embed=emBed)


        #  String เมธอด islower
        elif message.content == "!string islower":
            emBed = discord.Embed(title="string.islower", description="เช็คตัวอักษรทั้งหมดในข้อความว่าเป็นตัวพิมพ์เล็กหรือไม่ถ้าใช่จะ Return ค่าออกมาเป็น True", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "hello world!"\nx = txt.islower()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='True')
            emBed.add_field(name="ลองใช้ islower", value='โดยการพิม do islower (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)

        #  String เมธอด capitalize
        elif message.content == "!string capitalize":
            emBed = discord.Embed(title="string.capitalize", description="เปลี่ยนตัวอักษรตัวเเรกของประโยคให้เป็นตัวใหญ่เเล้วเปลี่ยนตัวอักษรที่เหลือเป็นตัวเล็ก", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "hello World!"\nx = txt.capitalize()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='Hello world!')
            emBed.add_field(name="ลองใช้ capitalize", value='โดยการพิม do cap (ข้อความที่ต้องการ)', inline=False)
            await message.channel.send(embed=emBed)

        #  String เมธอด count
        elif message.content == "!string count":
            emBed = discord.Embed(title="string.count", description="แสดงจำนวนของตัวอักษรที่เราเจอในข้อความตามที่เรากำหนด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Psit is veryhard hard"\nx = txt.count("hard")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='2')
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าว่าจะให้เริ่มนับตั้งเเต่ตำเเหน่งไหนและหยุดนับที่ตำแหน่งไหน', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Psit is veryeasy easy" \n x = txt.count("easy", 10, 17)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='1')
            emBed.add_field(name="ลองใช้ count", value='โดยการพิม do count (ข้อความที่ต้องการ) *count จะมีค่า = "money"', inline=False)
            await message.channel.send(embed=emBed)

        #  String เมทธอด center
        elif message.content == "!string center":
            emBed = discord.Embed(title="string.center", description="ทำหน้าที่จัด String ให้อยู่ตรงกลาง ", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana"\nx = txt.count("20")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='       banana       ')
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถกำหนดช่องว่างซ้ายขวาให้เป็นตัวเลขหรือตัวอักษรได้เเต่มีข้อระวังคือต้องทำเป็น String เท่านั้น', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana" \n x = txt.count("20", "O")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value='OOOOOOObananaOOOOOOO')
            emBed.add_field(name="ลองใช้ center", value='โดยการพิม do center (ความยาว, ตัวอักษรหรือตัวเลขที่ทำเป็นstringเพื่อมาเเทนช่องว่าง)', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string find":
            emBed = discord.Embed(title="string.find", description="หาตำเเหน่งของ String ที่กำหนดโดยจะเริ่มนับจาก0เเละถ้าหาไม่เจอจะ Return nค่าออกมาเป็น -1 ", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world."\nx = txt.find("welcome")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=7)
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าเพื่อให้เริ่มหาตำเเหน่งที่ตำเเหน่งไหนเเละหยุดหาที่ตำเเเหน่งไหน', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world." \n x = txt.find("e", 5, 10)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=8)
            emBed.add_field(name="ลองใช้ center", value='โดยการพิม do find (stringที่ต้องการหาจำเเเหน่ง, ตำเเหน่งที่จะให้เริ่มหา, ตำเเหน่งที่จะให้หยุดหา)', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string index":
            emBed = discord.Embed(title="string.index", description="บอกตำเเหน่งของ String ที่กำหนดโดยจะเริ่มนับจาก 0 เเละถ้าหาไม่เจอจะ Error", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world."\nx = txt.index("e")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=1)
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าเพื่อให้เริ่มหาตำเเหน่งที่ตำเเหน่งไหนเเละหยุดหาที่ตำเเเหน่งไหน', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world." \n x = txt.find("e", 5, 10)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=8)
            emBed.add_field(name="ลองใช้ center", value='โดยการพิม do index (String ที่ต้องการหาตำเเเหน่ง, ตำเเหน่งที่จะให้เริ่มหา, ตำเเหน่งที่จะให้หยุดหา)', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string isalnum":
            emBed = discord.Embed(title="string.isalnum", description="เช็ค String ทุกตัวว่าเป็น Alphabet(a-z)เเละมีเลข(0-9)ไหมถ้าตรงตามเงื่อนไขจะ Return ออกมาเป็น True", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Company12"\nx = txt.isalnum()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=True)
            emBed.add_field(name="ลองใช้ isalnum", value='โดยการพิม do isalnum', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string isalpha":
            emBed = discord.Embed(title="string.isalpha", description= "จะ Return ค่าเป็น True เมื่อ String ทุกตัวเป็น Alphabet(a-z)", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Company"\nx = txt.isalpha()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=True)
            emBed.add_field(name="ลองใช้ isalpha", value='โดยการพิม do isalpha', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string isnumeric":
            emBed = discord.Embed(title="string.isnumeric", description="จะ Return ค่าเป็น True เมื่อ String เป็นตัวเลขทั้งหมด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "1234345"\nx = txt.isnumeric()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=True)
            emBed.add_field(name="ลองใช้ isalpha", value='โดยการพิม do isnumeric', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string isupper":
            emBed = discord.Embed(title="string.isupper", description="จะ Return ค่าเป็น True เมื่อ String เป็นตัวเลขใหญ่ทั้งหมด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "CENTER"\nx = txt.isupper()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=True)
            emBed.add_field(name="ลองใช้ isalpha", value='โดยการพิม do isupper', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string ljust":
            emBed = discord.Embed(title="string.ljust", description="จะ Return ค่า String ชิดซ้ายเเล้วช่องว่างที่เหลือจะอยู่ด้านขวา", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana"\nx = txt.ljust(20)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="banana              ")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าเพิ่มอีกตัวเพื่อเปลี่ยนจากช่องว่างเป็น String', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana" \n x = txt.ljust(20, "O"\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="bananaOOOOOOOOOOOOOO")
            emBed.add_field(name="ลองใช้ ljust", value='โดยการพิม do ljust(ความยาว, String ที่ต้องการมาเเทนช่องว่าง)', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string lower":
            emBed = discord.Embed(title="string.lower", description="เเปลง String ตัวใหญ๋ให้เป็นตัวเล็ก", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "OOP"\nx = txt.lower()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="oop")
            emBed.add_field(name="ลองใช้ lower", value='โดยการพิม do lower', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string lstrip":
            emBed = discord.Embed(title="string.lstrip", description="ทำหน้าที่เอาช่องว่างด้านซ้ายของ String ออก", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "       OOP  "\nx = txt.lstrip()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="OOP  ")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถนำ String ที่ไม่ต้องการทางด้านซ้ายออกได้โดยการใส่ String ที่ต้องการนำออกไป', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "aaaaOOPmm"\nx = txt.lstrip()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="OOPmm")
            emBed.add_field(name="ลองใช้ lstrip", value='โดยการพิม do lstrip(stringที่ต้องการลบทางด้านซ้าย)', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string replace":
            emBed = discord.Embed(title="string.replace", description="เเทนที่ String เก่าด้วย String ใหม่", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "I like bananas"\nx = txt.replace("bananas", "apples")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="I like apples")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='ถ้ามีคำซ้ำหลายๆคำสามารถกำหนดได้ว่าจะเเทนเเค่กี่คำ', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "one one was a race horse, two was one too."\nx = txt.replace("one", "five", 2)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="five five was a race horse, two was one too.")
            emBed.add_field(name="ลองใช้ replace", value='โดยการพิม do replace(String ตัวที่ต้องการให้โดนเเทนที่, String ที่จะให้เเทนที่, จำนวนที่จะให้เเทน)', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string rfind":
            emBed = discord.Embed(title="string.rfind", description="หาตำเเหน่งจากทางด้านขวาโดยจะเริ่มจาก0จะนับตำเเหน่งปกติเเต่จะเอาตำเเหน่งด้านขวาก่อน", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world."\nx = txt.rfind("e")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=13)
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าเพื่อให้เริ่มหาตำเเหน่งที่ตำเเหน่งไหนเเละหยุดหาที่ตำเเเหน่งไหน', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Hello, welcome to my world."\nx = txt.rfind("e", 5, 10)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value=8)
            emBed.add_field(name="ลองใช้ rfind", value='โดยการพิม do rfind(String ที่ต้องการหา, ตำเเหน่งที่ต้องการเริ่มหา, ตำเเหน่งที่ต้องการให้หยุดหา)', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string rjust":
            emBed = discord.Embed(title="string.rjust", description="Return ค่าออกมาในรูปเเบบที่ String ชิดขวาเเล้วช่องว่างอยู่ซ้าย", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana"\nx = txt.rjust(20)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="              banana")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถใส่ค่าเพิ่มอีกตัวเพื่อเปลี่ยนจากช่องว่างเป็น String', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "banana"\nx = txt.rjust(20, "O")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="OOOOOOOOOOOOOObanana")
            emBed.add_field(name="ลองใช้ rjust", value='โดยการพิม do rjust (ความยาว, เป็นstringที่ต้องการให้เเทนที่ช่องว่าง)', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string rsplit":
            emBed = discord.Embed(title="string.rsplit", description="", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = ""\nx = txt.()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = ""\nx = txt.()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="")
            emBed.add_field(name="ลองใช้ rsplit", value='โดยการพิม do rsplit()', inline=False)
            await message.channel.send(embed=emBed)
        
        elif message.content == "!string strip":
            emBed = discord.Embed(title="string.strip", description="ทำหน้าที่นำช่องว่างทั้้งซ้ายเเละขวาออก", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "     banana     "\nx = txt.strip()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="banana")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถกำหนดว่าจะเอา String ตัวไหนออก', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "mmmbananammm"\nx = txt.strip("mmm")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="banana")
            emBed.add_field(name="ลองใช้ strip", value='โดยการพิม do strip (String ที่ต้องการให้ลบ)', inline=False)
            await message.channel.send(embed=emBed)
    
        elif message.content == "!string split":
            emBed = discord.Embed(title="string.split", description="นำ String ที่ไม่ต้องการออกเเละเเปลง String ที่เหลือให้อยู่ในรูปเเบบของ List", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "apple#banana#cherry#orange""\nx = txt.split("#")\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="['apple', 'banana', 'cherry', 'orange']")
            emBed.add_field(name="ตัวอย่างเพิ่มเติม", value='สามารถกำหนดว่าจะเอาstringตัวทีจะให้เอาออกกี่ตัว', inline=False)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "apple#banana#cherry#orange""\nx = txt.split("#", 1)\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="['apple', 'banana#cherry#orange']")
            emBed.add_field(name="ลองใช้ split", value='โดยการพิม do split (String ที่ต้องการให้เอาออก, จำนวนที่จะให้เอาออก)', inline=False)
            await message.channel.send(embed=emBed)

        elif message.content == "!string swapcase":
            emBed = discord.Embed(title="string.swapcase", description="สลับ String ตัวเล็กให้เเป็นตัวใหญ่เเละสลับ String ตัวใหญ่ให้เป็นตัวเล็ก", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "Apple bANANA"\nx = txt.swapcase()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="aPPLE Bnana")
            emBed.add_field(name="ลองใช้ swapcase", value='โดยการพิม do swapcase', inline=False)
            await message.channel.send(embed=emBed)

        elif message.content == "!string upper":
            emBed = discord.Embed(title="string.upper", description="เปลี่ยน String ให้เป็นตัวใหญ่ทั้งหมด", color=0x6F9DC3)
            emBed.add_field(name="ตัวอย่างโค้ด", value='txt = "apple"\nx = txt.upper()\nprint(x)')
            emBed.add_field(name="ผลลัพธ์", value="APPLE")
            emBed.add_field(name="ลองใช้ upper", value='โดยการพิม do upper', inline=False)
            await message.channel.send(embed=emBed)




def setup(bot):
    bot.add_cog(string_data(bot))
