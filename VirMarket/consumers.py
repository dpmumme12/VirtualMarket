from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from asyncio import sleep
import aiohttp
from VirMarket_CS.models import Stocks
from asgiref.sync import sync_to_async
from channels.auth import login

class StockGraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print(self.scope['session'])
        print(self.scope['user'])

        async with aiohttp.ClientSession() as session:

            url = 'https://sandbox.iexapis.com/stable/stock/AAPL/price?token=Tsk_67f6bc30222b44d1b13725f19d0619db'

            for i in range (1000):
        
                async with session.get(url) as resp:
                    response = await resp.json()
                    await self.send(json.dumps({'value': response}))
                    await sleep(1)


class UserTotalAccountBalanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        
        await self.accept()
        

        pk = self.scope['url_route']['kwargs']['pk']
    
        queryset =  await get_set(pk)
        user_stocks = []
        for stock in queryset:
            user_stocks.append(stock['Symbol'])

        async with aiohttp.ClientSession() as session:
            url = f"https://sandbox.iexapis.com/stable/stock/market/batch?symbols={(','.join(user_stocks))}&types=price&token=Tsk_67f6bc30222b44d1b13725f19d0619db"
            while True:
                async with session.get(url) as resp:
                        response = await resp.json()
                        TotalAccountBalance = 0
                        for stock in queryset:
                            try:
                                TotalAccountBalance += (stock['Shares'] * response[stock['Symbol'].upper()]['price'])
                            except:
                                pass
                        await self.send(json.dumps({'price': TotalAccountBalance}))
                        await sleep(1)

@sync_to_async()
def get_set(pk):
    return list(Stocks.objects.filter(User_id = pk).order_by('Symbol').values())