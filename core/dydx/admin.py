from django.contrib import admin
from .models import Positions,Balance,HistoryFunding, HistoryTrades, HistoryTransfers



class PositionsAdmin(admin.ModelAdmin):
    list_display = ('user','market', 'long', 'average_open','created_date')
    list_filter = ('user','long','created_date')
    search_fields = ['user', 'long']


class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user','balance','created_date')
    list_filter = ('user','balance')
    search_fields = ['user', 'balance']

admin.site.register(Positions,PositionsAdmin)
admin.site.register(Balance,BalanceAdmin)
admin.site.register(HistoryFunding)
admin.site.register(HistoryTrades)
admin.site.register(HistoryTransfers)