from django.contrib import admin
from main_site.models import Stock


class StockAdmin(admin.ModelAdmin):
	list_display = ('company_name', 'ticker', 'purchase_price', 'current_price')
	
admin.site.register(Stock, StockAdmin)
