import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = cycle(['E ora pess', 'Bota uma jiga', 'Não me apetece dar a jiga', 'Hacieee'])

@client.event
async def on_ready():
    '''await client.change_presence(status=discord.Status.idle, activity=discord.Game('E ora pessoal'))'''
    change_status.start()
    print('O bot está pronto.')

@client.event
async def on_member_join(member):
    print(f'E oringz {member} acabaste de te juntar aos DefeczZ.')

@client.event
async def on_member_remove(member):
    print(f'Hacieee {member}')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def lema(ctx):
    await ctx.send('Haciehaciemastrelugsdadugsdugsda')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['É o mais certo.',
                 'Tás chato.',
                 'Não percebi, podes repetir?',
                 'Adegz',
                 'Ah yepz',
                 'Ah de nuapz',
                 'Se calhar sim, se calhar não, sabão não é de certeza',
                 'O que é que isso importa, o Paulo tá de chamadz',
                 'Não vou responder a isso, tás burro',
                 'Calma, tou num comp já te digo',
                 'Vocês são fodidos ahahah',
                 'Quem me dera saber responder a isso, sou apenas um bot :(',
                 '27',
                 'Já chega de perguntas',
                 'Cala-te']
    await ctx.send(f'Pergunta: {question}\nResposta: {random.choice(responses)}')

@client.command(aliases=['defecz'])
async def _defecz(ctx):
    responses = ['Haaaacie',
                 'Strelinquinz',
                 'Strelinquinquinz',
                 'Adeeeeeegz',
                 'Ah yeeeepz',
                 'Ah de nuapz',
                 'Juro pê lá morté dé mi madré']
    await ctx.send(f'{random.choice(responses)}')

'''
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)




'''
'''
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'É só um kickzinho amanhã voltas parceiro {user.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Xauzinho para sempre parsona {user.mention}')
'''

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Vê lá se não és banido outra vez {user.mention}')
            return

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@tasks.loop(seconds=4)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Não sei o que fazer com isso, pede ao Gui Mart para me acrescentar isso. Agora cala-te!')

@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Diz quantas queres apagar não?')







client.run('Njk1NzA5NjI4NjE2NDA5MTA4.XoeIXg.67ZOhUQpe_Qqn8klx1JE1rz3n7M')
