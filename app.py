import discord
import requests
import asyncio
from flask import Flask, request

TOKEN = '6be536d6723d57eb45aea6c7ed4756911ae81015dd88d0d3a81de56df0c9b021''

class DisBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user} подключён к Discord!')
        for guild in client.guilds:
            print(
                f'{client.user} подключился к тусе:\n'
                f'{guild.name} (id: {guild.id})'
            )

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.lower() == '!help':
            await message.channel.send('''
                '''
                )

    async def


client = DisBot()
client.run(TOKEN)