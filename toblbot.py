import discord
import csv
import pathlib
from stattracker import team, player, map_round, match, Hero
from discord.ext import commands
from discord.ext.commands import CommandNotFound

teams = []
players = []
matches = []
last_updated = "Last updated May 25th, 2020 at 8:34 am."

client = commands.Bot(command_prefix = '!') # $ for live
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

    embed.add_field(name="1. Game Hive", value="W: 20 L: 7 Diff: +13", inline=False) # Wins: 6
    embed.add_field(name="2. Fewbisoft", value="W: 20 L: 9 Diff: +11", inline=False) # Wins: 6
    embed.add_field(name="3. Everything Hurts", value="W: 16 L: 11 Diff: +5", inline=False) # Wins: 5

    embed.add_field(name="4. Cronchers of Catan", value="W: 10 L: 14 Diff: -4", inline=False) # Wins: 3

    embed.add_field(name="5. Stacy's Moms", value="W: 11 L: 16 Diff: -5", inline=False) # Wins: 2
    embed.add_field(name="6. Onibaku", value="W: 11 L: 17 Diff: -6", inline=False) # Wins: 2

    embed.add_field(name="7. Nerf Mei", value="W: 11 L: 18 Diff: -7", inline=False) # Wins: 2

    embed.add_field(name="8. Finer Things Club", value="W: 11 L: 18 Diff: -7", inline=False) # Wins: 2

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
    embed.add_field(name="March 29th, 2020", value="Dorado, Oasis, Hollywood, Temple of Anubis, Watchpoint: Gilbraltar", inline=True)
    embed.add_field(name="April 5th, 2020", value="Eichenwalde, Horizon Lunar Colony, Nepal, Numbani, Route 66", inline=True)
    embed.add_field(name="April 19th, 2020", value="Ilios, Havana, Hanamura, King's Row, Lijiang Tower", inline=True)
    embed.add_field(name="April 26th, 2020", value="Rialto, Blizzard World, Busan, Paris, Dorado", inline=True)
    embed.add_field(name="May 3rd, 2020", value="Numbani, Volskaya Industries, Watchpoint: Gilbraltar, Eichenwalde, Oasis", inline=True)
    embed.add_field(name="May 10th, 2020", value="Nepal, Route 66, Temple of Anubis, Hollywood, Ilios", inline=True)
    embed.add_field(name="May 24th, 2020", value="2:00pm and 4:00pm: Nepal, Hollywood, Volskaya, Route 66, Ilios (Contingency Map = Junkertown)\n\
                                        6:00pm and 8:00pm: Ilios, Route 66, Volskaya, Hollywood, Nepal (Contingency Map = Junkertown)", inline=True)
    embed.add_field(name="May 31st, 2020", value="4:00pm and 6:00pm: Dorado, Oasis, Temple of Anubis, Eichenwalde, Havana (Contingency Map = Lijiang Tower)", inline=True)
    embed.add_field(name="June 7th, 2020", value="Lijiang Tower, King’s Row, Watchpoint: Gibraltar, Hanamura, Busan, Numbani, Rialto (Contingency Map = Oasis)", inline=True)
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def help(ctx):
    embed=discord.Embed(title="HELP", description="The following commands are available to all users. TOBL bot made by @KiT#0004.", color=0xf3e91d)
    embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")
    embed.add_field(name="$schedule", value="View all upcoming games.", inline=True)
    embed.add_field(name="$maps", value="View map pool for each weekend.", inline=True)
    embed.add_field(name="$standings", value="View current standings.", inline=True)
    embed.add_field(name="$upcoming", value="View this weekends matches / map pool", inline=True)
    embed.add_field(name="$stats", value="View stats for specific player\n(ex: $stats Krusher99)", inline=True)
    embed.add_field(name="$playtime", value="View hero playtime per team\n(ex: $playtime StacysMoms)\nUse 'all' to view playtime across entire league.", inline=False)
    embed.add_field(name="$top10", value="View top 10 players for specific stat\n(ex: $top10 finalblows)", inline=True)
    embed.set_footer(text="More features are on the way!")
    await ctx.send(embed=embed)

@client.command()
async def upcoming(ctx):
    embed=discord.Embed(title="Matches for May 31st (PLAYOFFS!!)", description="Next upcoming games.", color=0xf3e91d)
    embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")
    embed.add_field(name="Maps", value="4:00pm and 6:00pm: Dorado, Oasis, Temple of Anubis, Eichenwalde, Havana (Contingency Map = Lijiang Tower)", inline=False)
    embed.add_field(name="Matches", value="4:00pm . The highest seed winner from May 24th will play the 2nd seed.\n\
                                            6:00pm . The lowest seed winner from May 24th will play the 1st seed.", inline=False)
    embed.set_footer(text=last_updated)
    await ctx.send(embed=embed)

@client.command()
async def schedule(ctx):
    embed=discord.Embed(title="Schedule", description="Complete league schedule.", color=0xf3e91d)
    embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")
    embed.add_field(name="March 15th, 2020", value="2:00pm (login @ 1:45pm) - Cronchers of Catan vs. Game Hive\n\
                                            4:00pm (login @ 3:45pm) - Finer Things Club vs. Everything Hurts\n\
                                            6:00pm (login @ 5:45pm) - Onibaku vs. Stacy's Moms\n\
                                            8:00pm (login @ 7:45pm) - Fewbisoft vs. Nerf Mei", inline=False)
    embed.add_field(name="March 29nd, 2020", value="2:00pm (login @ 1:45pm) - Fewbisoft vs. Everything Hurts\n\
                                            4:00pm (login @ 3:45pm) - Stacy's Moms vs. Game Hive\n\
                                            6:00pm (login @ 5:45pm) - Cronchers of Catan vs. Nerf Mei\n\
                                            8:00pm (login @ 7:45pm) - Onibaku vs. Finer Things Club", inline=False)
    embed.add_field(name="April 5th, 2020", value="2:00pm (login @ 1:45pm) - Onibaku vs. Game Hive\n\
                                            4:00pm (login @ 3:45pm) - Nerf Mei vs. Everything Hurts\n\
                                            6:00pm (login @ 5:45pm) - Finer Things Club vs. Fewbisoft\n\
                                            8:00pm (login @ 7:45pm) - Cronchers of Catan vs. Stacy's Moms", inline=False)
    embed.add_field(name="April 19th, 2020", value="2:00pm (login @ 1:45pm) - Fewbisoft vs. Stacy's Moms\n\
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
    embed.add_field(name="May 24th, 2020", value="2:00pm . The 5th place seed will play the 8th place seed.\n\
                                            4:00pm . The 6th place seed will play the 7th place seed.\n\
                                            6:00pm . The winner of the 2:00pm match (5th vs. 8th) will play the 4th seed.\n\
                                            8:00pm . The winner of the 4:00pm match (6th vs. 7th) will play the 3rd seed.", inline=False)
    embed.add_field(name="May 31st, 2020", value="4:00pm . The highest seed winner from May 24th will play the 2nd seed.\n\
                                            6:00pm . The lowest seed winner from May 24th will play the 1st seed.", inline=False)
    embed.add_field(name="June 7th, 2020", value="4:00pm . Consolations Finals!\n\
                                            6:00pm . SEASON FIVE GRAND FINALS!", inline=False)       
    await ctx.send(embed=embed)

@client.command()
async def playtime(ctx, team_name=None, start=None, end=None):

    if not start is None and end is None:
        end = start

    total_time = 0
    echo_total_time = 0
    sigma_total_time = 0
    reaper = Hero("Reaper", "<:reaper:688453034317054051>")
    tracer = Hero("Tracer", "<:tracer:688453036506480726>")
    mercy = Hero("Mercy", "<:mercy:688453037001408534>")
    hanzo = Hero("Hanzo", "<:hanzo:688453035705237651>")
    torbjorn = Hero("Torbjorn", "<:torbjorn:688453036732973073>")
    reinhardt = Hero("Reinhardt", "<:reinhardt:688453036263473195>")
    pharah = Hero("Pharah", "<:pharah:688453035701043318>")
    winston = Hero("Winston", "<:winston:688453037085556955>")
    widowmaker = Hero("Widowmaker", "<:widowmaker:688453036355354675>")
    bastion = Hero("Bastion", "<:bastion:688453029028036722>")
    symmetra = Hero("Symmetra", "<:symmetra:688453036716195925>")
    zenyatta = Hero("Zenyatta", "<:zenyatta:688453036430852269>")
    genji = Hero("Genji", "<:genji:688453035219091490>")
    roadhog = Hero("Roadhog", "<:roadhog:688453036309348455>")
    mccree = Hero("McCree", "<:mccree:688453036347359263>")
    junkrat = Hero("Junkrat", "<:junkrat:688453036997214224>")
    zarya = Hero("Zarya", "<:zarya:688453036980305942>")
    soldier = Hero("Soldier", "<:soldier:688453036451954701>")
    lucio = Hero("Lucio", "<:lucio:688453037198540877>")
    dva = Hero("D.Va", "<:dva:688453035902500888>")
    mei = Hero("Mei", "<:mei:688453036284182724>")
    sombra = Hero("Sombra", "<:sombra:688453036007620611>")
    doomfist = Hero("Doomfist", "<:doomfist:688453033276735488>")
    ana = Hero("Ana", "<:ana:688453028411473925>")
    orisa = Hero("Orisa", "<:orisa:688453036221268056>")
    brigitte = Hero("Brigitte", "<:brigitte:688453032698052688>")
    moira = Hero("Moira", "<:moira:688453037152403486>")
    wrecking_ball = Hero("Wrecking Ball", "<:wrecking_ball:688453035072290816>")
    ashe = Hero("Ashe", "<:ashe:688453030324338782>")
    echo = Hero("Echo", "<:echo:706705092253974530>")
    echo.is_echo = True
    baptiste = Hero("Baptiste", "<:baptiste:688453019351908590>")
    sigma = Hero("Sigma", "<:sigma:688453035470356480>")

    all_heroes = [ana, ashe, baptiste, bastion, brigitte, dva, doomfist, echo, genji, hanzo, junkrat, lucio, mccree,
     mei, mercy, moira, orisa, pharah, reaper, reinhardt, roadhog, sigma, soldier, sombra, symmetra, torbjorn,
     tracer, widowmaker, winston, wrecking_ball, zarya, zenyatta]
    
    if team_name is None or team_name.lower().replace("'", "") == "all":
        for t in teams:

            for k in t.playrate_data.keys():
                if not end is None and (k > int(end) or k < int(start)):
                        continue    
                
                
                for elem in t.playrate_data[k]:   

                    
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

                    if k <= 3:
                        baptiste.time += elem[29]
                        sigma.time += elem[30]
                        sigma_total_time += elem[31]
                        total_time += elem[31]

                    elif k <= 6:
                        echo.time += elem[29]
                        baptiste.time += elem[30]
                        total_time += elem[31]
                    
                    else:
                        echo.time += elem[29]
                        baptiste.time += elem[30]
                        sigma.time += elem[31]
                        sigma_total_time += elem[32]
                        total_time += elem[32]

                    if k >= 5:
                        echo_total_time += elem[31]  

        if total_time == 0:
            await ctx.send("No playtime recorded for the requested weeks.")
            return

        if end is None:
            embed=discord.Embed(title="Hero playtime for all teams", description="Showing hero playtime for all weeks.\nAny heroes not shown have received 0 playtime.", color=0xf3e91d)
        elif end == start:
            embed=discord.Embed(title="Hero playtime for all teams", description="Showing hero playtime for week " + start + ".\nAny heroes not shown have received 0 playtime.", color=0xf3e91d)
        else:
            embed=discord.Embed(title="Hero playtime for all teams", description="Showing hero playtime for weeks " + start + " to " + end + "." + "\nAny heroes not shown have received 0 playtime.", color=0xf3e91d)

        embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")

        count = 0

        all_heroes = sorted(all_heroes, key=lambda x: x.time, reverse=True)


        if echo_total_time == 0:
            echo_play_perc = 0
        else:
            echo_play_perc = (echo.time / echo_total_time) * 100
        if sigma_total_time == 0:
            sigma_play_perc = 0
        else:
            sigma_play_perc = (sigma.time / sigma_total_time) * 100

        previous = 100

        for hero in all_heroes:
            play_perc = (hero.time / total_time) * 100

            if hero.name == "Echo" or hero.name == "Sigma":
                continue

            if echo_play_perc < previous and echo_play_perc > play_perc:
                if echo_play_perc != 0 and count <= 24:
                    count += 1
                    embed.add_field(name=echo.emote + " " + echo.name, value="{0:.1f}%".format(echo_play_perc), inline=True)

                elif echo_play_perc != 0 and count == 25:
                    count += 1
                    embed2=discord.Embed(color=0xf3e91d)
                    embed2.add_field(name=echo.emote + " " + echo.name, value="{0:.1f}%".format(echo_play_perc), inline=True)
                
                elif echo_play_perc != 0 and count > 25:
                    count += 1
                    embed2.add_field(name=echo.emote + " " + echo.name, value="{0:.1f}%".format(echo_play_perc), inline=True)
            
            if sigma_play_perc < previous and sigma_play_perc > play_perc:
                if echo_play_perc != 0 and count <= 24:
                    count += 1
                    embed.add_field(name=sigma.emote + " " + sigma.name, value="{0:.1f}%".format(sigma_play_perc), inline=True)

                elif sigma_play_perc != 0 and count == 25:
                    count += 1
                    embed2=discord.Embed(color=0xf3e91d)
                    embed2.add_field(name=sigma.emote + " " + sigma.name, value="{0:.1f}%".format(sigma_play_perc), inline=True)
                
                elif sigma_play_perc != 0 and count > 25:
                    count += 1
                    embed2.add_field(name=sigma.emote + " " + sigma.name, value="{0:.1f}%".format(sigma_play_perc), inline=True)

            previous = play_perc
            

            if play_perc != 0 and count <= 24:
                count += 1
                embed.add_field(name=hero.emote + " " + hero.name, value="{0:.1f}%".format(play_perc), inline=True)

            elif play_perc != 0 and count == 25:
                count += 1
                embed2=discord.Embed(color=0xf3e91d)
                embed2.add_field(name=hero.emote + " " + hero.name, value="{0:.1f}%".format(play_perc), inline=True)
            
            elif play_perc != 0 and count > 25:
                count += 1
                embed2.add_field(name=hero.emote + " " + hero.name, value="{0:.1f}%".format(play_perc), inline=True)

        if count <= 25:
            embed.set_footer(text=last_updated)
            await ctx.send(embed=embed)

        else:
            embed2.set_footer(text=last_updated)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)
        return

    else:
        flip = True

        for t in teams:
            if team_name.lower().replace("'", "") == t.name.lower().replace("'", "").replace(" ", ""):
                current_team_name = t.name
                flip = False
                for k in t.playrate_data.keys():
                    if not end is None and (k > int(end) or k < int(start)):
                        continue
                    for elem in t.playrate_data[k]:
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

                        if k <= 3:
                            baptiste.time += elem[29]
                            sigma.time += elem[30]
                            sigma_total_time += elem[31]
                            total_time += elem[31]

                        elif k <= 6:
                            echo.time += elem[29]
                            baptiste.time += elem[30]
                            total_time += elem[31]
                        
                        else:
                            echo.time += elem[29]
                            baptiste.time += elem[30]
                            sigma.time += elem[31]
                            sigma_total_time += elem[32]
                            total_time += elem[32]

                        if k >= 5:
                            echo_total_time += elem[31]  


        if flip:
            await ctx.send("Unable to find team with name '" + team_name + "'. Remember to omit spaces ('Stacys Moms' -> 'StacysMoms')")
            return

        if total_time == 0:
            await ctx.send("No playtime recorded for the requested team at the requested weeks.")
            return

        if end is None:
            embed=discord.Embed(title="Hero playtime for " + current_team_name, description="Showing hero playtime for all weeks.\nAny heroes not shown have received 0 playtime.", color=0xf3e91d)
        elif end == start:
            embed=discord.Embed(title="Hero playtime for " + current_team_name, description="Showing hero playtime for week " + start + ".\nAny heroes not shown have received 0 playtime.", color=0xf3e91d)
        else:
            embed=discord.Embed(title="Hero playtime for " + current_team_name, description="Showing hero playtime for weeks " + start + " to " + end + "." + "\nAny heroes not shown have received 0 playtime.", color=0xf3e91d)        
        
        embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")

        count = 0

        all_heroes = sorted(all_heroes, key=lambda x: x.time, reverse=True)

        if echo_total_time == 0:
            echo_play_perc = 0
        else:
            echo_play_perc = (echo.time / echo_total_time) * 100
        if sigma_total_time == 0:
            sigma_play_perc = 0
        else:
            sigma_play_perc = (sigma.time / sigma_total_time) * 100

        previous = 100

        for hero in all_heroes:
            play_perc = (hero.time / total_time) * 100

            if hero.name == "Echo" or hero.name == "Sigma":
                continue

            if echo_play_perc < previous and echo_play_perc > play_perc:
                if echo_play_perc != 0 and count <= 24:
                    count += 1
                    embed.add_field(name=echo.emote + " " + echo.name, value="{0:.1f}%".format(echo_play_perc), inline=True)

                elif echo_play_perc != 0 and count == 25:
                    count += 1
                    embed2=discord.Embed(color=0xf3e91d)
                    embed2.add_field(name=echo.emote + " " + echo.name, value="{0:.1f}%".format(echo_play_perc), inline=True)
                
                elif echo_play_perc != 0 and count > 25:
                    count += 1
                    embed2.add_field(name=echo.emote + " " + echo.name, value="{0:.1f}%".format(echo_play_perc), inline=True)
            
            if sigma_play_perc < previous and sigma_play_perc > play_perc:
                if echo_play_perc != 0 and count <= 24:
                    count += 1
                    embed.add_field(name=sigma.emote + " " + sigma.name, value="{0:.1f}%".format(sigma_play_perc), inline=True)

                elif sigma_play_perc != 0 and count == 25:
                    count += 1
                    embed2=discord.Embed(color=0xf3e91d)
                    embed2.add_field(name=sigma.emote + " " + sigma.name, value="{0:.1f}%".format(sigma_play_perc), inline=True)
                
                elif sigma_play_perc != 0 and count > 25:
                    count += 1
                    embed2.add_field(name=sigma.emote + " " + sigma.name, value="{0:.1f}%".format(sigma_play_perc), inline=True)

            previous = play_perc


            if play_perc != 0 and count <= 24:
                count += 1
                embed.add_field(name=hero.emote + " " + hero.name, value="{0:.1f}%".format(play_perc), inline=True)

            elif play_perc != 0 and count == 25:
                count += 1
                embed2=discord.Embed(color=0xf3e91d)
                embed2.add_field(name=hero.emote + " " + hero.name, value="{0:.1f}%".format(play_perc), inline=True)
            
            elif play_perc != 0 and count > 25:
                count += 1
                embed2.add_field(name=hero.emote + " " + hero.name, value="{0:.1f}%".format(play_perc), inline=True)

        if count <= 25:
            embed.set_footer(text=last_updated)
            await ctx.send(embed=embed)

        else:
            embed2.set_footer(text=last_updated)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)
        return

    await ctx.send("Idk what happened for us to reach this point....")

@client.command()
async def top10(ctx, stat=None, pt=None, start=None, end=None):
    if stat is None:
        await ctx.send("Missing argument: Desired Statistic\
            \nChoose from any of the follow: eliminations, finalblows, deaths, damage, healing, ults, crouches, damagereceived, healingreceived\n(ex: '$top10 damage')")
        return

    if pt == "-":
        pt = None

    if not start is None and end is None:
        end = start
    
    check = 0
    if stat.lower() == "eliminations":
        check = 0
    elif stat.lower() == "finalblows":
        check = 1
    elif stat.lower() == "deaths" or stat.lower() == "leastdeaths":
        check = 2
    elif stat.lower() == "damage":
        check = 3
    elif stat.lower() == "healing":
        check = 4
    elif stat.lower() == "damagereceived":
        check = 5
    elif stat.lower() == "healingreceived":
        check = 6
    elif stat.lower() == "ults":
        check = 7
    elif stat.lower() == "crouches":
        check = 8
    else:
        await ctx.send("Unable to understand argument: " + stat + "\nRemember to omit spaces ('final blows' -> 'finalblows')")
        return

    for p in players:

        sum_time = 0
        p.sorting_stat = 0
        
        for k in p.map_data.keys():
            

            if not end is None and (k > int(end) or k < int(start)):
                continue
            
            for elem in p.playtime[k]:
                sum_time += elem        

                #{60; 22; 21; 15117.47; 0; 15793.74; 6543.80; 7}
            for elem in p.map_data[k]:
                p.sorting_stat += float(elem[check])
        
        if pt is not None and pt.lower() == "per10" and sum_time >= 600:
            p.sorting_stat = p.sorting_stat*(10/(sum_time // 60))
        elif pt is not None and pt.lower() == "per10" and stat.lower() == "leastdeaths":
            p.sorting_stat = 999999
        elif pt is not None and pt.lower() == "per10":
            p.sorting_stat = 0

        if sum_time < 600 and stat.lower() == "leastdeaths":
            p.sorting_stat = 999999

                
    if stat.lower() == "leastdeaths":
        sorted_players = sorted(players, key=lambda x: x.sorting_stat, reverse=False)
    else:
        sorted_players = sorted(players, key=lambda x: x.sorting_stat, reverse=True)

    if pt is not None and pt.lower() == "per10":

        if end is None:
            embed=discord.Embed(title="Top 10 Players for Stat: " + stat + " avg per 10 minutes", description="Showing stats for all weeks.", color=0xf3e91d)
        elif end == start:
            embed=discord.Embed(title="Top 10 Players for Stat: " + stat + " avg per 10 minutes", description="Showing stats for week " + start + ".", color=0xf3e91d)
        else:
            embed=discord.Embed(title="Top 10 Players for Stat: " + stat + " avg per 10 minutes", description="Showing stats for weeks " + start + " to " + end + ".", color=0xf3e91d)            
        
    else:

        if end is None:
            embed=discord.Embed(title="Top 10 Players for Stat: " + stat, description="Showing stats for all weeks.", color=0xf3e91d)
        elif end == start:
            embed=discord.Embed(title="Top 10 Players for Stat: " + stat, description="Showing stats for week " + start + ".", color=0xf3e91d)
        else:
            embed=discord.Embed(title="Top 10 Players for Stat: " + stat, description="Showing stats for weeks " + start + " to " + end + ".", color=0xf3e91d)            


    embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")
    for i in range(10):
        if (pt is not None and pt.lower() == "per10") or stat.lower() == "damage" or stat.lower() == "healing" or stat.lower() == "healingreceived" or stat.lower() == "damagereceived": 
            embed.add_field(name=str(i + 1) + ". " + sorted_players[i].name, value="Total: " + "{0:.2f}".format(sorted_players[i].sorting_stat), inline=True)
        else:
            embed.add_field(name=str(i + 1) + ". " + sorted_players[i].name, value="Total: " + "{0:.0f}".format(sorted_players[i].sorting_stat), inline=True)
                     
    embed.set_footer(text="Player must have played at least 10 minutes to appear here.\n" + last_updated)
    await ctx.send(embed=embed)
    return


@client.command()
async def stats(ctx, name=None, start=None, end=None):
    if name is None:
        await ctx.send("Missing argument: Player Name\n(ex: '$stats Krusher99')")
        return

    if not start is None and end is None:
        end = start

    for p in players:
        if p.name.lower() == name.lower():
            #Time Played
            # temp_minutes = p.total_playtime // 60
            # hours = str(temp_minutes // 60)
            # minutes = str(temp_minutes % 60)
            sum_time = 0

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

                if not end is None and (k > int(end) or k < int(start)):
                    continue
                           
                #Maps Played
                if p.map_data[k] != []:
                    total_maps += len(p.map_data[k])
                
                for elem in p.playtime[k]:
                    sum_time += elem
                
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

            temp_minutes = sum_time // 60
            hours = str(temp_minutes // 60)
            minutes = str(temp_minutes % 60)

            if temp_minutes != 0:
                elims_pt = "{0:.2f}".format(total_elims*(10/temp_minutes))
                fb_pt = "{0:.2f}".format(total_final_blows*(10/temp_minutes))
                deaths_pt = "{0:.2f}".format(total_deaths*(10/temp_minutes))
                dmg_pt = "{0:.2f}".format(total_damage_dealt*(10/temp_minutes))
                heal_pt = "{0:.2f}".format(total_healing_dealt*(10/temp_minutes))
                dmgt_pt = "{0:.2f}".format(total_damage_taken*(10/temp_minutes))
                healt_pt = "{0:.2f}".format(total_healing_taken*(10/temp_minutes))
                ults_pt = "{0:.2f}".format(total_ults_used*(10/temp_minutes))
                crouch_pt = "{0:.2f}".format(total_crouches*(10/temp_minutes))
            else:
                elims_pt = "0"
                fb_pt = "0"
                deaths_pt = "0"
                dmg_pt = "0"
                heal_pt = "0"
                dmgt_pt = "0"
                healt_pt = "0"
                ults_pt = "0"
                crouch_pt = "0"


            if end is None:
                embed=discord.Embed(title="Stats for " + p.name + " (" + p.team.name + ")", description="Showing stats for all weeks.\n" + p.name + " has played for a total of " + hours + " hours and " + minutes + " minutes across " + str(total_maps) + " map(s).", color=0xf3e91d)
            elif end == start:
                embed=discord.Embed(title="Stats for " + p.name + " (" + p.team.name + ")", description="Showing stats for week " + start + ".\n" + p.name + " has played for a total of " + hours + " hours and " + minutes + " minutes across " + str(total_maps) + " map(s).", color=0xf3e91d)
            else:
                embed=discord.Embed(title="Stats for " + p.name + " (" + p.team.name + ")", description="Showing stats for weeks " + start + " to " + end + ".\n" + p.name + " has played for a total of " + hours + " hours and " + minutes + " minutes across " + str(total_maps) + " map(s).", color=0xf3e91d)
        


            #embed=discord.Embed(title="Stats for " + p.name + " (" + p.team.name + ")", description=p.name + " has played for a total of " + hours + " hours and " + minutes + " minutes across " + str(total_maps) + " map(s).", color=0xf3e91d)
            embed.set_thumbnail(url="http://overwatchtoronto.org/images/logo_white.png")

            str_elims = ""
            str_fb = ""
            str_deaths = ""
            str_damage = ""
            str_heal = ""
            str_dmgt = ""
            str_healt = ""
            str_ults = ""
            str_crouches = ""

            if start is None:
                str_elims = " (#" + str(rank_eliminations.index(p) + 1) + ")"
                str_fb = " (#" + str(rank_finalblows.index(p) + 1) + ")"
                str_deaths = " (#" + str(rank_least_deaths.index(p) + 1) + ")"
                str_damage = " (#" + str(rank_damage.index(p) + 1) + ")"
                str_heal = " (#" + str(rank_healing.index(p) + 1) + ")"
                str_dmgt = " (#" + str(rank_damagereceived.index(p) + 1) + ")"
                str_healt = " (#" + str(rank_healingreceived.index(p) + 1) + ")"
                str_ults = " (#" + str(rank_ults.index(p) + 1) + ")"
                str_crouches = " (#" + str(rank_crouches.index(p) + 1) + ")"

            embed.add_field(name="Eliminations", value="Total: " + str(total_elims) + "\nAvg/10mins: " + elims_pt + str_elims, inline=True)
            embed.add_field(name="Final Blows", value="Total: " + str(total_final_blows) + "\nAvg/10mins: " + fb_pt + str_fb, inline=True)
            embed.add_field(name="Deaths", value="Total: " + str(total_deaths) + "\nAvg/10mins: " + deaths_pt + str_deaths, inline=True)
            embed.add_field(name="Damage Dealt", value="Total: " + "{0:.2f}".format(total_damage_dealt) + "\nAvg/10mins: " + dmg_pt + str_damage, inline=True)
            embed.add_field(name="Healing Dealt", value="Total: " + "{0:.2f}".format(total_healing_dealt) + "\nAvg/10mins: " + heal_pt + str_heal, inline=True)
            embed.add_field(name="Damage Received", value="Total: " + "{0:.2f}".format(total_damage_taken) + "\nAvg/10mins: " + dmgt_pt + str_dmgt, inline=True)
            embed.add_field(name="Healing Received", value="Total: " + "{0:.2f}".format(total_healing_taken) + "\nAvg/10mins: " + healt_pt + str_healt, inline=True)
            embed.add_field(name="Ults Used", value="Total: " + str(total_ults_used) + "\nAvg/10mins: " + ults_pt + str_ults, inline=True)
            embed.add_field(name="Tactical Crouches", value="Total: " + str(total_crouches) + "\nAvg/10mins: " + crouch_pt + str_crouches, inline=True)
            embed.set_footer(text="Death ranking is for least deaths per 10.\n" + last_updated)
            await ctx.send(embed=embed)
            return
    
    await ctx.send("Unable to find player with name: " + name)

def ranking_maker(stat, pt="per10"):
    check = 0
    if stat.lower() == "eliminations":
        check = 0
    elif stat.lower() == "finalblows":
        check = 1
    elif stat.lower() == "deaths" or stat.lower() == "leastdeaths":
        check = 2
    elif stat.lower() == "damage":
        check = 3
    elif stat.lower() == "healing":
        check = 4
    elif stat.lower() == "damagereceived":
        check = 5
    elif stat.lower() == "healingreceived":
        check = 6
    elif stat.lower() == "ults":
        check = 7
    elif stat.lower() == "crouches":
        check = 8

    for p in players:
        
        p.sorting_stat = 0
        
        for k in p.map_data.keys():
            
                #{60; 22; 21; 15117.47; 0; 15793.74; 6543.80; 7}
            for elem in p.map_data[k]:
                p.sorting_stat += float(elem[check])
        
        if pt is not None and pt.lower() == "per10" and p.total_playtime >= 600:
            p.sorting_stat = p.sorting_stat*(10/(p.total_playtime // 60))
        elif pt is not None and pt.lower() == "per10" and stat.lower() == "leastdeaths":
            p.sorting_stat = 999999
        elif pt is not None and pt.lower() == "per10":
            p.sorting_stat = 0

        if p.total_playtime < 600 and stat.lower() == "leastdeaths":
            p.sorting_stat = 999999

                
    if stat.lower() == "leastdeaths":
        sorted_players = sorted(players, key=lambda x: x.sorting_stat, reverse=False)
    else:
        sorted_players = sorted(players, key=lambda x: x.sorting_stat, reverse=True)
    
    return sorted_players

def scan_data():
    with open(str(pathlib.Path(__file__).parent.absolute()) + "/teams.txt", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, skipinitialspace=True, delimiter=',')
        for row in csv_reader:
            curr_team = team(row[0])
            for name in row[1:]:
                curr_player = player(name, curr_team)
                players.append(curr_player)
                curr_team.players.append(curr_player)
            teams.append(curr_team)


    with open(str(pathlib.Path(__file__).parent.absolute()) + "/stats.txt", 'r') as csv_file:
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
                    
                for y in players:
                    if y.name == row[0] and y.team == match_save.teams[0]:

                        temp_playtime = [int(i.replace(" ", "")) for i in row[31].replace("{", "").replace("}", "").split(";")]

                        if match_save.week <= 6:
                            while len(temp_playtime) < 31:
                                temp_playtime.append(0)
                        else:
                            while len(temp_playtime) < 32:
                                temp_playtime.append(0)

                        temp_playtime.append(int(row[17]))
                        current_round.hero_playtime_1 = temp_playtime
                        match_save.teams[0].playrate_data[match_save.week].append(temp_playtime)

                        temp_playtime = [int(i.replace(" ", "")) for i in row[32].replace("{", "").replace("}", "").split(";")]
                        if match_save.week <= 6:
                            while len(temp_playtime) < 31:
                                temp_playtime.append(0)
                        else:
                            while len(temp_playtime) < 32:
                                temp_playtime.append(0)

                        temp_playtime.append(int(row[17]))
                        current_round.hero_playtime_2 = temp_playtime
                        match_save.teams[1].playrate_data[match_save.week].append(temp_playtime)

                    elif y.name == row[6] and y.team == match_save.teams[0]:

                        temp_playtime = [int(i.replace(" ", "")) for i in row[31].replace("{", "").replace("}", "").split(";")]
                        if match_save.week <= 6:
                            while len(temp_playtime) < 31:
                                temp_playtime.append(0)
                        else:
                            while len(temp_playtime) < 32:
                                temp_playtime.append(0)

                        temp_playtime.append(int(row[17]))
                        current_round.hero_playtime_1 = temp_playtime
                        match_save.teams[1].playrate_data[match_save.week].append(temp_playtime)

                        temp_playtime = [int(i.replace(" ", "")) for i in row[32].replace("{", "").replace("}", "").split(";")]
                        if match_save.week <= 6:
                            while len(temp_playtime) < 31:
                                temp_playtime.append(0)
                        else:
                            while len(temp_playtime) < 32:
                                temp_playtime.append(0)

                        temp_playtime.append(int(row[17]))
                        current_round.hero_playtime_2 = temp_playtime
                        match_save.teams[0].playrate_data[match_save.week].append(temp_playtime)

                current_round.map_time = int(row[17])

                match_save.maps.append(current_round)
                matches.append(match_save)


scan_data()

rank_eliminations = ranking_maker("eliminations")
rank_finalblows = ranking_maker("finalblows")
rank_deaths = ranking_maker("deaths")
rank_least_deaths = ranking_maker("leastdeaths")
rank_damage = ranking_maker("damage")
rank_healing = ranking_maker("healing")
rank_damagereceived = ranking_maker("damagereceived")
rank_healingreceived = ranking_maker("healingreceived")
rank_ults = ranking_maker("ults")
rank_crouches = ranking_maker("crouches")


#client.run('Njg1MTg5OTA3OTQwOTAwODY5.XmFFGA.5Rg5_RrWeboBw9LQ6XGWNbf8BL8') # Live
client.run('NzA1NTczMjgxNDczODg4MjU3.XqtsGA.CWoeoGuAQFgM8ebg7EhIpOgMG7M') # Tester




