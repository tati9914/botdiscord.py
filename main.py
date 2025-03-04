
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'BIENVENIDO! TE HAS CONECTADO Y EL BOT ESTA FUNCIONANDO {bot.user}')

@bot.command('hola')
async def hola(ctx):
    await ctx.send('Hola soy el bot de discord, en q l@ asist@')

@bot.command('aleatorio')
async def aleatorio(ctx, minimo:int, maximo:int):
    num=random.randint(minimo,maximo)
    texto='el numero generado es: '+ str(num)
    await ctx.send(texto)

@bot.command('gen_pass')
async def gen_pass(ctx,pass_length:int):
    elements = "+-/*!&$#?=@<>"
    password = ""

@bot.command('frase')
async def frase (ctx):
    citas = [
        "La vida es 10% lo que te sucede y 90% cómo reaccionas a ello. – Charles R. Swindoll",
        "El único modo de hacer un gran trabajo es amar lo que haces. – Steve Jobs",
        "El futuro pertenece a aquellos que creen en la belleza de sus sueños. – Eleanor Roosevelt",
        "No se trata de si van a derribarte, se trata de si vas a levantarte cuando lo hagan» —Vince Lombardi"
    ]
    cita = random.choice(citas)
    await ctx.send(f"Cita inspiradora: {cita}")

@bot.command('broma')
async def broma(ctx):
    chistes = [
        "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
        "¿Por qué el libro de matemáticas está estresado? Porque tenía demasiados problemas.",
        "¿Cuál es el café más peligroso del mundo? El ex-preso."
    ]
    chiste = random.choice(chistes)
    await ctx.send(f"Chiste: {chiste}")
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
