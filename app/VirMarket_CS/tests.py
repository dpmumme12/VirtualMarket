from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from VirMarket_CS.models import User_Finances

####################################################################################
#### Tests all the internal API endpoints to make sure core functionality works ####
####################################################################################

class APITestCases(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    
    def test_GetStockTransaction(self):
        """Test to get transaction history for"""


        url = reverse('TransacionsAPI')
        response =  self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_PostStockTransaction(self):
        """Test to Buy and Sell stocks through this API endpoint"""


        url = reverse('TransacionsAPI')
        response =  self.client.post(url, {
            "Symbol": "AAPL",
            "Name": "APPLE",
            "Shares": 5,
            "Price": "677.63",
            "TransactionType": "BUY",
            "User_id": self.user.id
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response =  self.client.post(url, {
            "Symbol": "AAPL",
            "Name": "APPLE",
            "Shares": 5,
            "Price": "677.63",
            "TransactionType": "SELL",
            "User_id": self.user.id
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_GetStocks(self):
        """Test to get all stocks the user is currently invested in"""


        url = reverse('StocksAPI')
        response =  self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_GetUserBalance(self):
        """Test to get the user's current balance"""


        url = reverse('UserBalanceAPI')
        response =  self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_GetUserInfo(self):
        """Test to get the user's profile info"""


        url = reverse('UserInfoAPI')
        response =  self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_UpdateUserInfo(self):
        """Test to update the user's profile info"""


        url = reverse('UserInfoAPI')
        response =  self.client.put(url, {
            "username": "test.user",
            "first_name": "testing",
            "last_name": "User",
            "email": "Test@test.com"
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
