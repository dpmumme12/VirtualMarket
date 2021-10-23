from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asyncio import sleep
import aiohttp
from VirMarket_CS.models import Stocks, User_Finances
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User

###################################
### Websocket connections views ###
###################################

class StockGraphConsumer(AsyncWebsocketConsumer):
    """ Websocket that constantly sends data for a stock every second """

    async def connect(self):
        await self.accept()
        symbol = self.scope['url_route']['kwargs']['symbol']

        async with aiohttp.ClientSession() as session:

            url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token=Tsk_67f6bc30222b44d1b13725f19d0619db'

            while True:
        
                async with session.get(url) as resp:
                    response = await resp.json()
                    await self.send(json.dumps({'response': response}))
                    await sleep(1)


class UserTotalAccountBalanceConsumer(AsyncWebsocketConsumer):
    """ Websocket that constantly sends updated UserTotalAccount Balance as well 
        as the latest price for every stock they are invested in """
        
    async def connect(self):
        
        await self.accept()
        pk = self.scope['url_route']['kwargs']['pk']
        
        UninvestedBalance = await get_UninvestedBalance(pk)
        queryset =  await get_stocks(pk)
        
        user_stocks = []
        for stock in queryset:
            user_stocks.append(stock['Symbol'])

        async with aiohttp.ClientSession() as session:
            url = f"https://sandbox.iexapis.com/stable/stock/market/batch?symbols={(','.join(user_stocks))}&types=quote&token=Tsk_67f6bc30222b44d1b13725f19d0619db"
            while True:
                async with session.get(url) as resp:
                        response = await resp.json()
                        TotalAccountBalance = 0
                        for stock in queryset:
                            try:
                                TotalAccountBalance += (stock['Shares'] * response[stock['Symbol'].upper()]['quote']['latestPrice'])
                            except:
                                pass

                        TotalAccountBalance += float(UninvestedBalance)
                        await self.send(json.dumps({'TotalAccountBalance': TotalAccountBalance, 'stocks': response}))
                        await sleep(1)

@sync_to_async()
def get_stocks(pk):
    return list(Stocks.objects.filter(User_id = pk).order_by('Symbol').values())

@sync_to_async()
def get_UninvestedBalance(pk):
    user = User.objects.get(id =pk)
    return User_Finances.objects.get(User = user).Current_Balance


