import os
import discord
from discord.ext import commands, tasks
from asyncio import sleep
import pymongo
from discord.utils import get
import random
import asyncio
import json
import sys
import datetime
import requests
import aiohttp

token = "ODYwODAwODEyMDMxNDEwMTg2.YOAhOg.nsUT90vPLZkxup57n2WXvvay2FI"
headers = {'Authorization': f'Bot {token}'}
os.system('pip install discord.py==1.5.1')
os.system("pip install dnspython")
os.system("python -m pip install -U pymongo")
os.system("python -m pip install pymongo[srv]")
os.system("pip install dnspython==2.0.0")
os.system("pip3 install dnspython")
White = "\033[0;37m"
Orange = "\033[1;33m"
WARNING = '\033[93m'
FAIL = '\033[91m'
CORRECT = "\033[32m"
Yellow = "\033[33m"
Blue = "\033[34m"
Magenta = "\033[35m"
red = '\x1b[38;5;196m'
LightGray = "\033[37m"
DarkGray = "\033[90m"
LightRed = "\033[91m"
LightGreen = "\033[92m"
LightYellow = "\033[93m"
LightBlue = "\033[94m"
LightMagenta = "\033[95m"
Purple = "\033[37m"
color = 0x2f3136


async def ownership(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 712969671766442024
# setup
os.system("pip install discord.py==1.5")
intents=discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix=commands.when_mentioned_or(","), case_insensitive=True, intents=intents)

client.remove_command("help")
client.sniped_messages = {}
blacklisted = [842738716695068693]
starttime = datetime.datetime.utcnow()
mongodb = pymongo.MongoClient('mongodb+srv://radiant:sh11223344sh@radiantbot.jrkmc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = mongodb.get_database("radiant").get_collection("servers")

pic = "https://images-ext-1.discordapp.net/external/uFVt5bQSv_KbXan9ePbuvPoHTojR7iVAF6vphM9lZGM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/860800812031410186/09a3d218766a121829fb8a51d59285e2.webp?width=678&height=678"

modules = [
    'welcchannel',
    'welcmsg',
    'log'
]



class radiant:

    def new(owner_id, server_id):
        db.insert_one({
            "whitelisted": [owner_id],
            "log": None,
            "punishment": "ban",
            'welcchannel': None,
            'welcmsg': None,
            'autorole': None,
            'limits': 1,
            "guild_id": server_id
        })


from cogs.Antinuke import Antinuke

client.add_cog(Antinuke(client))

#@client.command()
#@commands.has_permissions(administrator=True)
#@commands.cooldown(1,60, commands.BucketType.user)
#async def setup(ctx):
 # try:
  #  if ctx.author.id in blacklisted:
   #   return
    #else:
#      if not db.find_one({ "guild_id": ctx.guild.id }):
 #       guild_ = client.get_guild(ctx.guild.id)
  #      radiant.new(guild_.owner.id, guild_.id)
   #   channel2 = discord.utils.get(ctx.guild.channels, name=f'radiant-logs')
    #  embed = discord.Embed(title = f"Welcome to Radiants Setup. Starting Setup In 2 Seconds.",color =color)
#      msg = await ctx.send(embed=embed)
 #     embed6 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color)
  #    await msg.edit(embed=embed6)
   #   
    #  if not channel2:
     #   embed7 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color)
      #  embed7.add_field(name = f"<a:loading1:863106653682925622> Could Not Find A Logging... Creating A Logging Channel..", value='‏‏‎‏‏‎ ‎', inline=False)
       # await msg.edit(embed=embed7)
#        channel = await ctx.guild.create_text_channel(name='radiant-logs')
 #       overwrite = channel.overwrites_for(ctx.guild.default_role)
  #      overwrite.send_messages = False
   #     overwrite.view_channel = False
    #    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
     #   embed8 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color)
      #  embed8.add_field(name = f"<a:loading1:863106653682925622> Could Not Find A Logging... Creating A Logging Channel..", value='‏‏‎ ‎', inline=False)
       # embed8.add_field(name =f"<a:success:863095257654493195> Created Logging Channel", value='‏‏‎ ‎', inline=False)
        #await msg.edit(embed=embed8)
 #       embed11 = discord.Embed(title = f"<a:success:863095257654493195> Checking For Logging Channel...",color =color)
  #      embed11.add_field(name = f"<a:success:863095257654493195> Could Not Find A Logging... Creating A Logging Channel..", value='‏‏‎ ‎', inline=False)
   #     embed11.add_field(name =f"<a:success:863095257654493195> Created Logging Channel", value='‏‏‎ ‎', inline=False)
    #    embed11.add_field(name = f"<a:success:863095257654493195> Finished Radiants Setup, To Completly Finish Radiants setup you could set a welcome channel by doing ,welcchannel (channel) and to set a welcome message do welcmsg (welcome message). ",value='‏‏‎ ‎', inline=False)
     #   await msg.edit(embed=embed11)
 #     else:
  #      embed9 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color,inline=False)
   #     embed9.add_field(name = f"<a:success:863095257654493195> Found Logging Channel",value='‏‏‎ ‎', inline=False)
    #    await msg.edit(embed=embed9)
     #   embed10 = discord.Embed(title = f"<a:success:863095257654493195> Checking For Logging Channel...",color =color, inline=False)
      #  embed10.add_field(name = f"<a:success:863095257654493195> Found Logging Channel",value='‏‏‎ ‎', inline=False)
       # embed10.add_field(name = f"<a:success:863095257654493195> Finished Radiants Setup, To Completly Finish Radiants setup you could set a welcome channel by doing ,welcchannel (channel) and to set a welcome message do welcmsg (welcome message). ",value='‏‏‎ ‎',inline=False)
        #await msg.edit(embed=embed10)
   #     print(f"{ctx.author.name} send a cmd in {ctx.guild.name}")
  #except Exception as e:
   # print(e)

@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def shutdown(ctx):
    if ctx.author.id == 712969671766442024 or ctx.author.id == 757931086998274089:
        await ctx.send("Shuting down....")
        await client.logout()
    else:
        return


@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def leave(ctx):
  if ctx.author.id == 712969671766442024 or ctx.author.id == 757931086998274089: 
    await ctx.guild.leave()
    print(f"{ctx.author.name} send a cmd in {ctx.guild.name}")
  else:
    return






@client.command()   
@commands.cooldown(1,10, commands.BucketType.user) 
async def guilds(ctx):
  try:
    if ctx.author.id == 712969671766442024 or ctx.author.id == 757931086998274089:
      embed = discord.Embed(title="guilds:",color=color)
      guilds = client.guilds
      for guild in guilds:
        gm = guild.member_count
        gn = guild.name
        print(f"{gn} | {gm}")
    else:
      return
  except Exception as e:
    print(e)

@tasks.loop(seconds=5)
async def statusloop():
  await client.wait_until_ready()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f",help"))
  await sleep(5)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"over {len(client.guilds)} guilds"))
  await sleep(5)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"over {len(set(client.get_all_members()))} members"))
  await sleep(5)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"discord.gg/e6dqdZzFxu"))
  await sleep(5)
statusloop.start()

# login display

@client.event
async def on_ready():
  print(f"Logged into {client.user.name} | {client.user.id}")

# create logs channel

@client.event
async def on_connect():
  for server in client.guilds:
        if not db.find_one({ "guild_id": server.id }):
            guild_ = client.get_guild(server.id)
            radiant.new(guild_.owner.id, guild_.id)
            


@client.event
async def on_guild_join(guild):
    server = client.get_guild(guild.id)
    radiant.new(server.owner.id, server.id)
    channel = guild.text_channels[0]
    channellol = client.get_channel(864968374476079105)
    invlink = await channel.create_invite(unique=True)
    await channellol.send(f"i have been added to: {invlink}")

@client.event
async def on_guild_remove(guild):
  channellol = client.get_channel(864968374476079105)
  haha = f'{len(guild.members)}'
  await channellol.send(f"I have Been Removed From: **{guild.name}** -> **{haha}** Members")


#@client.command(aliases=["whois"])
#@commands.cooldown(1,5, commands.BucketType.user)
#async def userinfo(ctx, member: discord.Member = None):
 # if ctx.author.id in blacklisted:
  #    return
 # else:
  #  if member == None:
   #     member = ctx.author
   # if member == '':
    #    member = ctx.author
 #   embed = discord.Embed(title='User Info', color=color)
  #  embed.add_field(name="User ID", value=f'{member.id}', inline=True)
   # embed.add_field(name="User Name", value=f'{member.display_name}', inline=True)
    #embed.add_field(name="Discriminator", value=f'{member.discriminator}', inline=True)
 #   embed.add_field(name="Creation Date", value=f'{member.created_at.strftime("%a, %d %B %Y, %I:%M %p")}', inline=True)
  #  embed.set_thumbnail(url=member.avatar_url)
   # embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    #await ctx.send(embed=embed)

@client.command(aliases=["whois"])
@commands.cooldown(1,5, commands.BucketType.guild)
async def userinfo(ctx, *, user: discord.Member = None): 
  if ctx.author.id in blacklisted:
      return
  else:
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=color, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="User ID", value=f'{user.id}')
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    return await ctx.message.reply(embed = embed, mention_author=False) 


#@client.command(aliases=["h"])
#@commands.cooldown(1,8, commands.BucketType.user)
#async def  (ctx):
  #try:
    
   # if ctx.author.id in blacklisted:
    #  return
 #   else:
  #    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"]
   #   current = 0
    #  msg = await ctx.send(embed=client.help_pages[current])
    
     # for button in buttons:
      #    await msg.add_reaction(button)
        
  #    while True:
   #     try:
    #        reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=30.0)

     #   except asyncio.TimeoutError:
      #      return print(f"{ctx.author.name} send a help cmd in {ctx.guild.name}")

       # else:
        #    previous_page = current
         #   if reaction.emoji == u"\u23EA":
          #      current = 0
                
           # elif reaction.emoji == u"\u2B05":
            #    if current > 0:
             #       current -= 1
                    
        #    elif reaction.emoji == u"\u27A1":
         #       if current < len(client.help_pages)-1:
          #          current += 1

           # elif reaction.emoji == u"\u23E9":
            #    current = len(client.help_pages)-1

         #   for button in buttons:
          #      await msg.remove_reaction(button, ctx.author)

           # if current != previous_page:
            #    await msg.edit(embed=client.help_pages[current])
  #except Exception as e:
   #   print(e)




@client.command(aliases=["h"])
@commands.cooldown(1,8, commands.BucketType.user)
async def help(ctx):
  try:
    if ctx.author.id in blacklisted:
      return
    else:
     embed1 = discord.Embed(title=f"**Radiants Help Command**", description= 'Invite me [__here__](https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)', color=color)
     embed1.add_field(name=f'**Modules**',value='''
   Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
 ```1 | Moderation Commands
2 | Fun Commands
3 | Info Commands
4 | Anti-Nuke
5 | Welcoming
6 | Economy 
7 | Animals```''')
     embed1.set_footer(text="Page 1/8")
     embed2 = discord.Embed(title="**Radiants Moderation Commands**",description= 'Invite me [here](https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)', color = color) 
     embed2.add_field(name=f'''**Moderation Commands**''', value=f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
   ```1 | ban <user> [reason]
2 | kick <user> [reason]
3 | unbanall
4 | mute <user> [reason]
5 | unmute <user>
6 | purge <amount
7 | nuke
8 | slowmode <amount>
9 | autorole <role>
10| setup
11| lock
12| unlock
13| toggle <module>
14| role <user> <role>```''')
     embed2.set_footer(text="Page 2/8")
     embed3 = discord.Embed(title="**Radiants Utility Commands**",description= 'Invite me [here](https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)', color = color) 
     embed3.add_field(name=f'''**Utility Commands**''', value=f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
   ```1 | membercount 
2 | av <user>
3 | ping
4 | Serverbanner
5 | Servericon
6 | whois <user>
7 | serverinfo
8 | botinfo
9 | uptime
10| afk [reason]```''')  
     embed3.set_footer(text="Page 3/8")
     embed4 = discord.Embed(title="**Radiants Fun Commands**",description= 'Invite me [here](https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)', color = color) 
     embed4.add_field(name=f'''**Fun Commands**''', value=f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
  ```1 | hug <user>
2 | slap <user>
3 | kiss <user>
4 | tickle <user>
5 | 8ball <user>
6 | snipe 
7 | coinflip 
8 | pp <user>
9 | hug <user>
10| coinflip```''') 
     embed4.set_footer(text="Page 4/8")
     embed5 = discord.Embed(title="**Radiants Anti-Nuke Commands**",   description= 'Invite me [here](https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)', color = color) 
     embed5.add_field(name=f'''**Anti-Nuke Commands**''', value=f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
  ```1 | whitelist <user>
2 | unwhitelist <user>
3 | whitelisted 
4 | Punishment <punishment>```''')
     embed5.set_footer(text="Page 5/8")
     embed6 = discord.Embed(title='**Radiant Anti-Nuke Modules**', color=color)
     embed6.add_field(name="Modules: ", value= 
  f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
   ```1 | racoon
2 | fox
3 | bear
4 | koala
5 | kangaroo
6 | dog
7 | cat
8 | duck```''')
     embed6.set_footer(text="Page 6/8")
     embed7 = discord.Embed(title='**Radiant Welcoming System**', color=color)
     embed7.add_field(name="Modules: ", value= 
  f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
  ```1 | Welcchannel <channel>
2 | welcmsg <message>
3 | welctest```''')
     embed7.set_footer(text="Page 7/8")
     embed8 = discord.Embed(title='**Radiant Economy Commands**', color=color)
     embed8.add_field(name="Economy Commands: ", value= 
  f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
  ```1 | bal
2 | withdraw <amount>
3 | rob <user>
4 | deposit <amount>
5 | leaderboard
6 | send <user> <amount>
7 | beg```''')
     embed8.set_footer(text="Page 8/8")
     pages = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8]
     message = await ctx.message.reply(embed = embed1, mention_author=False) 
   
     await message.add_reaction('⏮')
     await message.add_reaction('◀')
     await message.add_reaction('▶')
     await message.add_reaction('⏭')

     def check(reaction, user):
        return user == ctx.author

     i = 0
     reaction = None

     while True:
          if str(reaction) == '⏮':
              i = 0
              await message.edit(embed=pages[i])
          elif str(reaction) == '◀':
              if i > 0:
                  i -= 1
                  await message.edit(embed=pages[i])
          elif str(reaction) == '▶':
              if i < 7:
                  i += 1
                  await message.edit(embed=pages[i])

          elif str(reaction) == '⏭':
              i = 7
              await message.edit(embed=pages[i])

          try:  
              reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=check)
              await message.remove_reaction(reaction, user)
          except:
              pass

              await message.clear_reaction()
  except Exception as e:
    print(e)




@client.command(aliases=['coin'])
@commands.cooldown(1,5, commands.BucketType.user)
async def coinflip(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    choices = ["heads", "tails"]
    embed = discord.Embed(title='Coinflip',description = f'{random.choice(choices)}', color=color)
    await ctx.send(embed=embed)
    print(f"{ctx.author.name} send a cmd in {ctx.guild.name}")




@client.command(aliases=["wled"])
@commands.cooldown(1,10, commands.BucketType.user)
async def whitelisted(ctx):
  try:
    if ctx.author.id in blacklisted:
      return
    else:
      whitelistedusers = db.find_one({ "guild_id": ctx.guild.id })['whitelisted']
      if ctx.author.id == ctx.guild.owner.id or ctx.author.id in whitelistedusers:
        result = ''
        data = db.find_one({ "guild_id": ctx.guild.id })['whitelisted']
        for i in data:
            user_ = client.get_user(i)
            if user_ == None:
                user = 'Unable To Fetch Name'
            else:
                user = user_.mention
            result += f"{user} : {i}\n"

        embed = discord.Embed(title=f'Whitelisted Users For: {ctx.guild.name}',description=result,  color=color)
        await ctx.send(embed=embed)
        if result == None:
          embed1 = discord.Embed(title=f'Radiant',description="There Is No Whitelisted Users In This Server, Do ,whitelist (user) To Whitelist A User Of Your Choice",  color=color)
          await ctx.send(embed=embed1)

      else:
        embed2 = discord.Embed(title=f'Radiant',description="Only Whitelisted Users And Server Owner Can Use This Command",  color=color)
        await ctx.send(embed=embed2)

  except Exception as e:
    await ctx.send(e)

@client.command(aliases=["ppsize"])
@commands.cooldown(1,5, commands.BucketType.user)
async def pp(ctx):
  if ctx.author.id in blacklisted:
    return
  else:

    responses = [
        "Your pp size 8==================================D .",
        "Your pp size 8===D.", "Your pp size 8======D",
        "Your pp size 8========D.", "Your pp size 8================D.",
        "Your pp size 8====D", "Your pp size 8==D.",
        "Your pp size 8==========D.", "Your pp size 8=D."
    ]
    embed = discord.Embed(title=f"{random.choice(responses)}",description="",color=color)

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def welctest(ctx):
  try:
     if ctx.author.id in blacklisted:
       return
     else:
       welcmsg = db.find_one({ "guild_id": ctx.guild.id})['welcmsg']
       if welcmsg == None:
         embed = discord.Embed(color=color,description=f'No Welcome Message Has Been Set Yet, Do ,welcmsg To Set A Welcome Message And ,welcchannel To Set A Welcome Channel')
         await ctx.send(embed=embed)
       else:
         embed = discord.Embed(color=color,description=f'{welcmsg}')
         embed.set_author(name=f'Welcome To {ctx.guild.name}')
         embed.set_footer(text=f'{len(ctx.guild.members)} Members | {ctx.guild.name}')
         embed.set_thumbnail(url=f'{ctx.author.avatar_url}')
         await ctx.send(ctx.author.mention, embed=embed)
  except Exception as e:
    print(e)



@client.event
async def on_member_join(member):
 
    guild = member.guild
    welcchannel = db.find_one({ "guild_id": guild.id})['welcchannel']
    welcmsg = db.find_one({ "guild_id": guild.id})['welcmsg'] 
    autoroleid = db.find_one({ "guild_id": guild.id})['autorole']
    if welcchannel is None:
        pass  
    else: 
      channel = client.get_channel(int(welcchannel)) 
  
    embed = discord.Embed(color=color,description=f'{welcmsg}')
    embed.set_author(name=f'Welcome To {guild.name}')
    embed.set_footer(text=f'{len(guild.members)} Members | {guild.name}')
    embed.set_thumbnail(url=f'{member.avatar_url}')
    try:
      if welcmsg is None:
          pass
      else:
          #await channel.send(member.mention)
          await channel.send(member.mention, embed=embed)
    except Exception as e:
      print(e)
    try:
      if autoroleid is None:
          pass
      else:
        autorole = get(guild.roles, id=int(autoroleid))
        await member.add_roles(autorole, reason="Autorole")
    except Exception as e:
      print(e)
     



#@client.event
#async def on_member_join(member):
#   guild = member.guild
#  try:
   #     guild = member.guild
    #    logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add).flatten()
     #   logs = logs[0]
      #  reason = "Adding Bot As Non-Whitelisted User"
       # whitelisted = db.find_one({ "guild_id": guild.id })['whitelisted']
        #if logs.user.id in whitelisted:
    #        return
     #   await member.ban(f'Radiant Anti-Nuke | {reason}')
      #  punishment = db.find_one({ "guild_id": guild.id })['punishment']
       # if punishment == 'ban':
        #    try:
         #       await logs.user.ban(reason=f"Radiant Anti-Nuke | {reason}")
          #  except:
               #pass
 #       if punishment == 'kick':
  #          try:
   #             await logs.user.kick(reason=f"Radiant Anti-Nuke | {reason}")
    #        except:
     #           pass
   # except:
    #  pass 



#@client.command(aliases=["limitsset"])
#@commands.has_permissions(administrator=True)
#@commands.cooldown(1,5, commands.BucketType.user)
#async def limits(ctx, amount=None):
 # try:
  #  if ctx.author.id in blacklisted:
   #     return
    #else:
      
     # if amount == None:
      # embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/XHryBKsgJ7', description=f'Please Specify A Limit Amount To Set')
      # embed.set_thumbnail(url=client.user.avatar_url)
       #embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
     #  await ctx.send(embed=embed)
      # return

   #   else:
    #   db.update_one({"guild_id": ctx.guild.id }, {"$set": { f"limits": f'{amount}'}})
     #  embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/XHryBKsgJ7', description=f'Limits Is Set To {amount}')
      # embed.set_thumbnail(url=client.user.avatar_url)
       #embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
       #await ctx.send(embed=embed)
       #return
  #except Exception as e:
   # print(e)

#def new(owner_id, server_id):
        #db.insert_one({
            #"whitelisted": [  owner_id],
            #"log": None,
            #"punishment": "ban",
            #'welcchannel': None,
            #'welcmsg': None,
            #'autorole': None,
            #'ban_limit': 1,
           # 'kick_limit': 1,
            #'chandel_limit': 1,
           # 'roledel_limit': 1,
           # 'chancreate_limit': 1,
           # 'rolecreate_limit': 1,
           # 'bot_limit': 1,
           # "guild_id": server_id
       # })

@client.command()
@commands.cooldown(1,5, commands.BucketType.guild)
async def uptime(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    uptime = datetime.datetime.utcnow() - starttime
    uptime = str(uptime).split('.')[0]
    embed = discord.Embed(title="Radiants Uptime", description=f"**Uptime** = " + ''  + uptime +'', color=color)
    embed.set_footer(text="Note: It Only Has A Couple Mins/Hours Of Uptime Because I Have Fixed The Help Command And Had To Stop And Re Run Radiant")
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_channels=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def unlock(ctx, channel: discord.TextChannel = None):
  if ctx.author.id in blacklisted:
    return
  else:
      overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      embed = discord.Embed(title='Radiant', description=f'Unlocked **{ctx.channel.name}**', color=color)
      await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_channels=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def lock(ctx, channel: discord.TextChannel = None):
  if ctx.author.id in blacklisted:
    return
  else:
      overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      embed = discord.Embed(title='Radiant', description=f'Locked **{ctx.channel.name}**', color=color)
      await ctx.send(embed=embed)

@client.command(aliases=["welcomechannelset","wlcchannelset", "wlcchannel", "welcchan", "wlcchan", "welcomechannel"])
@commands.has_permissions(administrator=True)
@commands.cooldown(1,5, commands.BucketType.guild)
async def welcchannel(ctx, channel : discord.TextChannel=None):
  if ctx.author.id in blacklisted:
    return
  else:
    if not db.find_one({ "guild_id": ctx.guild.id }):
        guild_ = client.get_guild(ctx.guild.id)
        radiant.new(guild_.owner.id, guild_.id)
    if channel == None:
       embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'Please Specify A Welcome Channel To Set')
       embed.set_thumbnail(url=client.user.avatar_url)
       embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)
    
    else:
        db.update_one({"guild_id": ctx.guild.id }, {"$set": { f"welcchannel": f'{channel.id}'}})
        embed = discord.Embed(title=f'Radiant', description=f'Welcome Channel Is now Set To: **{channel}**, Do ,toggle welchannel If You Want To Turn It Off',color=color)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@client.command(aliases=["welcmsg", "welcomemessage", "welcomemsg"])
@commands.has_permissions(administrator=True)
@commands.cooldown(1, 5, commands.BucketType.guild)
async def welcmessage(ctx, *, msg=None):
  if ctx.author.id in blacklisted:
    return
  else:
    if not db.find_one({ "guild_id": ctx.guild.id }):
        guild_ = client.get_guild(ctx.guild.id)
        radiant.new(guild_.owner.id, guild_.id)
    if msg == None:
       embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'Please Specify A Welcome Message To Set')
       embed.set_thumbnail(url=client.user.avatar_url)
       embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)
    
    else:
        db.update_one({"guild_id": ctx.guild.id }, {"$set": { f"welcmsg": f'{msg}'}})
        embed = discord.Embed(title=f'Radiant', description=f'Welcome Message Is now Set To: {msg}, Do ,toggle welcmsg If You Want To Turn It Off',color=color)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
@commands.cooldown(1, 8, commands.BucketType.guild)
async def autorole(ctx, *, role : discord.Role = None):
  if ctx.author.id in blacklisted:
    return
  else:
    if not db.find_one({ "guild_id": ctx.guild.id }):
        guild_ = client.get_guild(ctx.guild.id)
        radiant.new(guild_.owner.id, guild_.id)
    if role == None:
       embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/e6dqdZzFxu', description=f'Please Specify A Role To Set')
       embed.set_thumbnail(url=client.user.avatar_url)
       embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)
    else:
      db.update_one({"guild_id": ctx.guild.id }, {"$set": { f"autorole": f'{role.id}'}})
      embed = discord.Embed(title=f'Radiant', description=f'Autorole Is now Set To: **{role}**, Do ,toggle autorole If You Want To Turn It Off',color=color)
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)







#@client.command(aliases=["log", "loggingchannel", "logging"])
#@commands.has_permissions(administrator=True)
#@commands.cooldown(1,60, commands.BucketType.guild)
#async def logs(ctx):
 # try:
  #  if ctx.author.id in blacklisted:
   #   return
   # else:
    #  if not db.find_one({ "guild_id": ctx.guild.id }):
     #   guild_ = client.get_guild(ctx.guild.id)
      #  radiant.new(guild_.owner.id, guild_.id)
  #    channel2 = discord.utils.get(ctx.guild.channels, name=f'radiant-logs')
   #   embed = discord.Embed(title = f"Welcome to Radiants Setup. Starting Setup In 2 Seconds.",color =color)
    #  msg = await ctx.send(embed=embed)
     # embed6 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color)
      #await msg.edit(embed=embed6)
      
 #     if not channel2:
  #      embed7 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color)
   #     embed7.add_field(name = f"<a:loading1:863106653682925622> Could Not Find A Logging... Creating A Logging Channel..", value='‏‏‎‏‏‎ ‎', inline=False)
    #    await msg.edit(embed=embed7)
     #   channel = await ctx.guild.create_text_channel(name='radiant-logs')
      #  overwrite = channel.overwrites_for(ctx.guild.default_role)
       # overwrite.send_messages = False
        #overwrite.view_channel = False
   #     await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    #    embed8 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color)
     #   embed8.add_field(name = f"<a:loading1:863106653682925622> Could Not Find A Logging... Creating A Logging Channel..", value='‏‏‎ ‎', inline=False)
      #  embed8.add_field(name =f"<a:success:863095257654493195> Created Logging Channel", value='‏‏‎ ‎', inline=False)
       # await msg.edit(embed=embed8)
        #embed11 = discord.Embed(title = f"<a:success:863095257654493195> Checking For Logging Channel...",color =color)
 #       embed11.add_field(name = f"<a:success:863095257654493195> Could Not Find A Logging... Creating A Logging Channel..", value='‏‏‎ ‎', inline=False)
  #      embed11.add_field(name =f"<a:success:863095257654493195> Created Logging Channel", value='‏‏‎ ‎', inline=False)
   #     embed11.add_field(name = f"<a:success:863095257654493195> Finished Radiants Setup, To Completly Finish Radiants setup you could set a welcome channel by doing ,welcchannel (channel) and to set a welcome message do welcmsg (welcome message). ",value='‏‏‎ ‎', inline=False)
    #    await msg.edit(embed=embed11)
     # else:
      #  embed9 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color,inline=False)
       # embed9.add_field(name = f"<a:success:863095257654493195> Found Logging Channel",value='‏‏‎ ‎', inline=False)
  #      #await msg.edit(embed=embed9)
   #     embed10 = discord.Embed(title = f"<a:success:863095257654493195> Checking For Logging Channel...",color =color, inline=False)
    #    embed10.add_field(name = f"<a:success:863095257654493195> Found Logging Channel",value='‏‏‎ ‎', inline=False)
     #   embed10.add_field(name = f"<a:success:863095257654493195> Finished Radiants Setup, To Completly Finish Radiants setup you could set a welcome channel by doing ,welcchannel (channel) and to set a welcome message do welcmsg (welcome message). ",value='‏‏‎ ‎',inline=False)
      #  await msg.edit(embed=embed10)
     #   print(f"{ctx.author.name} send a cmd in {ctx.guild.name}")
  #except Exception as e:
   # print(e)



@client.command(aliases=["unwl"]) 
@commands.cooldown(1,5, commands.BucketType.guild)
async def unwhitelist(ctx, member: discord.Member = None):
  try:
    if ctx.author.id in blacklisted:
      return
    else:
      if not db.find_one({ "guild_id": ctx.guild.id }):
        guild_ = client.get_guild(ctx.guild.id)
        radiant.new(guild_.owner.id, guild_.id)
      if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if member == None:
            embed = discord.Embed(title='Radiant', color=color, description=f'Please Specify A Member To UnWhitelist')
            await ctx.send(embed=embed)
            
        else:
            db.update_one({ "guild_id": ctx.guild.id }, { "$pull": { "whitelisted": member.id }})
            embed = discord.Embed(title='Radiant', color=color, description=f'Unwhitelisted **{member.mention}**')
            embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
      else:
       embed = discord.Embed(title='Radiant', color=color, description=f'Only Guild Owner Can Use This Command')
       embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)
       return
  except Exception as e:
    print(e)


        
@client.command(aliases=["wl"]) 
@commands.cooldown(1,5, commands.BucketType.guild)
async def whitelist(ctx, member: discord.Member = None):
  try:
    if ctx.author.id in blacklisted:
      return
    else:
      if not db.find_one({ "guild_id": ctx.guild.id }):
        guild_ = client.get_guild(ctx.guild.id)
        radiant.new(guild_.owner.id, guild_.id)
      if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if member == None:
            embed = discord.Embed(title='Radiant', color=color, description=f'Please Mention A User To Whitelist')
            await ctx.send(embed=embed)
        else:
            whitelistedusers = db.find_one({ "guild_id": ctx.guild.id })['whitelisted']
            if member.id in whitelistedusers:
              embed = discord.Embed(title='Radiant', color=color, description=f'This User Is Already Whitelisted')
              embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
              await ctx.send(embed=embed)
            else: 
              db.update_one({ "guild_id": ctx.guild.id }, { "$push": { "whitelisted": member.id}})
              embed = discord.Embed(title='Radiant', color=color, description=f'Whitelisted **{member.mention}**')
              embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
              await ctx.send(embed=embed)
      else:
       embed = discord.Embed(title='Radiant', color=color, description=f'Only Guild Owner Can Use This Command')
       embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)
       return
  except Exception as e:
    print(e)


@client.command(aliases=["p"])
@commands.has_permissions(administrator=True)
@commands.cooldown(1,15, commands.BucketType.guild)
async def punishment(ctx, punishment= None):
  if ctx.author.id in blacklisted:
    return
  else:
    if not db.find_one({ "guild_id": ctx.guild.id }):
        guild_ = client.get_guild(ctx.guild.id)
        radiant.new(guild_.owner.id, guild_.id)
    if punishment == None:
        embed = discord.Embed(title='Radiant', color=color, description=f'Please Specify A Punishment')
        await ctx.send(embed=embed)
    if punishment.lower() == 'ban':
        db.update_one({ "guild_id": ctx.guild.id }, { "$set": { "punishment": "ban"}})
        embed = discord.Embed(title='Radiant', color=color, description=f'Punishment Is Now Set To Ban!')
        await ctx.send(embed=embed)
    elif punishment.lower() == 'kick':
        db.update_one({ "guild_id": ctx.guild.id }, { "$set": { "punishment": "kick"}})
        embed = discord.Embed(title='Radiant', color=color, description=f'Punishment Is Now Set To Kick!')
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='Radiant', color=color, description=f'Invalid Form O Punishment, Available  Forms Of Punishments Are Ban And Kick!')
        await ctx.send(embed=embed)






@client.command()
@commands.cooldown(1,5, commands.BucketType.guild)
@commands.has_permissions(kick_members = True)
async def kick(ctx, member:discord.Member=None, *, reason = "unspecified reason"):
    if member == None:
      await ctx.send("Please specify a user for me to kick!")
      return
    if member.id == ctx.author.id:
        await ctx.send("You cannot kick yourself, sorry! ")
        return
    
    if member.top_role >= ctx.author.top_role:
        await ctx.send(f"You can not kick a user with a higher role than you!")         
        return

    else: 
        await member.ban(reason = f"\nkick Command Used By {ctx.author.name}#{ctx.author.discriminator}")
        reasonEmbed = discord.Embed(description = f'Succesfully kicked {member.mention} for {reason}\n \n ',color = color)
        reasonEmbed.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url='{}'.format(member.avatar_url))
        reasonEmbed.set_footer(text=f"kicked by {ctx.author.name}", icon_url = '{}'.format(ctx.author.avatar_url))
        await ctx.send(embed=reasonEmbed)



@client.command()
@commands.cooldown(1,5, commands.BucketType.guild)
@commands.has_permissions(ban_members = True)
async def ban(ctx, member:discord.Member=None, *, reason = "unspecified reason"):
    if member == None:
      await ctx.send("Please specify a user for me to ban!")
      return
    if member.id == ctx.author.id:
        await ctx.send("You cannot ban yourself!")
        return
    
    if member.top_role >= ctx.author.top_role:
        await ctx.send(f"You can not ban a user with a higher role than you!")         
        return
    else: 
        await member.ban(reason = f"\nBan Command Used By {ctx.author.name}#{ctx.author.discriminator}")
        reasonEmbed = discord.Embed(description = f'Succesfully banned {member.mention} for {reason}\n \n ',color = color)
        reasonEmbed.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url='{}'.format(member.avatar_url))
        reasonEmbed.set_footer(text=f"Banned by {ctx.author.name}", icon_url = '{}'.format(ctx.author.avatar_url))
        await ctx.send(embed=reasonEmbed)


@client.command(aliases=["massunban"])
@commands.has_permissions(ban_members=True)
@commands.cooldown(1,60, commands.BucketType.guild)
async def unbanall(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    bans = 0 
    unbanned = 0
    banlist = await ctx.guild.bans()
    idktbh = len(banlist)
    if idktbh == 0:
      await ctx.send("There is no banned users in this server for me to unban!")
      return
    else:
      embed = discord.Embed(title='Unbanall', color=color, description=f'Unbanning Users...')
      msg = await ctx.send(embed=embed)

      for users in banlist:
        bans += 1
        await ctx.guild.unban(user=users.user) 
        unbanned += 1
      embed1 = discord.Embed(title='Unbanall', color=color, description=f'**Unbanned {unbanned} Members!**')
      await ctx.send(embed=embed1)
    


@client.command(aliases=["h1"])
@commands.cooldown(1,5, commands.BucketType.user)
async def help1(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    embed = discord.Embed(title=f"**Radiants Help Command**", description= 'Invite me [__here__](https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)', color=color)
    embed.add_field(name=f'**Modules**',value='''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
 ```1 | Moderation Commands
2 | Fun Commands
3 | Info Commands
4 | Anti-Nuke
5 | Welcoming System
6 | Economy ```''')
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
@client.command(aliases=["welcomingsystem"])
@commands.cooldown(1,5, commands.BucketType.user)
async def welcoming(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    embed = discord.Embed(title='**Radiant Welcoming System**', color=color)
    embed.add_field(name="Modules: ", value= 
  f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
  ```1 | Welcchannel <channel>
2 | welcmsg <message>
3 | welctest```''')
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@client.command(aliases=["moderation"]) 
@commands.cooldown(1,5, commands.BucketType.user)
async def mod(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
   embed = discord.Embed(title="**Radiants Moderation Commands**",description= 'Invite me [here](https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)', color = color) 
   embed.add_field(name=f'''**Moderation Commands**''', value=f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
   ```1 | ban <user> [reason]
2 | kick <user> [reason]
3 | unbanall
4 | mute <user> [reason]
5 | unmute <user>
6 | purge <amount
7 | nuke
8 | slowmode <amount>
9 | autorole <role>
10| setup
11| lock
12| unlock
13| toggle <module>
14| role <user> <role>```''')
   embed.set_thumbnail(url=ctx.guild.icon_url)
   embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
   await ctx.send(embed=embed)


@client.command(aliases=["u"]) 
@commands.cooldown(1,5, commands.BucketType.user)
async def utility(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
   embed = discord.Embed(title="**Radiants Info Commands**",description= 'Invite me [here](https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)', color = color) 
   embed.add_field(name=f'''**utility Commands**''', value=f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
   ```1 | membercount 
2 | av <user>
3 | ping
4 | Serverbanner
5 | Servericon
6 | whois <user>
7 | serverinfo
8 | botinfo
9 | uptime
10| afk [reason]```''')  
   embed.set_thumbnail(url=ctx.guild.icon_url)
   embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
   await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def animals(ctx):
    if ctx.author.id in blacklisted:
      return
    else:
     embed1 = discord.Embed(title=f"**Radiants Help Command**", description= 'Invite me [__here__](https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)', color=color)
     embed1.add_field(name=f'**Modules**',value='''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
   ```1 | racoon
2 | fox
3 | bear
4 | koala
5 | kangaroo
6 | dog
7 | cat
8 | duck```''')
    embed1.set_thumbnail(url=ctx.guild.icon_url)
    embed1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed1)

@client.command()
@commands.cooldown(1,5, commands.BucketType.user) 
async def fun(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
   embed = discord.Embed(title="**Radiants Fun Commands**",description= 'Invite me [here](https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)', color = color) 
   embed.add_field(name=f'''**Fun Commands**''', value=f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
  ```1 | hug <user>
2 | slap <user>
3 | kiss <user>
4 | tickle <user>
5 | 8ball <user>
6 | snipe 
7 | coinflip 
8 | pp <user>
9 | hug <user>
10| coinflip```''') 
   embed.set_thumbnail(url=ctx.guild.icon_url)
   embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
   await ctx.send(embed=embed)

  
@client.command(aliases=["antinuke", "anti-nuke"]) 
@commands.cooldown(1,5, commands.BucketType.user)
async def anti(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
   embed = discord.Embed(title="**Radiants Anti-Nuke Commands**",description= 'Invite me [here](https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)', color = color) 
   embed.add_field(name=f'''**Anti-Nuke Commands**''', value=f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
  ```1 | whitelist <user>
2 | unwhitelist <user>
3 | whitelisted 
4 | Punishment <punishment>
5 | toggle <module>
6 | logs```''')
   embed.set_thumbnail(url=ctx.guild.icon_url)
   embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
   await ctx.send(embed=embed)

@client.command() 
@commands.cooldown(1,5, commands.BucketType.user)
async def economy(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    embed = discord.Embed(title='**Radiant Economy Commands**', color=color)
    embed.add_field(name="Economy Commands: ", value= 
  f'''
Use The Reactions Bellow To Go Threw The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
  ```1 | bal
2 | withdraw
3 | rob
4 | deposit
5 | leaderboard
6 | send
7 | beg```''')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
snipe_message_content = None
snipe_message_author = None
snipe_message_id = None
snipe_message_discriminator = None

@client.command(aliases=["sc", "serverpfp"])
@commands.cooldown(1,15, commands.BucketType.user)
async def servericon(ctx):
    if ctx.author.id in blacklisted:
      return
    else:
      embed = discord.Embed()
      embed.set_image(url=ctx.guild.icon_url)
      await ctx.send(embed=embed)

#@client.event
#async def on_message_delete(message):
#
 #   global snipe_message_content
  #  global snipe_message_author
   # global snipe_message_id
    #global snipe_message_discriminator

 #   snipe_message_content = message.content
  #  snipe_message_author = message.author.name
   # snipe_message_discriminator = message.author.discriminator
    #snipe_message_id = message.id
 #   await asyncio.sleep(60)

  #  if message.id == snipe_message_id:
   #     snipe_message_author = None
    #    snipe_message_content = None
     #   snipe_message_id = None



#@client.command(aliases=["s"])
#@commands.cooldown(1,5, commands.BucketType.user)
#async def snipe(message): 
#  if message.author.id in blacklisted:
 #   return
  #else:
   # if snipe_message_content==None:
    #    embed = discord.Embed(title=f"Radiant", description="There is Noting To Snipe.")
     #   embed.set_footer(text=f"Requested by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      #  await message.channel.send(embed=embed)
#    else:
 #       embed = discord.Embed(description=f"{snipe_message_content}")
  #      embed.set_footer(text=f"Requested by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
   #     embed.set_author(name= f"Sniped Message By: {snipe_message_author}#{snipe_message_discriminator}")
    #    await message.channel.send(embed=embed)
     #   return
      #  print(f"{message.author.name} executed a command")


@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@client.command(aliases=["s"])
@commands.cooldown(1,5, commands.BucketType.user)
async def snipe(ctx):
    try:
      if ctx.author.id in blacklisted:
        return
      else:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]
        
    except:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents, color=color, timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)




@client.command(aliases=['r'])
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(manage_roles=True)
async def role(ctx, member : discord.Member=None, *, role : discord.Role):
  try:
    if ctx.author.id in blacklisted:
        return
    else:
      if member is None:
        embed0 = discord.Embed(title = "Missing Argument", description=f"Missing Argument, Correct Use Is ,role (user) (role)", color=color)
        await ctx.message.reply(embed = embed0, mention_author=False) 
        return
      else:
        if role.position >= ctx.guild.me.top_role.position:
          embedidk= discord.Embed(title="Radiant",description=f"My Role Is Under {role.name} Please Pull My Role Up To Be Able To Use This Command", color=color)
          await ctx.message.reply(embed = embedidk, mention_author=False) 
          return 
        if ctx.author.id == ctx.guild.owner.id:
          if role in member.roles:
              await member.remove_roles(role, reason=f"Role Command Used By {ctx.author.name}#{ctx.author.discriminator}") 
              embed = discord.Embed(title = "Radiant", description=f"Removed the role {role.name} from {member.name}", color=color) 
              await ctx.send(embed=embed)
              return
          else:
              await member.add_roles(role, reason=f"Role Command Used By {ctx.author.name}#{ctx.author.discriminator}") 
              embed1 = discord.Embed(title = "Radiant", description=f"Gave the role {role.name} to {member.name}", color=color)
              await ctx.send(embed=embed1)
              return  
        else:
          if role.position > ctx.author.top_role.position:
              embedbored = discord.Embed(title = "Radiant", description=f"That Role Is Above You!", color=color) 
              await ctx.send(embed=embedbored)
              return
          if role == ctx.author.top_role.position:
              embedbored1 = discord.Embed(title = "Radiant", description=f"That Role Is The Same Position As Your Top Role!", color=color) 
              await ctx.send(embed=embedbored1)
              return   
          else:
              if role in member.roles:
                  await member.remove_roles(role, reason=f"Role Command Used By {ctx.author.name}#{ctx.author.discriminator}") 
                  embed1 = discord.Embed(title = "Radiant", description=f"Removed the role {role.name} from {member.name}", color=color) 
                  await ctx.send(embed=embed1)
                  return
              else:
                  await member.add_roles(role, reason=f"Role Command Used By {ctx.author.name}#{ctx.author.discriminator}") 
                  embed2 = discord.Embed(title = "Radiant", description=f"Gave the tole {role.name} to {member.name}", color=color)
                  await ctx.send(embed=embed2) 
                  return
  except Exception as e:
    print(e)

@client.command(aliases=["si"])
@commands.cooldown(1,10, commands.BucketType.user)
async def serverinfo(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    embed = discord.Embed(title='Server Info', color=color)
    embed.add_field(name="Server ID", value=f'{ctx.guild.id}')
    embed.add_field(name="Server Name", value=f'{ctx.guild.name}')
    embed.add_field(name="Server Owner", value=f'{ctx.guild.owner}')
    embed.add_field(name="Creation Date", value=f'{ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p")}', inline=True)
    embed.add_field(name="Membercount", value=f'{len(ctx.guild.members)}')
    embed.add_field(name="Role Amount", value=f'{len(ctx.guild.roles)}')
    embed.add_field(name="Channel Amount", value=f'{len(ctx.guild.channels)}')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.message.reply(embed = embed, mention_author=False) 
    print(f"{ctx.author.name} executed a cmd")

@client.command(aliases=["bi2"])
@commands.cooldown(1,10, commands.BucketType.user)
async def botinfo2(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    embed = discord.Embed(title=f'Radiant', url = 'https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot',description ='More info about Radiant:',inline=True, color=color)
    embed.add_field(name=f'Version', value='`1.0`', inline=True)
    embed.add_field(name='Library',value=f'`discord.py`', inline=True)
    embed.add_field(name='Creators',value=f'`Veltz, vert`', inline=True)
    embed.add_field(name='Guilds and Users', value=f'Users: `{len(set(client.get_all_members()))}`\nTotal Guilds: `{len(client.guilds)}`',inline=True)
    embed.add_field(name='Prefix', value=f"Prefix: `,`", inline=True)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    print(f"{ctx.author.name} executed a command")

@client.command(aliases=["bi3", "stats3"])
@commands.cooldown(1,5, commands.BucketType.user)
async def botinfo3(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    embed = discord.Embed(title=f'Radiant', url = 'https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot',description ='More info about Radiant:',inline=True, color=color)

    embed.add_field(name='<:developerbadge1:861204989174087691> __Developers__:', value="<@712969671766442024>\n<@757931086998274089>\n",inline=True)
    embed.add_field(name='<:online1:862212467034554368> __Status__:', value="Online",inline=True)
    embed.add_field(name='<:dpy1:862217428674412564> __Library__:', value="Discord.Py",inline=True)
    embed.add_field(name='__Total Guilds__:', value=f"{len(client.guilds)} Guilds",inline=True)
    embed.add_field(name='__Total Users__:', value=f"{len(set(client.get_all_members()))} Users",inline=True)
    embed.add_field(name='__prefix__:', value=f',', inline=True)
    embed.add_field(name='__Invite Link__:', value=f"[__here__](https://discord.com/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)",inline=True)
    embed.add_field(name='__Support Server__:', value=f"[__here__](https://discord.gg/antinuke)",inline=True)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    print(f"{ctx.author.name} executed a command")

@client.command(aliases=["bi", "stats"])
@commands.cooldown(1, 5, commands.BucketType.user)
async def botinfo(ctx):
  try: 
    if ctx.author.id in blacklisted:
      return
    else: 
      embed=discord.Embed(title = "Radiant", url = "https://discord.gg/e6dqdZzFxu", description=f"""
      ```asciidoc\nGuilds   :: {len(client.guilds)}\nUsers    :: {len(set(client.get_all_members()))}\nLibrary  :: Dpy\nDevs     :: Veltz#0001, vert#7000, Claqz#6666```\n\n \n\n```asciidoc\nPrefix  :: ,\nStatus  :: Online\nDpy     :: 1.7.3\nCmds    :: {len(client.commands)}```
      """,color=color)
      embed.add_field(name='__Invite Link__:', value=f"[__here__](https://discord.com/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)",inline=True)
      embed.add_field(name='__Support Server__:', value=f"[__here__](https://discord.gg/e6dqdZzFxu)",inline=True)
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.message.reply(embed = embed, mention_author=False) 
      print(f"{ctx.author.name} executed a botinfo command")
  except Exception as e:
    print(e)

@client.command(aliases=['mc', 'membercount'])
@commands.cooldown(1,5, commands.BucketType.user)
async def members(ctx):
  try: 
    if ctx.author.id in blacklisted:
      return
    else: 
      total = len(ctx.guild.members)
      online = len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members)))
      idle = len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members)))
      dnd = len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members)))
      offline = len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))
      humans = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
      bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
      embed=discord.Embed(title = f"{ctx.guild.name} Member Count:", description=f"""
      ```asciidoc\ntotal    :: {total}\nonline   :: {online}\nidle     :: {idle}\ndnd      :: {dnd}\noffline  :: {offline}\nhumans   :: {humans}\nbots     :: {bots}```
      """, color=color)
      await ctx.message.reply(embed = embed, mention_author=False) 
  except Exception as e:
    print(e)

#@client.command()
#@commands.cooldown(1, 60, commands.BucketType.user)
#@commands.has_permissions(administrator=True)
#async def pfps(ctx):
 # members = (client.get_all_members())
  #for member in members:
   # print("i am about to send pfps")
    #await asyncio.sleep(4)
   # await ctx.send(member.avatar_url)
   # print("i sent a pfp")

lol = "https://"  

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)
@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def restart(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    if ctx.author.id == 712969671766442024 or ctx.author.id == 757931086998274089:
      await ctx.send("Restarting Radiant")
      restart_bot()
    else:
      return
  
@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def afk(ctx, reason : str=None, * , member: discord.Member=None):
  if ctx.author.id in blacklisted:
    return
  else:
    if reason == None:
        reason = 'No Reason Specifed'
    current_nick = ctx.author.nick
    embed = discord.Embed(color=color)
    embed.title="AFK"
    embed.description=f"{ctx.author.mention} Is Now Afk | {reason}"
    await ctx.send(embed=embed)
    await ctx.author.edit(nick=f"[AFK] {ctx.author.name}") 

    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    embed = discord.Embed(color=color)
    embed.title="AFK"
    await ctx.author.edit(nick=current_nick)
    embed.description=f"{ctx.author.mention} u are no longer afk!"
    await ctx.send(embed=embed)
    while ctx.author is afk:
        if member.mentioned_in(msg):
          await ctx.send(f"{member.name} Is Afk | {reason}")



#@client.event
#@commands.cooldown(1,10, commands.BucketType.user)
#async def on_message(message):
 # if message.author.id in blacklisted:
  #  return
#  else:
 #   await client.process_commands(message)
  #  if message.author.bot:
   #   return
    #if message.content ==  ('radiant'):
     #   await message.channel.send(f'Hello There {message.author.mention}! My prefix is , do ,help to see my commands and ,invite to invite me! If you have any more questions make sure to join my support server  <a:zumilkdancer:861189874908135444>')
#    if message.content ==  ('@radiant'):
 #       await message.channel.send(f'Hello There {message.author.mention}! My prefix is , do ,help to see my commands and ,invite to invite me! If you have any more questions make sure to join my support server  <a:zumilkdancer:861189874908135444>')
    #if message.content == ('radiantK'):
        #await message.channel.send(f'{message.author.name}K')
    #if message.content == ('bad bot'):
       # await message.channel.send(f'{message.author.mention} no big man')
    #if message.content == ('good bot'):
        #await message.channel.send(f'{message.author.mention} Thanks!, but you havent added me to your server yet :sob:')
    #if message.content.startswith('https'):()
    #await message.delete()
    #await message.channel.send(f"{message.author.mention} Please dont send links!")



@client.command()
@commands.cooldown(1,15, commands.BucketType.user)
async def bug(ctx, *, message=None):
  if ctx.author.id in blacklisted:
    return
  else:
    if message == None:
      embed = discord.Embed(title="",description="Please do ,bug (the bug you want to report) for this command to work", color=color)
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(title="",description="Thank you for reporting this bug our developer will try to fix this bug", color=color) 
      await ctx.send(embed=embed)

      channel = client.get_channel(866282279445725184)
      embed2 = discord.Embed(title=f"Bug reported by {ctx.author.name}#  {ctx.author.discriminator}",description=f"bug = **{message}**\n Server = **{ctx.guild.name}**",color=color)
      await channel.send(embed=embed2)

@client.command()
@commands.cooldown(1,7, commands.BucketType.guild)
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds):
  if ctx.author.id in blacklisted:
    return
  else:
    await ctx.channel.edit(slowmode_delay=seconds)
    embed = discord.Embed(title='Radiant',description=f"Set Slowmode To {seconds}",color=color)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.message.reply(embed = embed, mention_author=False) 


@client.command(aliases=["inv"])
@commands.cooldown(1,5, commands.BucketType.user)
async def invite(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    embed = discord.Embed(title='**Radiant**', color=color)
    embed.add_field(name="Support: ", value= 
  f'''1 | Invite Me [__here__](https://discord.com/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)
2 | Join My Support Server [__here__](https://discord.gg/e6dqdZzFxu)
3 | Upvote Me [__here__](https://discordbotlist.com/bots/radiant-7353) And [__here__](https://top.gg/bot/860800812031410186)''')
    await ctx.message.reply(embed = embed, mention_author=False) 

@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def upvote(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    embed = discord.Embed(title='**Radiant**', color=color)
    embed.add_field(name="Support: ", value= 
  f'''1 | Invite Me [__here__](https://discord.com/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)
2 | Join My Support Server [__here__](https://discord.gg/e6dqdZzFxu)
3 | Upvote Me [__here__](https://discordbotlist.com/bots/radiant-7353) And [__here__](https://top.gg/bot/860800812031410186)''')
    await ctx.message.reply(embed = embed, mention_author=False) 


@client.command(aliases=["nukechannel"])
@commands.has_permissions(manage_channels=True)
@commands.cooldown(1,60, commands.BucketType.guild)
async def nuke(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    channelthings = [ctx.channel.category, ctx.channel.position]
    await ctx.channel.clone()
    await ctx.channel.delete()
    embed=discord.Embed(title=f'Nuked Channel!', description=f'**Channel was nuked by {ctx.author.name}**',color=color, timestamp=ctx.message.created_at)
    embed.set_image(url="https://media2.giphy.com/media/jmSImqrm28Vdm/200.gif")
    nukedchannel = channelthings[0].text_channels[-1]
    await nukedchannel.edit(position=channelthings[1])
    await nukedchannel.send(embed=embed)

            

@client.command(aliases=["supportserver"])
@commands.cooldown(1,5, commands.BucketType.user)
async def support(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    embed = discord.Embed(title='radiant', color=color, description=f'> [__**Support Server**__](https://discord.gg/sVYqaruSYK)')
    await ctx.message.reply(embed = embed, mention_author=False) 

@client.command(aliases=["sb"])
@commands.cooldown(1,40, commands.BucketType.user)
async def serverbanner(ctx):
	try:
		embed = discord.Embed()
		embed.set_image(url=ctx.guild.banner_url)
		await ctx.message.reply(embed = embed, mention_author=False) 
	except:
		await ctx.send(f"{ctx.guild.banner_url}")
@client.command(aliases=["banned", "bannedusers"])
@commands.has_permissions(ban_members=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def banlist(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    list = await ctx.guild.bans()
    banned = ""
    count = 0

    if len(list) > 0:
        for ban in list:
            user = ban.user

            count += 1
            banned += f"\n{count} Banned user(s)\nName(s): {user.name}#{user.discriminator}\nuser id(s){user.id}\n\n"
        embed1 = discord.Embed(title=f'Radiant', url = 'https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot',description =banned, color=color)
        embed1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.message.reply(embed = embed1, mention_author=False) 
    else:
        embed2 = discord.Embed(title=f'Radiant', url = 'https://discord.com/api/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot',description ="There are no banned users for this guild", color=color)
        embed2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.message.reply(embed = embed2, mention_author=False) 

@client.command()
@commands.cooldown(1,8, commands.BucketType.user)
async def ping(ctx):
  if ctx.author.id in blacklisted:
    return
  else:
    embed = discord.Embed(title='Ping', color=color, description=f'**{int(client.latency * 1000)} Ms**')
    await ctx.message.reply(embed = embed, mention_author=False) 


@client.command(aliases=['8ball'])
@commands.cooldown(1,5, commands.BucketType.user)
async def eightball(ctx, *, question =None):
  try:
    if ctx.author.id in blacklisted:
      return
    else:
      if question == None:
        embed = discord.Embed(title='Please Specify A Question',color=color)
        await ctx.message.reply(embed = embed, mention_author=False) 
        return
      else:
        responses = [
	    "It is certain.", "It is decidedly so.", "Without a doubt.",
	    "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
	    "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
	    "Reply hazy, try again.", "Ask again later.",
	    "Better not tell you now.", "Cannot predict now.",
	    "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
	    "My sources say no.", "Outlook not so good.", "Very doubtful."
	    ]
      embed = discord.Embed(title='8ball', description=random.choice(responses), color=color)
      await ctx.message.reply(embed = embed, mention_author=False) 
  except Exception as e:
    print(e)






@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def hug(ctx, member: discord.Member):
  try:
    if ctx.author.id in blacklisted:
      return
    else:
      if member == None:
        await ctx.send("Please mention a user")
      else:
        choices = ['https://i.imgur.com/r9aU2xv.gif', 'https://i.imgur.com/wOmoeF8.gif', 'https://i.imgur.com/nrdYNtL.gif', 'https://i.imgur.com/BPLqSJC.gif', 'https://i.imgur.com/ntqYLGl.gif']
        pic = random.choice(choices)
        embed = discord.Embed(description=f"**{ctx.author.mention} Hugged {member.mention}**",color=color)
        embed.set_image(url=pic)
        await ctx.message.reply(embed = embed, mention_author=False) 
  except Exception as e:
    print(e)


@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def kiss(ctx, member: discord.Member=None):
  try:
    if ctx.author.id in blacklisted:
      return
    else:
      if member == None:
        await ctx.send("Please mention a user")
      else:
        choices = ['http://i.imgur.com/0D0Mijk.gif', 'http://i.imgur.com/TNhivqs.gif', 'http://i.imgur.com/3wv088f.gif', 'http://i.imgur.com/7mkRzr1.gif', 'http://i.imgur.com/8fEyFHe.gif']
        pic = random.choice(choices)
        embed = discord.Embed(description=f"**{ctx.author.mention} Kissed {member.mention}**",color=color)
        embed.set_image(url=pic)
        await ctx.message.reply(embed = embed, mention_author=False) 
  except Exception as e:
    print(e)



@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def slap(ctx, member: discord.Member):
  try:
    if ctx.author.id in blacklisted:
      return
    else:
      if member == None:
        await ctx.send("Please mention a user")
      else:
        choices = ['https://i.imgur.com/HYJHoG7.gif', 'https://i.imgur.com/9GxTsgl.gif', 'https://i.imgur.com/uwHDm3r.gif', 'https://i.imgur.com/mT4VjD6.gif', 'https://i.imgur.com/w66ZqGR.gif']
        pic = random.choice(choices)
        embed = discord.Embed(description=f"**{ctx.author.mention} Slapped {member.mention}**",color=color)
        embed.set_image(url=pic)
        await ctx.message.reply(embed = embed, mention_author=False) 
  except Exception as e:
    print(e)


@commands.has_permissions(manage_messages=True)
@client.command()
@commands.cooldown(1,15, commands.BucketType.user)
async def purge(ctx, amount=0):
  if ctx.author.id in blacklisted:
    return
  else:
    if amount == 0:
      embed = discord.Embed(title='Radiant', description=f"Please Specify A Amount Of Messages For Me To Purge" ,color=color,timestamp=ctx.message.created_at)
      idklol = await ctx.send(embed=embed)
    else:
      await ctx.channel.purge(limit=amount)
      embed = discord.Embed(title='Purged', description=f"Purged {amount} Message(s)",color=color,timestamp=ctx.message.created_at, delete_after=5)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      idk = await ctx.send(embed=embed)
      await asyncio.sleep(3)
      await idk.delete()



@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def tickle(ctx, member: discord.Member):
  try:
    if ctx.author.id in blacklisted:
      return
    else:
      if member == None:
        await ctx.send("Please mention a user")
      else:
        choices = ['https://media.tenor.com/images/2e3bcdc3423c4b97dbdf2225fd3d6caf/tenor.gif', 'https://media.tenor.com/images/41b8627d905cceebda978d386a796b36/tenor.gif', 'https://media.tenor.com/images/d6a0512280a84726ff8ac695a37eadbe/tenor.gif']
        pic = random.choice(choices)
        embed = discord.Embed(description=f"**{ctx.author.mention} Tickled {member.mention}**",color=color)
        embed.set_image(url=pic)
        await ctx.message.reply(embed = embed, mention_author=False)  
  except Exception as e:
    print(e)





@commands.has_permissions(manage_messages=True)
@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
async def mute(ctx, member: discord.Member=None, *, reason=None):
  if ctx.author.id in blacklisted:
    return
  else:
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if member == None:
      await ctx.message.reply("Please specify a user for me to mute", mention_author=False)
      return
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in ctx.guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)

    await member.add_roles(mutedRole, reason=reason)
    embed=discord.Embed(title=f"Muted {member}, reason = {reason}", color=color)
    await ctx.message.reply(embed = embed, mention_author=False) 

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1,5, commands.BucketType.user)
async def unmute(ctx, member: discord.Member):
  if ctx.author.id in blacklisted:
    return
  else:
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
   if member == None:
     await ctx.send("Please specify a user for me to unmute")

   await member.remove_roles(mutedRole)
   embed=discord.Embed(title=f"Unmuted {member}", color=color)
   await ctx.message.reply(embed = embed, mention_author=False) 


@client.command(aliases=["avatar"])
@commands.cooldown(1,5, commands.BucketType.user)
async def av(ctx, *, member: discord.Member=None): 
  if ctx.author.id in blacklisted:
    return
  else:
    if not member: 
        member = ctx.message.author
    userAvatar = member.avatar_url
    embed=discord.Embed(title=f"{member.name}'s avatar:", color = color)
    embed.set_image(url=userAvatar)
    await ctx.message.reply(embed = embed, mention_author=False) 

@client.event
@commands.cooldown(1,5, commands.BucketType.user)
async def on_command_error(ctx, error):#   
      if ctx.author.id in blacklisted:
        return
      else:
       if isinstance(error, commands.MissingPermissions):
           await ctx.send(f'{ctx.author.mention} it seems that you are missing the **{"".join(error.missing_perms)}** permissions')
       elif isinstance(error, commands.CommandOnCooldown):
           await ctx.send(f'{ctx.author.mention} You are on cooldown for {round(error.retry_after)} second(s)!')
       #elif isinstance(error, commands.CommandNotFound):
        #   await ctx.send("Invalid command, do ,help to see radiants commands!")
       #elif isinstance(error, commands.CommandOnCooldown):
        #    await ctx.send(f"It seems that i am missing the **{''.join(error.missing_perms)}** ")
  




    

@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def toggle(ctx,*,module=None):
  if ctx.author.id in blacklisted:
        return
  else: 
    if not db.find_one({ "guild_id": ctx.guild.id }):
        guild_ = client.get_guild(ctx.guild.id)
        radiant.new(guild_.owner.id, guild_.id)
    if module == None:
        embed = discord.Embed(title='Radiant', color=color, description=f'Please Specify A Module To Toggle')
        await ctx.message.reply(embed = embed, mention_author=False) 
    if module == "welcchannel" or module == "welcomechannel":
      db.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"welcchannel": None}})
      embed = discord.Embed(title='Radiant', color=color, description=f'I have Set The Welcome Channel To **None** If You Want To Turn It On Do ,welcchannel (Channel Id)')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.message.reply(embed = embed, mention_author=False) 
      return
    if module == "welcmsg":
      db.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"welcmsg": None}})
      embed = discord.Embed(title='Radiant', color=color, description=f'I have Set The Welcome Message To: **None**, If You Want To Turn It On Do ,welcmsg (Message)')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.message.reply(embed = embed, mention_author=False) 
      return
    #if module == "log":
     # db.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"log": None}})
      #embed = discord.Embed(title='Radiant', color=color, description=f'I have Set The Logging Channel To: **None**, If You Want To Turn It On Do ,log (Channel)')
   #   embed.set_thumbnail(url=ctx.guild.icon_url)
    #  embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
     # await ctx.send(embed=embed)
      #return
    if module == "autorole":
      db.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"autorole": None}})
      embed = discord.Embed(title='Radiant', color=color, description=f'I have Set Auto Role To **None**, Do ,autorole (role) To Set It On')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.message.reply(embed = embed, mention_author=False) 
      return
    else: 
      embed = discord.Embed(title='Radiant', color=color, description=f'Invalid Module To Toggle Please Do ,modules To See My Modules And ,settings To See The Server Settings')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.message.reply(embed = embed, mention_author=False) 
      return

  

@client.command()
@commands.cooldown(1,5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def settings(ctx):
  if ctx.author.id in blacklisted:
      return
  else:
    if not db.find_one({ "guild_id": ctx.guild.id }):
        guild_ = client.get_guild(ctx.guild.id)
        radiant.new(guild_.owner.id, guild_.id)
    embed = discord.Embed(title='Radiant', color=color)
    embed.description = 'Radiant Settings'
    punishment = db.find_one({ "guild_id": ctx.guild.id })['punishment']
    if punishment == None:
      punishment = "No Punishment Has Not Been Set Yet"
    #log = discord.utils.get(ctx.guild.channels, name=f'radiant-logs')
    #if log == None:
     # log = "Logging Has Not Been Setup Yet, Do ,logs To Set It Up."
    welcchannel= db.find_one({ "guild_id": ctx.guild.id })['welcchannel']
    if welcchannel == None:
      welcchannel = "No Welcome Channel Has Not Been Set Yet"
    else:
      welcchannel = f"<#{welcchannel}>"
    welcmsg= db.find_one({ "guild_id": ctx.guild.id })['welcmsg']
    if welcmsg == None: 
      welcmsg = "No Welcome Message Has Not Been Set Yet"
    autoroleid = db.find_one({ "guild_id": ctx.guild.id })['autorole']
    if autoroleid == None:
      autoroleid = "No Autorole Has Not Been Set Yet"
    else:
      autoroleid = f"<@{autoroleid}>"
    embed.add_field(name='__Punishment__:', value=f'{punishment}')
    embed.add_field(name='__Welcome Channel__', value=f'{welcchannel}')
    embed.add_field(name='__Welcome Message__', value=f'{welcmsg}')
    embed.add_field(name='__Autorole__', value=f'{autoroleid}')
    embed.add_field(name='__prefix__:', value=f''', 
                                                    <@860800812031410186>''')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.message.reply(embed = embed, mention_author=False) 

@client.command() 
@commands.cooldown(1,5, commands.BucketType.user) 
async def prefix(ctx):
  if ctx.author.id in blacklisted:
        return
  else:
    embed = discord.Embed(title='**Radiants Prefixes:**', description = f",\n\n<@860800812031410186>", color=color)
    await ctx.message.reply(embed = embed, mention_author=False) 

@client.command(aliases=["m", "module"])
@commands.cooldown(1,10, commands.BucketType.user) 
@commands.has_permissions(administrator=True)
async def modules(ctx):
  if ctx.author.id in blacklisted:
        return
  else:
    embed = discord.Embed(title='**Radiant Anti-Nuke Modules**', color=color)
    embed.add_field(name="Modules: ", value= 
  f'''1. welcchannel
2. welcmsg
3. autorole''')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name='__Support Server__:', value=f"[__here__](https://discord.gg/sVYqaruSYK)", inline=False)
    embed.add_field(name='__Invite Link__:', value=f"[__here__](https://discord.com/oauth2/authorize?client_id=860800812031410186&permissions=8&scope=bot)", inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.message.reply(embed = embed, mention_author=False) 

@client.command() 
@commands.cooldown(1,5, commands.BucketType.user)
async def poll(ctx, *, pollqs=None):
  if ctx.author.id in blacklisted:
        return
  else:
    if pollqs == None:
      await ctx.send("Please Specify A Question")
    else:
      embed = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} Asks:",description = pollqs, color=color)
      message = await ctx.send(embed=embed)
      await message.add_reaction("👍")
      await message.add_reaction("👎")


@client.command(aliases=["balance"])
@commands.cooldown(1,5, commands.BucketType.user)
async def bal(ctx, *, member: discord.Member=None): 
  if ctx.author.id in blacklisted:
        return
  else:
    if not member: 
      member = ctx.message.author
      await open_account(member)
    
    users = await get_bank_data()

    walletmoney = users[str(member.id)]["wallet"]

    bankmoney = users[str(member.id)]["bank"]

    embed = discord.Embed(title=f"{member.name}'s balance", color=color)
    embed.add_field(name= "Wallet:", value=f"⏣ {walletmoney}")
    embed.add_field(name= "Bank:", value=f"⏣ {bankmoney}")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)




@client.command()
@commands.cooldown(1,10, commands.BucketType.user)
async def beg(ctx):
  if ctx.author.id in blacklisted:
        return
  else:
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    givers = ["Obama", "Lana Rhoades", "Mia Khalifa", "Donald Trump", "Osama Bin Laden", "Johnny Sins", "Joe Biden"]
    randomgiver = random.choice(givers)
    earnings = random.randrange(500)
    responses = [f"Stop Begging Smh, Here have **⏣ {earnings}** You Seem Really Broke.", f"awww you poor little beggar, Here Take **⏣ {earnings}**.", f"honestly why are you even begging, get a job, this is the only time i will give u money smh, Here Take **⏣ {earnings}**."] 
    lmfao = random.choice(responses)
    embed = discord.Embed(title=f"From: {randomgiver}", description= f"{lmfao}", color=color )
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

    users[str(user.id)]["wallet"] += earnings

    with open("money.json", "w") as f:
        json.dump(users,f)



@client.command()
@commands.cooldown(1,10, commands.BucketType.user)
async def withdraw(ctx,amount = None):
  if ctx.author.id in blacklisted:
        return
  else:
    await open_account(ctx.author)
    if amount == None:
        embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'Please Specify A Amount Of Money To Withdraw')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount>bal[1]:
        embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'You Dont Have That Amount of Money{ctx.author.mention}')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return
    if amount<0:
        embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'Amount Of Money Must Be Positive')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")
    embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'You Withdrew **⏣ {amount}** ')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@client.command(aliases=["deposit"])
@commands.cooldown(1,10, commands.BucketType.user)
async def dep(ctx,amount = None):
  if ctx.author.id in blacklisted:
        return
  else:
    await open_account(ctx.author)
    if amount == None:
        embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'Please Specify A Amount Of Money To Deposit')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount>bal[0]:
        embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'You Dont Have That Amount of Money{ctx.author.mention}')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return
    if amount<0:
        embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'Amount Of Money Must Be Positive')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return
    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")

    embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'You Deposited **⏣ {amount}** ')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command(aliases=["give", "send"])
@commands.cooldown(1,10, commands.BucketType.user)
async def pay(ctx,member: discord.Member, amount = None):
  if ctx.author.id in blacklisted:
        return
  else:
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'Please Specify A Amount Of Money To Give')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        return

    bal = await update_bank(ctx.author)

    if amount == "all":
        amount = bal[0]


    amount = int(amount)

    if amount>bal[1]:
        embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'You Dont Have That Amount of Money{ctx.author.mention}')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.message.reply(embed = embed, mention_author=False) 
        return
    if amount<0:
        embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'Amount Of Money Must Be Positive')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.message.reply(embed = embed, mention_author=False) 
        return

    await update_bank(ctx.author,-1*amount,"bank")
    await update_bank(member,amount,"bank")

    embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'You Gave {member.mention} **⏣ {amount}**')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.message.reply(embed = embed, mention_author=False) 

@client.command(aliases=["steal"])
@commands.cooldown(1,10, commands.BucketType.user)
async def rob(ctx,member: discord.Member=None):
  if ctx.author.id in blacklisted:
        return
  else:
    if member == None:
      embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'Please specify a user to rob!')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.message.reply(embed = embed, mention_author=False) 
      return
    else:
      await open_account(ctx.author)
      await open_account(member)
   
      bal = await update_bank(member)


    earnings = random.randrange(0, bal[0])
    if bal[0]<100:
      embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'Its Not Worth It!')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.message.reply(embed = embed, mention_author=False) 
      return
    else:
        await update_bank(ctx.author,earnings)
        await update_bank(member,-1*earnings)

        embed = discord.Embed(title=f'Radiant', color=color, url='https://discord.gg/sVYqaruSYK', description=f'You Robbed {member.mention} And Got **⏣ {earnings}**!')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        await ctx.message.reply(embed = embed, mention_author=False) 


@client.command(aliases = ["lb"])
@commands.cooldown(1,5, commands.BucketType.user)
async def leaderboard(ctx, x=1):
  if ctx.author.id in blacklisted:
        return
  else:
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    embed = discord.Embed(title = f"Richest People",color =color)
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        embed.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        if index == x:
            break
        else:
            index += 1

    await ctx.message.reply(embed = embed, mention_author=False) 

async def open_account(user):

    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("money.json", "w") as f:
        json.dump(users,f)
    return True


async def get_bank_data():
    with open("money.json", "r") as f:
        users = json.load(f)
    return users




async def update_bank(user, change=0,mode = 'wallet'):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open("money.json", "w") as f:
        json.dump(users,f)
    bal = users[str(user.id)]["wallet"],users[str(user.id)]["bank"]
    return bal



#<a:success:863095257654493195>      

@client.command()
@commands.cooldown(1,3, commands.BucketType.user)
async def racoon(ctx):
  embed = discord.Embed(title="""Here's a racoon""")

  async with aiohttp.ClientSession() as cs:
   async with cs.get('https://some-random-api.ml/animal/racoon') as r:
     res = await r.json()
     embed.set_image(url=res['image'])
     embed.set_footer(text=f'Random racoons:')

     await ctx.message.reply(embed = embed, mention_author=False) 

@client.command()
@commands.cooldown(1,3, commands.BucketType.user)
async def fox(ctx):
        url = "https://randomfox.ca/floof/"
        response = requests.get(url)
        fox = response.json()

        embed = discord.Embed(color = 0x36393F)
        embed.set_image(url = fox['image'])
        await ctx.message.reply(embed = embed, mention_author=False)   

@client.command()
@commands.cooldown(1,3, commands.BucketType.user)
async def panda(ctx):
      embed = discord.Embed(title="""Here's a Panda""")

      async with aiohttp.ClientSession() as cs:
          async with cs.get('https://some-random-api.ml/animal/panda') as r:
              res = await r.json()
              embed.set_image(url=res['image'])
              embed.set_footer(text=f'Random Pandas:')

              await ctx.message.reply(embed = embed, mention_author=False) 

@client.command()
@commands.cooldown(1,3, commands.BucketType.user)
async def bear(ctx):
      embed = discord.Embed(title="""Here's a Bear""")

      async with aiohttp.ClientSession() as cs:
          async with cs.get('https://no-api-key.com/api/v1/animals/bear') as r:
              res = await r.json()
              embed.set_image(url=res['image'])
              embed.set_footer(text=f'Random Bears:')

              await ctx.message.reply(embed = embed, mention_author=False) 

@client.command()
@commands.cooldown(1,3, commands.BucketType.user)
async def kangaroo(ctx):
      embed = discord.Embed(title="""Here's a kangaroo""")

      async with aiohttp.ClientSession() as cs:
          async with cs.get('https://some-random-api.ml/animal/kangaroo') as r:
              res = await r.json()
              embed.set_image(url=res['image'])
              embed.set_footer(text=f'Random kangaroos:')

              await ctx.message.reply(embed = embed, mention_author=False) 

@client.command()
@commands.cooldown(1,3, commands.BucketType.user)
async def koala(ctx):
      embed = discord.Embed(title="""Here's a koala""")

      async with aiohttp.ClientSession() as cs:
          async with cs.get('https://some-random-api.ml/animal/koala') as r:
              res = await r.json()
              embed.set_image(url=res['image'])
              embed.set_footer(text=f'Random koalas:')

              await ctx.message.reply(embed = embed, mention_author=False) 

@client.command()
@commands.cooldown(1,3, commands.BucketType.user)
async def dog(ctx):
      embed = discord.Embed(title="""Here's a dog""")

      async with aiohttp.ClientSession() as cs:
          async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
              res = await r.json()
              embed.set_image(url=res['message'])
              embed.set_footer(text=f'Random dogs:')

              await ctx.message.reply(embed = embed, mention_author=False) 

@client.command()
@commands.cooldown(1,3, commands.BucketType.user)
async def cat(ctx):
      embed = discord.Embed(title="""Here's a cat""")

      async with aiohttp.ClientSession() as cs:
          async with cs.get('http://aws.random.cat/meow') as r:
              res = await r.json()
              embed.set_image(url=res['file'])
              embed.set_footer(text=f'Random Cats:')

              await ctx.message.reply(embed = embed, mention_author=False) 
              
@client.command()
@commands.cooldown(1,3, commands.BucketType.user)
async def duck(ctx):
        url = "https://random-d.uk/api/v1/random"
        response = requests.get(url)
        fox = response.json()

        embed = discord.Embed(colour=color)
        embed.set_image(url = fox['url'])
        await ctx.message.reply(embed = embed, mention_author=False)   