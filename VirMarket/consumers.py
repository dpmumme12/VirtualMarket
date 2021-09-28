from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from asyncio import sleep
import aiohttp

class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        async with aiohttp.ClientSession() as session:

            url = 'https://sandbox.iexapis.com/stable/stock/AAPL/price?token=Tsk_67f6bc30222b44d1b13725f19d0619db'

            for i in range (1000):
        
                async with session.get(url) as resp:
                    response = await resp.json()
                    await self.send(json.dumps({'value': response}))
                    await sleep(1)