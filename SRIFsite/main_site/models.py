from django.db import models
from django.utils import timezone


class Stock(models.Model):
	last_updated = models.DateField()
	purchase_date = models.DateField()
	name = models.CharField(max_length = 1000)
	ticker = models.CharField(max_length = 10)
	shares = models.IntegerField()
	purchase_price = models.FloatField()
	current_price = models.FloatField()
	
	def __unicode__(self):
		return self.name

	def purchase_value(self):
		return (self.shares)*(self.purchase_price)

	def current_value(self):
		return (self.shares)*(self.current_price)	

	def change_in_price(self):
		return (self.current_price - self.purchase_price)

	def change_in_value(self):
		return (self.change_in_price()*self.shares)

	def percent_change(self):
		return (self.change_in_price()/self.purchase_price)

	def purchase_month(self):
		return self.purchase_date.month

class Pitch_By_Semester(models.Model):
	SEMESTER_CHOICES = (
		('S', 'Spring'),
		('F', 'Fall'),
	)
	semester = models.CharField(max_length=1, choices = SEMESTER_CHOICES)
	year = models.IntegerField()

	def __unicode__(self):
		semester_string = self.semester + " "+str(self.year)	
		return semester_string

	def num_pitches(self):
		return self.pitch_set.count()
	num_pitches.short_description = 'Number of Pitches'


class Pitch(models.Model):
	BUY_SELL_CHOICE = (
		('B', 'Buy'),
		('S', 'Sell'),
	)
	PASS_FAIL_CHOICE = (
		('P', 'Pass'),
		('F', 'Fail'),
	)
	buy_sell = models.CharField(max_length=1, choices = BUY_SELL_CHOICE)
	pass_fail = models.CharField(max_length=1, choices = PASS_FAIL_CHOICE)
	semester = models.ForeignKey(Pitch_By_Semester)
	pitch_date = models.DateField()
	company = models.CharField(max_length=1000)
	ticker = models.CharField(max_length=10)
	#vote outcome
	ESG_For = models.IntegerField()
	ESG_Against = models.IntegerField()
	Finance_For = models.IntegerField()
	Finance_Against = models.IntegerField()

	url = models.URLField()


	






