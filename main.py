import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

# Cargar las variables de entorno
load_dotenv()

# Obtener el token
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Inicio con el Bot {bot.user.name}, listo!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

#AL ENTRAR AL SERVIDOR
@bot.event
async def on_member_join(member):
    canal_bienvenida = discord.utils.get(member.guild.text_channels, name='bienvenidas')
    if canal_bienvenida:
        await canal_bienvenida.send(f'¡HOLAAA, {member.mention} BIENVENIDO AL SERVIDOR {member.guild.name}!Nos alegra tenerte aquí.')

#AL SALIR DEL SERVIDOR  
@bot.event
async def on_member_remove(member):
    canal_bienvenida = discord.utils.get(member.guild.text_channels, name='bienvenidas')#INV 
    if canal_bienvenida:
        await canal_bienvenida.send(f'¡Oh, no {member.mention} acaba de abandonar el servidor {member.guild.name}. Siempre te recordaremos!')

# COMANDO !HOLA
@bot.event
async def hola(ctx):
    await ctx.send(f'Hola {ctx.author.mention}, mi nombre es {bot.user.name}')


# COMANDO !DADO
@bot.command()
async def dado(ctx, caras: int = 6):
    if caras < 2:
        await ctx.send("❌ El dado debe tener al menos 2 caras")
        return
    resultado = random.randint(1, caras)
    await ctx.send(f"🎲 {ctx.author.mention} tiró un dado de **{caras}** caras: **{resultado}**")

# COMANDO !MONEDA
@bot.command()
async def moneda(ctx):
    resultado = random.choice(["Cara 👑", "Cruz ⚔️"])
    await ctx.send(f" {ctx.author.mention} lanzó una moneda y su resultado es: **{resultado}**")

# COMANDO !CARIÑO
@bot.command()
async def cariño(ctx, miembro: discord.Member = None):
    if miembro is None:
        await ctx.send("❌ Debes mencionar a alguien para abrazar")
        return
    
    if miembro == ctx.author:
        await ctx.send("Se dió un fuerte abrazo en soledad...")
        return
    
    mensajes = [
        f"🤗 {ctx.author.mention} abrazó fuertemente a {miembro.mention}",
        f"💕 {ctx.author.mention} beso a {miembro.mention} con musho cariño!",
        f"❤️ {ctx.author.mention} carga a {miembro.mention} con delicadeza",
        f"❤️ {ctx.author.mention} le da un besito a {miembro.mention} en la mejilla.",
        f"{ctx.author.mention} hizo que {miembro.mention} se sonrojara💕",
        f"💕{ctx.author.mention} se sonrojó al pensar en {miembro.mention}💕"
    ]
    
    await ctx.send(random.choice(mensajes))

# COMANDO !ODIO
@bot.command()
async def odio(ctx, miembro: discord.Member = None):
    if miembro is None:
        await ctx.send(f"{ctx.author.mention} debes mencionar a alguien para odiar.")
        return
    
    if miembro == ctx.author:
        await ctx.send(f"{ctx.author.mention} Se odia a si mismo...")
        return
    
    mensajes = [
        f"💔 {ctx.author.mention} odia profundamente a {miembro.mention}",
        f"😡 {ctx.author.mention} detesta a {miembro.mention} con toda su alma!",
        f"🔥 {ctx.author.mention} espera que se quemen los focos de la casa de {miembro.mention}",
        f"⚡ {ctx.author.mention} mira a {miembro.mention} y se irrita.",
        f"🌪️ {ctx.author.mention} zarandea a {miembro.mention}!",
        f"{ctx.author.mention} quiere tirarle una roca a {miembro.mention}"
    ]
    
    await ctx.send(random.choice(mensajes))

# COMANDO !CHISTE
@bot.command()
async def chiste(ctx):
    chistes = [
        "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
        "¿Qué le dijo una pared a la otra? Nos vemos en la esquina.",
        "¿Cuál es el colmo de un electricista? Que le dé miedo la oscuridad.",
        "¿Por qué los esqueletos no pelean entre ellos? Porque no tienen agallas.",
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "¿Por qué el libro de matemáticas estaba triste? Porque tenía muchos problemas."
    ]
    
    await ctx.send(random.choice(chistes))
#COMANDO !8BALL
responses = ["Sí", "No", "Tal vez.", "¿Es broma? Obvio no.", "Definitivamente si.", "Si tu no sabes, menos yo."]

@bot.command(name="8ball")
async def eightball(ctx, *, question: str = None):
    if not question:
        await ctx.send("¿Y la pregunta❓ Uso: `!8ball ¿Me irá bien?`")
        return

    respuesta = random.choice(responses)
    await ctx.send(f"🎱 {respuesta}")

# Ejecutar el bot
bot.run(TOKEN)
