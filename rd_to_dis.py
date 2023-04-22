import redis
import json
import discord
import asyncio

# 建立 Redis 连接
r = redis.Redis(host='localhost', port=6379)

#1099196072460566658

# YOURTWEET APPID
#1099198215678603315

# PUBLIC
#d9fae1ea6954e933b3cb45e3421857f754c9465aa399ac93275f2bbbccf60534

# TOKEN
DISCORD_TOKEN = 'MTA5OTE5ODIxNTY3ODYwMzMxNQ.GWjxuU.9ezlLvVQYzLbfz_Ycbkrbxd1XMrNZo6Q-Swiyc'

intents = discord.Intents(messages=True)
client = discord.Client(intents=intents)


# channel_id
channel_id = "1099196160549326908"
async def read_queue():
    while True:
        # get latest tweet from queue and delete user hash key
        tweet_json = r.rpop('tweet_queue')
        if tweet_json is not None:
            tweet_dict = json.loads(tweet_json)
            for user_hash, tweet in tweet_dict.items():
                # send tweet to discord server
                channel = client.get_channel(channel_id)
                await channel.send(f"User {tweet['username']} said: {tweet['content']}")
                # remove hash key from Redis
                r.delete(user_hash)
                print(f"{user_hash} deleted from Redis")
        else:
            print("No tweets in the queue.")
            break
        
        # wait for a while before trying again
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    # start reading the tweet queue
    await read_queue()

client.run(DISCORD_TOKEN)

