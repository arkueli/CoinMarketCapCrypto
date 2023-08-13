from django.contrib import admin
from .models import Parser

# Register Your Models Here
@admin.register(Parser)
class CryptoParserAdmin(admin.ModelAdmin):
    list_display = ('rank', 'name', 'symbol', 'market_cap', 'price', 'circulating_supply', 'volume_24h', 'one_hour', 'twenty_four_hours', 'seven_days')
    list_filter = ('rank', 'name', 'symbol', 'market_cap', 'price',  'circulating_supply', 'volume_24h', 'one_hour', 'twenty_four_hours', 'seven_days')

#admin.site.register(Parser, CryptoParserAdmin)




