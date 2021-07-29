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
from discord.utils import find
import datetime
os.system("pip install dnspython")
os.system("pip install dnspython")
color = 0x2f3136
intents=discord.Intents.all()
intents.members = True


class Antinuke(commands.Cog):
    def __init__(self, client):
        self.client = client


    mongodb = pymongo.MongoClient('mongodb+srv://radiant:@radiantbot.jrkmc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = mongodb.get_database("radiant").get_collection("servers")




    @commands.Cog.listener() 
    async def on_member_ban(self, guild, member):
     try:
        
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
        logs = logs[0]
        reason = "Banning Member As Non-Whitelisted User"
        whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        punishment = self.db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Radiant Anti-Nuke  | {reason}")
                return
            except:
              pass
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Radiant Anti-Nuke | {reason}")
                return
            except:
              pass
     except:
       pass
 


    @commands.Cog.listener() 
    async def on_emoji_update(self, emoji):
     try:
        guild = emoji.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.emoji_update).flatten()
        logs = logs[0]
        reason = "Updating Emojis As Non-Whitelisted User"
        whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        punishment = self.db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Radiant Anti-Nuke  | {reason}")
                return
            except:
              pass
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Radiant Anti-Nuke | {reason}")
                return
            except:
              pass
     except:
       pass
    @commands.Cog.listener() 
    async def on_member_remove(self, member):
      try:
        
        guild = member.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.kick).flatten()
        logs = logs[0]
        reason = "Kicking Members As Non-Whitelisted User"
        whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        punishment = self.db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Radiant Anti-Nuke  | {reason}")
                return
            except:
              pass
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Radiant Anti-Nuke | {reason}")
                return
            except:
              pass
      except:
       pass







    @commands.Cog.listener() 
    async def on_guild_channel_delete(self,channel):
       try:
        guild = channel.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete).flatten()
        logs = logs[0]
        reason = "Channel Deleted As Non-Whitelisted User"
        whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        punishment = self.db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Radiant Anti-Nuke | {reason}")
                return
            except:
                pass
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Radiant Anti-Nuke | {reason}")
                return
            except:
                pass
       except:
          pass    




    @commands.Cog.listener() 
    async def on_guild_role_delete(self,role):
      try:
        guild = role.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete).flatten()
        logs = logs[0]
        reason = "Role Deleted As Non-Whitelisted User"
        whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        punishment = self.db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Radiant Anti-Nuke | {reason}")
                return
            except:
                pass
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Radiant Anti-Nuke | {reason}")
                return
            except:
                pass
      except:
       pass 

    @commands.Cog.listener() 
    async def on_guild_channel_create(self, channel):
      try:
        guild = channel.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create).flatten()
        logs = logs[0]
        reason = "Channel Created As Non-Whitelisted User"
        whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return   
        punishment = self.db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Radiant Anti-Nuke | {reason}")
                await channel.delete()
                return
            except:
              pass
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Radiant Anti-Nuke | {reason}")
                await channel.delete()
                return
            except:
              pass
      except:
       pass   


    @commands.Cog.listener() 
    async def on_guild_role_create(self, role):
      try:
        guild = role.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create).flatten()
        logs = logs[0]
        reason = "Role Created As Non-Whitelisted User"
        whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        if logs.user.bot:
          return
        punishment = self.db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Radiant Anti-Nuke | {reason}")
                await role.delete()
                return
            except:
              pass
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Radiant Anti-Nuke | {reason}")
                await role.delete()
                return
            except:
                pass
      except:
          pass   





    @commands.Cog.listener()  
    async def on_member_join(self, member):
      guild = member.guild
      try:
        guild = member.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add).flatten()
        logs = logs[0]
        reason = "Adding Bot As Non-Whitelisted User"
        whitelisted = self.db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        else:
          if member.bot:
            await member.ban(reason=f"Radiant Anti-Nuke | {reason}")
            punishment = self.db.find_one({ "guild_id": guild.id })['punishment']
            if punishment == 'ban':
              try:
                  await logs.user.ban(reason=f"Radiant Anti-Nuke | {reason}")
              except:
                pass
            if punishment == 'kick':
              try:
                  await logs.user.kick(reason=f"Radiant Anti-Nuke | {reason}")
              except:
                pass
          else:
            pass          
      except:
       pass
    
