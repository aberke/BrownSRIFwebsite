from django.contrib import admin
from main_site.models import Stock, Pitch_By_Semester, Pitch


class StockAdmin(admin.ModelAdmin):

	list_display = ('name', 'ticker', 'shares', 'purchase_price', 'current_price', 'percent_change', 'last_updated')

	fieldsets = [
			(None, {'fields': ['purchase_date', 'last_updated']}),
			('Company', {'fields': ['name', 'ticker']}), 
			('Shares', {'fields': ['shares']}), 
			('Price', {'fields': ['purchase_price', 'current_price']})
	]


admin.site.register(Stock, StockAdmin)


class PitchInLine(admin.StackedInline):
	model = Pitch
	extra = 1

class Pitch_By_Semester_Admin(admin.ModelAdmin):
	list_display = ('year', 'semester', 'num_pitches')
	inlines = [PitchInLine]

admin.site.register(Pitch_By_Semester, Pitch_By_Semester_Admin)
