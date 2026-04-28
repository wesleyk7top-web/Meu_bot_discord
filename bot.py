import discord
from discord.ext import commands
import aiohttp
import json

TOKEN = "SEU_TOKEN_AQUI"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")

@bot.command()
async def criar(ctx):
    try:
        # Ler JSON
        with open("AccountConfiguration.json") as f:
            data = json.load(f)

        uid = data["uid"]
        password = data["password"]

        await ctx.send("⏳ Criando sala...")

        url = "http://127.0.0.1:5000/create-room"
        payload = {
            "uid": uid,
            "password": password
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:

                if response.status == 200:
                    await ctx.send("✅ Sala criada com sucesso!")
                else:
                    error = await response.text()
                    await ctx.send(f"❌ Erro: {error}")

    except Exception as e:
        await ctx.send(f"Erro: {e}")

bot.run(TOKEN)
