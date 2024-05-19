import discord
from discord.ext import commands
import requests
import asyncio
import re
from keep_alive import keep_alive
import os

kageookimi = os.environ.get("userToken")

desired =  ["moltres","bulbasaur", "venusaur", "charmander", "charizard", "squirtle", "blastoise", "Pikachu", "raichu", "vulpix", "ninetales", "ponyta", "gengar", "kangaskhan", "lapras", "scyther", "pinsir", "magikarp", "gyarados", "ditto", "eevee", "vaporeon", "jolteon", "flareon", "aerodactyl", "snorlax", "dragonite", "bayleef", "cyndaquil", "pichu", "politoed", "espeon", "umbreon", "unown", "wobbuffet", "onix", "steelix", "scizor", "heracross", "corsola", "skarmory", "smeargle", "elekid", "miltank", "tyranitar", "torterra", "infernape", "piplup", "pachirisu", "chingling", "bonsly", "mime jr.", "happiny", "chatot", "spiritomb", "gible", "gabite", "garchomp", "munchlax", "riolu", "lucario", "carnivine", "leafeon", "glaceon", "gallade", "rotom", "audino", "maractus", "sigilyph", "zoroark", "deerling", "emolga", "chandelure", "cubchoo", "cryogonal", "druddigon", "frogadier", "greninja", "vivillon", "talonflame", "florges", "skiddo", "gogoat", "furfrou", "espurr", "meowstic", "tyrunt", "aurorus", "sylveon", "hawlucha", "dedenne", "carbink", "goodra", "hydreigon", "klefki", "noibat", "noivern", "oricorio", "rockruff", "lycanroc", "wishiwashi", "stufful", "comfey", "oranguru", "passimian", "pyukumuku", "minior", "komala", "turtonator", "togedemaru", "mimikyu", "drampa", "dhelmise", "kommo-o", "rillaboom", "cinderace", "inteleon", "corviknight", "eldegoss", "wooloo", "appletun", "cramorant", "sinistea", "grimmsnarl", "perrserker", "cursola", "mr. rime", "runerigus","falinks", "pincurchin", "snom", "frosmoth", "stonjourner", "eiscue", "morpeko", "duraludon", "dragapult", "sprigatito", "meowscarada", "fuecoco", "skeledirge", "quaquaval", "tinkaton", "annihilape", "clodsire", "kingambit", "baxcalibur", "Arboliva", "Ponyta", "Finizen", "Tyrunt", "Woobat", "Snover", "Wooper", "Obstagoon", "Porygon", "Poliwag", "Gastly", "Amaura", "Diglett", "Aron", "Zorua", "Phantump", "Mareep", "Dreepy", "Drakloak", "Goomy", "Gardevoir", "Gallade", "Litwick", "Dewpider", "Axew", "Dratini","Ralts", "Tadbulb", "Stunky", "Skuntank", "Glimmet", "Buneary", "Lopunny", "Bellossom", "Vileplume", "Ledian", "Linoone", "Beautifly", "Milotic", "Leavanny", "Cinccino", "Swanna", "Ribombee", "Togedemaru", "Wyrdeer", "azurill", "sableye", "mawile", "plusle", "minun", "torkoal", "spinda", "zangoose", "seviper", "lunatone", "solrock", "kecleon", "chimecho", "tropius", "absol", "wynaut", "relicanth","luvdisc"]
client = commands.Bot(command_prefix=".", intents=discord.Intents.all())
@client.event
async def on_ready():
    print("I am up")

@client.command()
async def hello(ctx):
    await ctx.send("Hello World")

async def get_channel_id_by_name(guild, channel_name):
    for channel in guild.channels:
        if channel.name == channel_name:
            return channel.id
    return None

@client.command()
async def show(ctx):
    for channel in ctx.channel:
        print(channel.name)

excludedChannel = [1123638853501194301,1240828249127391234,1241501783042424893]

def sendText(msg,channel):
        payload = {
           "content":f"{msg}"
        }

        header = {
           "authorization":kageookimi
        }
        r = requests.post(f"https://discord.com/api/v9/channels/{channel}/messages",data = payload, headers = header) 

def keep_first_line(multiline_string):
    # Split the multiline string into lines and return the first line
    first_line = multiline_string.splitlines()[0]
    return first_line

def remove_percentage(text):
    # Define a regular expression pattern to match the percentage value
    pattern = r':\s*\d+\.\d+%'
    # Use re.sub() to replace the matched pattern with an empty string
    result = re.sub(pattern, '', text)
    return result.strip()  # Remove leading and trailing whitespaces


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.channel.id not in excludedChannel and message.author.id == 716390085896962058:
        await asyncio.sleep(3)
        text = []
        async for message in message.channel.history(limit=1):
            text.append(message)
        if text[0].content.endswith("%"):
            pokemon = remove_percentage(keep_first_line(text[0].content)).title()
            if pokemon in desired:
                await message.channel.edit(name=pokemon)
                await asyncio.sleep(2)
                ID = sendText(f".add_channel exclusivespawn",message.channel.id)
                await asyncio.sleep(1)
                sendText(f".redirection exclusivespawn",message.channel.id)


@client.command()
async def add_channel(ctx,*,channel_name):
    # CATEGORY_NAME = "ShinyHunt"
    guild = ctx.guild
    # category = discord.utils.get(guild.categories, name=CATEGORY_NAME)

    # if category is None:
    #     await ctx.send(f"Category '{CATEGORY_NAME}' not found.")
    #     return

    # try:
    #     new_channel = await guild.create_text_channel(name=channel_name, category=category)
    #     await ctx.send(f"Channel '{new_channel.name}' created successfully in '{CATEGORY_NAME}' category.")
    # except discord.HTTPException as e:
    #     await ctx.send(f"Failed to create channel: {e}")
    new_channel = await guild.create_text_channel(name=channel_name)


@client.command()
async def spam(ctx,args):
    for i in range(1,int(args)+1):
        payload = {
           "content":f"Xp generator comment No.{i}"
        }

        header = {
           "authorization":kageookimi
        }
        r = requests.post("https://discord.com/api/v9/channels/1240376251143815238/messages",data = payload, headers = header)
        await asyncio.sleep(0.5)

@client.command()
async def new(ctx,arg):
    id = ctx.channel.id
    await ctx.channel.edit(name=arg)

@client.command()
async def redirection(ctx,arg):
    getName = await get_channel_id_by_name(ctx.guild,arg)
    sendText(f"<@{716390085896962058}> redirect {client.get_channel(getName).mention}",ctx.channel.id)

keep_alive()
client.run(os.environ.get("token"))
