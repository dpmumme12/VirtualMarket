from celery import shared_task
from celery.utils.log import get_task_logger
import requests
from django.contrib.auth.models import User

from .email import send_signup_email
from VirMarket_CS.models import User_Finance_History, Stocks, User_Finances

logger = get_task_logger(__name__)

### Backround tasks ###
@shared_task
def send_signup_email_task(username):
    logger.info("Sent signup email.")
    return send_signup_email(username)

### Scheduled tasks ###
@shared_task
def Save_Users_Current_Account_Balance():

    users = User.objects.all()

    for user in users:
        UninvestedBalance = User_Finances.objects.get(User = user).Current_Balance
        queryset =  list(Stocks.objects.filter(User_id = user.id).order_by('Symbol').values())
        
        user_stocks = []
        for stock in queryset:
            user_stocks.append(stock['Symbol'])

            
        url = f"https://sandbox.iexapis.com/stable/stock/market/batch?symbols={(','.join(user_stocks))}&types=quote&token=Tsk_67f6bc30222b44d1b13725f19d0619db"
                
                    
        response = requests.get(url).json()
        TotalAccountBalance = 0
        for stock in queryset:
            try:
                TotalAccountBalance += (stock['Shares'] * response[stock['Symbol'].upper()]['quote']['latestPrice'])
            except:
                pass

        TotalAccountBalance += float(UninvestedBalance)
        User_Finance_History.objects.create(Balance=TotalAccountBalance, User_id=user)

    return 