import discord
import csv
import pathlib
from stattracker import team, player, map_round, match, Hero
from discord.ext import commands
from discord.ext.commands import CommandNotFound

teams = []
players = []
matches = []
last_updated = "Last updated March 13th, 2020 at 7:22 pm."

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
    embed.set_footer(text=last_updated)
    await ctx.send(embed=embed)

@client.command(case_insensitive=True)
async def kit(ctx):
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
    embed.add_field(name="May 24th, 2020", value="TBA", inline=False)
    embed.add_field(name="May 31st, 2020", value="TBA", inline=False)
    embed.add_field(name="June 7th, 2020", value="TBA", inline=False)       
    await ctx.send(embed=embed)

@client.command()
async def team_playtime(ctx, team_name=None):
    if team_name is None:
        await ctx.send("Missing argument: Team Name\n(ex: '$stats_player StacysMoms')")
        return

    total_time = 0
    reaper = Hero("Reaper", "<:reaper:688453731850911750>")
    tracer = Hero("Tracer", "<:tracer:688453731850911750>")
    mercy = Hero("Mercy", "<:mercy:688453731850911750>")
    hanzo = Hero("Hanzo", "<:hanzo:688453731850911750>")
    torbjorn = Hero("Torbjorn", "<:torbjorn:688453731850911750>")
    reinhardt = Hero("Reinhardt", "<:reinhardt:688453731850911750>")
    pharah = Hero("Pharah", "<:pharah:688453731850911750>")
    winston = Hero("Winston", "<:winston:688453731850911750>")
    widowmaker = Hero("Widowmaker", "<:widowmaker:688453731850911750>")
    bastion = Hero("Bastion", "<:bastion:688453731850911750>")
    symmetra = Hero("Symmetre", "<:symmetra:688453731850911750>")
    zenyatta = Hero("Zenyatta", "<:zenyatta:688453731850911750>")
    genji = Hero("Genji", "<:genji:688453731850911750>")
    roadhog = Hero("Roadhog", "<:roadhog:688453731850911750>")
    mccree = Hero("McCree", "<:mccree:688453731850911750>")
    junkrat = Hero("Junkrat", "<:junkrat:688453731850911750>")
    zarya = Hero("Zarya", "<:zarya:688453731850911750>")
    soldier = Hero("Soldier", "<:soldier:688453731850911750>")
    lucio = Hero("Lucio", "<:lucio:688453731850911750>")
    dva = Hero("D.Va", "<:dva:688453731850911750>")
    mei = Hero("Mei", "<:mei:688453731850911750>")
    sombra = Hero("Sombra", "<:sombra:688453731850911750>")
    doomfist = Hero("Doomfist", "<:doomfist:688453731850911750>")
    ana = Hero("Ana", "<:ana:688453731850911750>")
    orisa = Hero("Orisa", "<:orisa:688453731850911750>")
    brigitte = Hero("Brigitte", "<:brigitte:688453731850911750>")
    moira = Hero("Moira", "<:moira:688453731850911750>")
    wrecking_ball = Hero("Wrecking Ball", "<:wrecking_ball:688453731850911750>")
    ashe = Hero("Ashe", "<:ashe:688453731850911750>")
    baptiste = Hero("Baptiste", "<:baptiste:688453731850911750>")
    sigma = Hero("Sigma", "<:sigma:688453731850911750>")

    all_heroes = [ana, ashe, bastion, brigitte, dva, doomfist, genji, hanzo, junkrat, lucio, mccree,
     mei, mercy, moira, orisa, pharah, reaper, reinhardt, roadhog, soldier, sombra, symmetra, torbjorn,
     tracer, widowmaker, winston, wrecking_ball, zarya, zenyatta]
    
    for t in teams:
        if team_name.lower().replace("'", "") == t.name.lower().replace("'", "").replace(" ", ""):
            for k in t.playrate_data.keys():
                for elem in t.playrate_data[k]:
                    total_time.time += elem[31]
                    reaper.time += elem[0]
                    tracer.time += elem[1]
                    mercy.time += elem[2]
                    hanzo.time += elem[3]
                    torbjorn.time += elem[4]
                    reinhardt.time += elem[5]
                    pharah.time += elem[6]
                    winston.time += elem[7]
                    widowmaker.time += elem[8]
                    bastion.time += elem[9]
                    symmetra.time += elem[10]
                    zenyatta.time += elem[11]
                    genji.time += elem[12]
                    roadhog.time += elem[13]
                    mccree.time += elem[14]
                    junkrat.time += elem[15]
                    zarya.time += elem[16]
                    soldier.time += elem[17]
                    lucio.time += elem[18]
                    dva.time += elem[19]
                    mei.time += elem[20]
                    sombra.time += elem[21]
                    doomfist.time += elem[22]
                    ana.time += elem[23]
                    orisa.time += elem[24]
                    brigitte.time += elem[25]
                    moira.time += elem[26]
                    wrecking_ball.time += elem[27]
                    ashe.time += elem[28]
                    baptiste.time += elem[29]
                    sigma.time += elem[30]


            embed=discord.Embed(title="Hero playtime for  " + t.name, description="", color=0xf3e91d)
            embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")
            for hero in all_heroes:
                embed.add_field(name=hero.emote + " " + hero.name, value="{0:.1f}".format((hero.time / total_time) * 100), inline=True)
            embed.set_footer(text=last_updated)
            await ctx.send(embed=embed)
            return
    
    await ctx.send("Unable to find team with name: " + team_name + "\nRemember to omit spaces ('Stacy's Moms' -> 'Stacy'sMoms')")

@client.command()
async def stats_player(ctx, name=None):
    if name is None:
        await ctx.send("Missing argument: Player Name\n(ex: '$stats_player Krusher99')")
        return

    for p in players:
        if p.name.lower() == name.lower():
            #Time Played
            temp_minutes = p.total_playtime // 60
            hours = str(temp_minutes // 60)
            minutes = str(temp_minutes % 60)

            total_maps = 0
            total_elims = 0
            total_final_blows = 0
            total_deaths = 0
            total_damage_dealt = 0
            total_healing_dealt = 0
            total_damage_taken = 0
            total_healing_taken = 0
            total_ults_used = 0
            total_crouches = 0
            for k in p.map_data.keys():
                           
                #Maps Played
                if p.map_data[k] != []:
                    total_maps += len(p.map_data[k])
                
                #{60; 22; 21; 15117.47; 0; 15793.74; 6543.80; 7}
                for elem in p.map_data[k]:
                    total_elims += int(elem[0])
                    total_final_blows += int(elem[1])
                    total_deaths += int(elem[2])
                    total_damage_dealt += float(elem[3])
                    total_healing_dealt += float(elem[4])
                    total_damage_taken += float(elem[5])
                    total_healing_taken += float(elem[6])
                    total_ults_used += int(elem[7])
                    total_crouches += int(elem[8])
            


            embed=discord.Embed(title="Stats for " + p.name + " (" + p.team.name + ")", description=p.name + " has played for a total of " + hours + " hours and " + minutes + " minutes across " + str(total_maps) + " map(s).", color=0xf3e91d)
            embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")
            embed.add_field(name="Eliminations", value="Total: " + str(total_elims) + "\nAvg/10mins: " + "{0:.2f}".format(total_elims*(10/temp_minutes)), inline=True)
            embed.add_field(name="Final Blows", value="Total: " + str(total_final_blows) + "\nAvg/10mins: " + "{0:.2f}".format(total_final_blows*(10/temp_minutes)), inline=True)
            embed.add_field(name="Deaths", value="Total: " + str(total_deaths) + "\nAvg/10mins: " + "{0:.2f}".format(total_deaths*(10/temp_minutes)), inline=True)
            embed.add_field(name="Damage Dealt", value="Total: " + str(total_damage_dealt) + "\nAvg/10mins: " + "{0:.2f}".format(total_damage_dealt*(10/temp_minutes)), inline=True)
            embed.add_field(name="Healing Dealt", value="Total: " + str(total_healing_dealt) + "\nAvg/10mins: " + "{0:.2f}".format(total_healing_dealt*(10/temp_minutes)), inline=True)
            embed.add_field(name="Damage Received", value="Total: " + str(total_damage_taken) + "\nAvg/10mins: " + "{0:.2f}".format(total_damage_taken*(10/temp_minutes)), inline=True)
            embed.add_field(name="Healing Received", value="Total: " + str(total_healing_taken) + "\nAvg/10mins: " + "{0:.2f}".format(total_healing_taken*(10/temp_minutes)), inline=True)
            embed.add_field(name="Ults Used", value="Total: " + str(total_ults_used) + "\nAvg/10mins: " + "{0:.2f}".format(total_ults_used*(10/temp_minutes)), inline=True)
            embed.add_field(name="Tactical Crouches", value="Total: " + str(total_crouches) + "\nAvg/10mins: " + "{0:.2f}".format(total_crouches*(10/temp_minutes)), inline=True)
            embed.set_footer(text=last_updated)
            await ctx.send(embed=embed)
            return
    
    await ctx.send("Unable to find player with name: " + name)

def scan_data():
    with open(str(pathlib.Path(__file__).parent.absolute()) + "\\teams.txt", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, skipinitialspace=True, delimiter=',')
        for row in csv_reader:
            curr_team = team(row[0])
            for name in row[1:]:
                curr_player = player(name, curr_team)
                players.append(curr_player)
                curr_team.players.append(curr_player)
            teams.append(curr_team)


    with open(str(pathlib.Path(__file__).parent.absolute()) + "\\stats.txt", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, skipinitialspace=True, delimiter=',')
        for row in csv_reader:

            if row[0] == "GAME":
                for t in teams:
                    if t.name == row[2]:
                        temp_team_1 = t
                    elif t.name == row[3]:
                        temp_team_2 = t
                match_save = match((temp_team_1, temp_team_2), (int(row[4]), int(row[5])), int(row[1]))

            elif len(row) != 142:
                raise ValueError("Invalid map input")

            else:
            
                current_round = map_round(row[16])

                for x in range(12):
                    player_stats = row[x + 19].replace("{", "").replace("}", "").replace(" ", "").split(";")
                    current_round.player_dict[row[x]] = player_stats

                    while len(player_stats) < 9:
                        player_stats.append(0)

                    for y in players:
                        if y.name == row[x]:
                            y.map_data[match_save.week].append(player_stats)
                            y.playtime[match_save.week].append(int(row[17]))
                            y.total_playtime += int(row[17])
                    

                temp_playtime = [int(i.replace(" ", "")) for i in row[31].replace("{", "").replace("}", "").split(";")]
                while len(temp_playtime) < 31:
                    temp_playtime.append(0)
                temp_playtime.append(int(row[17]))
                current_round.hero_playtime_1 = temp_playtime
                match_save.teams[0].playrate_data[match_save.week].append(temp_playtime)

                temp_playtime = [int(i.replace(" ", "")) for i in row[32].replace("{", "").replace("}", "").split(";")]
                while len(temp_playtime) < 31:
                    temp_playtime.append(0)
                temp_playtime.append(int(row[17]))
                current_round.hero_playtime_2 = temp_playtime
                match_save.teams[1].playrate_data[match_save.week].append(temp_playtime)

                current_round.map_time = int(row[17])

                match_save.maps.append(current_round)
                matches.append(match_save)

scan_data()
client.run('Njg1MTg5OTA3OTQwOTAwODY5.XmFFGA.5Rg5_RrWeboBw9LQ6XGWNbf8BL8')