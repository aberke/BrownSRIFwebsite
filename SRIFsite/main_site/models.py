from django.db import models

# Create your models here.

class Stock(models.Model):
	purchase_date = models.DateField()
	company_name = models.CharField(max_length = 1000)
	ticker = models.CharField(max_length = 10)
	num_shares = models.IntegerField()
	purchase_price = models.FloatField()
	current_price = models.FloatField()
	
	def __unicode__(self):
		return self.company_name
	
	
	
	#write functions to calculate other values