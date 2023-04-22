import redis
import json
import discord
from discord.ext import tasks
import asyncio
import os
import logging

from dotenv import load_dotenv
load_dotenv()

# 建立 Redis 连接
r = redis.Redis(host='localhost', port=6379)

#1099196072460566658

# YOURTWEET APPID
#1099198215678603315

# PUBLIC
#d9fae1ea6954e933b3cb45e3421857f754c9465aa399ac93275f2bbbccf60534

class DiscordClient(discord.Client):
    async def on_ready(self):
        logging.info("Logged on as %s" % self.user)
        self.every_ten_seconds.start()

    async def on_message(self, message):
        # don't respond to ourselves
        if self.user == message.author:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

    @tasks.loop(seconds=3)
    async def every_ten_seconds(self):
        if not self.is_ready():
            logging.error("Discord client not ready")
            return
        channels = self.get_all_channels()
        logging.info("All channels %s" % channels)
        for channel in channels:
            logging.info("Channel in channels %s" % channel)


        for guild in self.guilds:
            logging.info("GUID ---> %s" % guild)
            for channel in guild.text_channels:
                logging.info("CHANNEL FOR GUID: %s" % str(channel.name))
        channel_id = "1099196160549326908"
        channel_id = "1099196160549326908"
        channel_id = "1099196072460566658"
        channel = self.get_channel(channel_id)
        if not channel:
            logging.error("No channel for %s" % channel_id)
            return

        while True:
            # get latest tweet from queue and delete user hash key
            tweet_json = r.rpop('tweet_queue')
            if not tweet_json:
                break

            tweet_dict = json.loads(tweet_json)
            for user_hash, tweet in tweet_dict.items():
                await channel.send(f"User {tweet['username']} said: {tweet['content']}")
                # remove hash key from Redis
                r.delete(user_hash)
                print(f"{user_hash} deleted from Redis")
            
            # wait for a while before trying again
            await asyncio.sleep(5)

logging.basicConfig(level=logging.INFO)
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents(messages=True)
client = DiscordClient(intents=intents)
client.run(DISCORD_TOKEN)
