import discord
from discord.ext import commands
import asyncio

client = discord.Client()
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print("♥ Ready (っ◔◡◔)っ")
    await client.change_presence(game=discord.Game(name="Find me @ giannhsgg"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #Arxh commands
    if message.content == "help":
            await client.send_message(message.channel, "▷ Try again by typing 'commands'\n \n IMPORTANT: Every command you wannto type gotta be with lowercase letters. \n Otherwise it may not work properly.")
    if message.content == "commands":
            await client.send_message(message.channel, "▷ Available commands :\n (Type lowercase letters)\n ▹ Instagram\n ▹ Facebook\n ▹ Messeger\n ▹ Youtube\n ▹ Tumblr\n ▹ SocialMedia\n ▹ Brisies \n \n *Type 'help' if you need something*")
    #Telos commands
    #Social Media mou
    if message.content == "instagram":
        await client.send_message(message.channel, "@giannhsgg on instagramo bitcho")
    if message.content == "facebook":
        await client.send_message(message.channel, "@giannhsgg on facebooko bitcho")
    if message.content == "messenger":
        await client.send_message(message.channel, "@giannhsgg on messegero bitcho")
    if message.content == "tumblr":
        await client.send_message(message.channel, "@giannhsgg on tumblero bitcho")        
    if message.content == "youtube":
        await client.send_message(message.channel, "MAYBE CallMe Johnny on youtubeo bitcho")
    if message.content == "socialmedia":
        await client.send_message(message.channel, "USUALLY @giannhsgg NIGGA")
    #Telos Social media
    #Arxi apo vrisies
    if message.content == "brisies":
            await client.send_message(message.channel, "\n Available commands :\n ✵ rebas \n ✵ puta \n ✵ pizda \n ✵ malaka \n ✵ pousth \n ✵ gamimene \n ✵ kurwa")
    if message.content == "rebas":
        await client.send_message(message.channel, "⫸⫸⫸Re bas & mas douleveis?⫷⫷⫷")
    if message.content == "puta":
        await client.send_message(message.channel, "eisai kai fenesai vlaka!")
    if message.content == "pizda":
        await client.send_message(message.channel, "sou to gamaw, skase!")
    if message.content == "malaka":
        await client.send_message(message.channel, "esu eisai o megaliteros malakas, apla pliroforiaka..")
    if message.content == "pousth":
        await client.send_message(message.channel, "esu pousth skase...")
    if message.content == "gamimene":
        await client.send_message(message.channel, "se exw gamisei kai giauto kles. Gia hrema")
    if message.content == "kurwa":
        await client.send_message(message.channel, "eisai ultimate kathisterimenos")

        
@client.event
async def on_message(message):
    if message.content == "$flex":
        await client.delete_message(message)
        await client.send_message(member, ":heart: :eggplant: :peach:")
        
client.run('NTUzOTczMzY3OTU1MjU5NDMz.D31rKw.F5qLGDjWlVy0RGAO_5eFT-U5sWY')


