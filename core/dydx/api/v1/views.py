
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ...models import Positions, Balance, HistoryTransfers, HistoryFunding, HistoryTrades
from .serializers import (PositionSerializer,
                          HistoryTradesSerializer,
                          HistoryFundingSerializer,
                          HistoryTransferSerializer
                        )
import yfinance as yf
from rest_framework.response import Response

class PositionsView(ListAPIView):


    permission_classes = [IsAuthenticated]
    serializer_class = PositionSerializer
    # queryset = Positions.objects.all()

    def get_queryset(self):

        queryset = Positions.objects.filter(user=self.request.user)

        return queryset
    
    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        data = list(res.data)
        user = self.request.user
        eth = yf.Ticker('ETH-USD')
        allprice = eth.history()
        price = allprice['Close'].iloc[-1]
        balancedata = Balance.objects.filter(user=user)
        if len(balancedata)<1:
            return res
        

        balancedata=balancedata[0]
        balance = balancedata.balance
        uniswap = balancedata.uniswap
        wallet = balancedata.wallet_address
        account_leverage = balancedata.account_leverage
        up_total = 0
        size_d_total = 0

        if len(data)<1:
            data_dict = {}
            data_dict['margin_usage'] = 0
            data_dict['balance'] = balance
            data_dict['uniswap'] = uniswap
            data_dict['wallet'] = wallet
            data_dict['account_leverage'] = account_leverage
            data_dict['equity'] = balance
            data_dict['bying_power'] = round((balance*20),2)
            data.append(data_dict)
            return Response(data)


        for pos in data:
            
            average_open = pos['average_open']
            size = pos['size']
            long = pos['long']
            if long :
                up = (price - average_open)* size
            else:
                up = (average_open - price)*size
            up_total += up
            size_d_total += size*price
            pos['unrealized_profit'] = round(up,2)
            size_dollar = size*price
            pos['size_dollar'] = round(size_dollar,2)
            pos['un_profit_perc'] = round((up*100/size_dollar),2)

        for pos in data:
            average_open = pos['average_open']
            size = pos['size']
            long = pos['long']
            if long :
                liq_price = average_open-(balance/size)
                up = (price - average_open)* size
            else:
                liq_price = average_open + (balance/size)
                up = (average_open - price)*size
            if liq_price <0 :
                liq_price = 0
            pos['liq_price'] = round(liq_price,2)
            pos['oracle'] = round(price,2)
            pos['bying_power'] = round((balance*20),2)
            pos['equity'] = round((balance + up_total),2) 
            pos['margin_usage'] = round(((size_d_total/account_leverage)*100/balance),2)
            pos['balance'] = balance
            pos['account_leverage'] = account_leverage
            pos['uniswap'] = uniswap
            pos['wallet'] = wallet


        return Response(data)


class HistoryTradesView(ListAPIView):


    permission_classes = [IsAuthenticated]
    serializer_class = HistoryTradesSerializer
    # queryset = Positions.objects.all()

    def get_queryset(self):

        queryset = HistoryTrades.objects.filter(user=self.request.user)

        return queryset


class HistoryTransferView(ListAPIView):


    permission_classes = [IsAuthenticated]
    serializer_class = HistoryTransferSerializer
    # queryset = Positions.objects.all()

    def get_queryset(self):

        queryset = HistoryTransfers.objects.filter(user=self.request.user)

        return queryset


class HistoryFundingView(ListAPIView):


    permission_classes = [IsAuthenticated]
    serializer_class = HistoryFundingSerializer
    # queryset = Positions.objects.all()

    def get_queryset(self):

        queryset = HistoryFunding.objects.filter(user=self.request.user)

        return queryset


    

        