# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import os
from dotenv import load_dotenv
import random

# Laddar in ENV filen.
load_dotenv()
# Tar token från env filen
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()

# Lyssnar på om botten går online.
@bot.event
async def on_ready():
    guild_count = 0
    for guild in bot.guilds:
        # Skriver ut vilka servrar som använder botten och deras ID.
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1

    # Skriver ut hur många servrar som använder skolbotten
    print("Skolbotten är på " + str(guild_count) + " servrar.")

# Hit skickas meddelanden till botten
@bot.event
async def on_message(message):
    if message.content == "?Schema":
        await message.channel.send(f" **Här är schemat för IA 2020:** \n https://schema.mau.se/setup/jsp/Schema.jsp?startDatum=idag&intervallTyp=m&intervallAntal=6&sokMedAND=false&sprak=SV&resurser=p.TGIAA20h%2C")

    if message.content == "?Utbildningsplan":
        await message.channel.send(f" **Här kommer utbildningsplanen för IA 2020** \n https://utbildningsinfo.mau.se/program/tgiaa/start/20202-08012/utbildningsplan/20202")

    if message.content == "?Zoom":
        await message.channel.send(f" **Här kommer zoom-länkar (Uppdaterat 220101)** \n ")
        await message.channel.send(f"**UX Evaluation Methods:** \n https://mau-se.zoom.us/j/68252593279?pwd=Q2J0YStuRTRlVWtnN0V6bWphNUlNUT09 \n")
        await message.channel.send(f"**Informationssäkerhet:**  \n https://mau-se.zoom.us/j/3901938246 \n")


    if message.content.startswith("?Vem"):
        channel = message.channel
        randomMember = random.choice(channel.guild.members)
        await channel.send(f'{randomMember.mention} drog det kortaste strået!')

    if message.content == "?Hjälp":
        await message.channel.send(f" **Botten lyssnar på följande kommandon:** \n "
                                   f"**?Schema** - Få aktuellt schema från Kronox \n "
                                   f"**?Utbildningsplan** - Skriver ut utbildningsplan för IA start 2020 \n "
                                   f"**?Zoom** - Få zoomlänkar till nuvarande kurser \n "
                                   f"**?Vem** - När man inte kan bestämma sig för vem som ska göra något")


bot.run(DISCORD_TOKEN)