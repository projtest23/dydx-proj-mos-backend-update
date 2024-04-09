from django.db import models
from django.contrib.auth.models import User


class Positions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    market = models.CharField(max_length=255,default='ETH-USD')
    long = models.BooleanField(default=True)
    size = models.FloatField()
    leverage = models.FloatField()
    realized_PL = models.FloatField()
    average_open = models.FloatField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    


class Balance(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    balance= models.FloatField()
    account_leverage = models.FloatField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    uniswap = models.BooleanField(default=True)
    wallet_address = models.CharField(max_length=500,null=True)


class HistoryTrades(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time= models.CharField(max_length=256)
    market = models.CharField(max_length=256,default='ETH-USD')
    long = models.BooleanField(default=True)
    amount = models.CharField(max_length=256)
    price = models.CharField(max_length=256)
    total = models.CharField(max_length=256)
    fee = models.CharField(max_length=256)
    TRADETYPE_CHOICES = (
        ('Liquidated', 'Liquidated'),
        ('Market', 'Market'),
    )
    LIQUIDITY_CHOICES = (
        ('Maker', 'Maker'),
        ('Taker', 'Taker'),
    )
    tradetype = models.CharField(max_length=256,choices=TRADETYPE_CHOICES)
    liquidity = models.CharField(max_length=256,choices=LIQUIDITY_CHOICES)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    creation_time = models.DateField(null=True)


class HistoryTransfers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time= models.CharField(max_length=256)
    action = models.CharField(max_length=256,default='Slow Withdraw')
    status = models.CharField(max_length=256, default='Confirmed')
    amount = models.CharField(max_length=256)
    transaction = models.CharField(max_length=500)
    transaction_link = models.CharField(max_length=500,default="https://")
    fee = models.CharField(max_length=256,default='-')
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    creation_time = models.DateField(null=True)


class HistoryFunding(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time= models.CharField(max_length=256)
    market = models.CharField(max_length=256,default='ETH-USD')
    funding_rate = models.CharField(max_length=500)
    long = models.BooleanField(default=True)
    payment = models.CharField(max_length=500)
    ppsition = models.CharField(max_length=500)
    position_asset = models.CharField(max_length=256,default='ETH')
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    creation_time = models.DateField(null=True)
