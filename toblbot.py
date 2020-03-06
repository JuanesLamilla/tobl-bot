import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound


client = commands.Bot(command_prefix = '$')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Command not found.")
        return
    raise error

@client.event
async def on_guild_join(guild):
    general = guild.text_channels[0]
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}! I am the TOBL Bot!\nFor info on how to use me, try out $help. If you have any questions, comments, or suggestions, hit up @KiT#0004.'.format(guild.name))

@client.command()
async def standings(ctx):
    embed=discord.Embed(title="Current Standings", color=0xf3e91d)
    embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")
    embed.add_field(name="1. Onibaku", value="W: 0 L: 0 D: 0 Diff: +0", inline=False)
    embed.add_field(name="2. Cronchers of Catan", value="W: 0 L: 0 D: 0 Diff: +0", inline=False)
    embed.add_field(name="3. Game Hive", value="W: 0 L: 0 D: 0 Diff: +0", inline=False)
    embed.add_field(name="4. Finer Things Club", value="W: 0 L: 0 D: 0 Diff: +0", inline=False)
    embed.add_field(name="5. Everything Hurts", value="W: 0 L: 0 D: 0 Diff: +0", inline=False)
    embed.add_field(name="6. Stacy's Moms", value="W: 0 L: 0 D: 0 Diff: +0", inline=False)
    embed.add_field(name="7. Fewbisoft", value="W: 0 L: 0 D: 0 Diff: +0", inline=False)
    embed.add_field(name="8. Nerf Mei", value="W: 0 L: 0 D: 0 Diff: +0", inline=False)
    embed.set_footer(text="Last updated March 5th, 2020 at 7:13 pm.")
    await ctx.send(embed=embed)

@client.command()
async def KIT(ctx):
    await ctx.send("KAT!")

@client.command()
async def maps(ctx):
    embed=discord.Embed(title="TOBL Maps", color=0xf3e91d)
    embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")
    embed.add_field(name="March 15th, 2020", value="Lijiang Tower, King's Row, Volskaya Industries, Junkertown, Busan", inline=True)
    embed.add_field(name="March 22nd, 2020", value="Dorado, Oasis, Hollywood, Temple of Anubis, Watchpoint: Gilbraltar", inline=True)
    embed.add_field(name="March 29th, 2020", value="Eichenwalde, Horizon Lunar Colony, Nepal, Numbani, Route 66", inline=True)
    embed.add_field(name="April 5th, 2020", value="Ilios, Havana, Hanamura, King's Row, Lijiang Tower", inline=True)
    embed.add_field(name="April 26th, 2020", value="Rialto, Blizzard World, Busan, Paris, Dorado", inline=True)
    embed.add_field(name="May 3rd, 2020", value="Numbani, Volskaya Industries, Watchpoint: Gilbraltar, Eichenwalde, Oasis", inline=True)
    embed.add_field(name="May 10th, 2020", value="Nepal, Route 66, Temple of Anubis, Hollywood, Ilios", inline=True)
    embed.add_field(name="May 24th, 2020", value="Maps TBA", inline=True)
    embed.add_field(name="May 31st, 2020", value="Maps TBA", inline=True)
    embed.add_field(name="June 7th, 2020", value="Maps TBA", inline=True)
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def help(ctx):
    embed=discord.Embed(title="HELP", description="The following commands are available to all users. TOBL bot made by @KiT#0004.", color=0xf3e91d)
    embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")
    embed.add_field(name="$schedule", value="View all upcoming games.", inline=True)
    embed.add_field(name="$maps", value="View map pool for each weekend.", inline=True)
    embed.add_field(name="$standings", value="View current standings.", inline=True)
    embed.add_field(name="$upcoming", value="View this weekends matches / map pool", inline=True)
    embed.add_field(name="$stats", value="Coming soon ;)", inline=True)
    embed.set_footer(text="More features are on the way!")
    await ctx.send(embed=embed)

@client.command()
async def stats(ctx):
    await ctx.send("Game statistics coming soon.")

@client.command()
async def upcoming(ctx):
    embed=discord.Embed(title="Matches for March 15th", description="Games this upcoming weekend.", color=0xf3e91d)
    embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")
    embed.add_field(name="Maps", value=" Lijiang Tower, King's Row, Volskaya Industries, Junkertown, Busan", inline=False)
    embed.add_field(name="Matches", value="2:00pm (login @ 1:45pm) - Cronchers of Catan vs. Game Hive\n\
                                            4:00pm (login @ 3:45pm) - Finer Things Club vs. Everything Hurts\n\
                                            6:00pm (login @ 5:45pm) - Onibaku vs. Stacy's Moms\n\
                                            8:00pm (login @ 7:45pm) - Fewbisoft vs. Nerf Mei", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def schedule(ctx):
    embed=discord.Embed(title="Schedule", description="Complete league schedule.", color=0xf3e91d)
    embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")
    embed.add_field(name="March 15th, 2020", value="2:00pm (login @ 1:45pm) - Cronchers of Catan vs. Game Hive\n\
                                            4:00pm (login @ 3:45pm) - Finer Things Club vs. Everything Hurts\n\
                                            6:00pm (login @ 5:45pm) - Onibaku vs. Stacy's Moms\n\
                                            8:00pm (login @ 7:45pm) - Fewbisoft vs. Nerf Mei", inline=False)
    embed.add_field(name="March 22nd, 2020", value="2:00pm (login @ 1:45pm) - Fewbisoft vs. Everything Hurts\n\
                                            4:00pm (login @ 3:45pm) - Stacy's Moms vs. Game Hive\n\
                                            6:00pm (login @ 5:45pm) - Cronchers of Catan vs. Nerf Mei\n\
                                            8:00pm (login @ 7:45pm) - Onibaku vs. Finer Things Club", inline=False)
    embed.add_field(name="March 29th, 2020", value="2:00pm (login @ 1:45pm) - Onibaku vs. Game Hive\n\
                                            4:00pm (login @ 3:45pm) - Nerf Mei vs. Everything Hurts\n\
                                            6:00pm (login @ 5:45pm) - Finer Things Club vs. Fewbisoft\n\
                                            8:00pm (login @ 7:45pm) - Cronchers of Catan vs. Stacy's Moms", inline=False)
    embed.add_field(name="April 5th, 2020", value="2:00pm (login @ 1:45pm) - Fewbisoft vs. Stacy's Moms\n\
                                            4:00pm (login @ 3:45pm) - Finer Things Club vs. Cronchers of Catan\n\
                                            6:00pm (login @ 5:45pm) - Nerf Mei vs. Onibaku\n\
                                            8:00pm (login @ 7:45pm) - Everything Hurts vs. Game Hive", inline=False)
    embed.add_field(name="April 26th, 2020", value="2:00pm (login @ 1:45pm) - Everything Hurts vs. Onibaku\n\
                                            4:00pm (login @ 3:45pm) - Game Hive vs. Nerf Mei\n\
                                            6:00pm (login @ 5:45pm) - Fewbisoft vs. Cronchers of Catan\n\
                                            8:00pm (login @ 7:45pm) - Finer Things Club vs. Stacy's Moms", inline=False)
    embed.add_field(name="May 3rd, 2020", value="2:00pm (login @ 1:45pm) - Finer Things Club vs. Nerf Mei\n\
                                            4:00pm (login @ 3:45pm) - Cronchers of Catan vs. Onibaku\n\
                                            6:00pm (login @ 5:45pm) - Stacy's Moms vs. Everything Hurts\n\
                                            8:00pm (login @ 7:45pm) - Fewbisoft vs. Game Hive", inline=False)
    embed.add_field(name="May 10th, 2020", value="2:00pm (login @ 1:45pm) - Stacy's Moms vs. Nerf Mei\n\
                                            4:00pm (login @ 3:45pm) - Finer Things Club vs. Game Hive\n\
                                            6:00pm (login @ 5:45pm) - Fewbisoft vs. Onibaku\n\
                                            8:00pm (login @ 7:45pm) - Cronchers of Catan vs. Everything Hurts", inline=False)
    embed.add_field(name="May 24th, 2020, 2020", value="TBA", inline=False)
    embed.add_field(name="May 31st, 2020", value="TBA", inline=False)
    embed.add_field(name="June 7th, 2020", value="TBA", inline=False)       
    await ctx.send(embed=embed)

client.run('Njg1MTg5OTA3OTQwOTAwODY5.XmFFGA.5Rg5_RrWeboBw9LQ6XGWNbf8BL8')