from django.db import models
from django.utils import timezone

# ************ For portfolio page ***************
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

# ************** For pitches page ****************
class SemesterPitch(models.Model):
	SEMESTER_CHOICES = (
		('S', 'Spring'),
		('F', 'Fall'),
	)
	semester = models.CharField(max_length=1, choices = SEMESTER_CHOICES)
	year = models.IntegerField()

	def __unicode__(self):
		semester_string= "Fall"
		if self.semester == 'S':
			semester_string = "Spring"
		semester_string += " "+str(self.year)	
		return semester_string

	def num_pitches(self):
		return self.pitch_set.count()
	num_pitches.short_description = 'Number of Pitches'


class Pitch(models.Model):
	BUY_SELL_CHOICE = (
		('B', 'Buy'),
		('S', 'Sell'),
	)
	semester = models.ForeignKey(SemesterPitch)
	#company
	company = models.CharField(max_length=1000)
	ticker = models.CharField(max_length=10)
	buy_sell = models.CharField(max_length=1, choices = BUY_SELL_CHOICE)
	#vote outcome
	pitch_date = models.DateField()
	passed = models.BooleanField()
	ESG_For = models.IntegerField()
	ESG_Against = models.IntegerField()
	Finance_For = models.IntegerField()
	Finance_Against = models.IntegerField()
	# for embedding presentation -- not required, so blank set to true
	embed_Iframe_Text = models.TextField()
	embed_Iframe_Text.blank = True;
	url_Snippet = models.TextField()
	url_Snippet.blank = True

	def __unicode__(self):
		return str(self.ticker)+" - "+str(self.company)


class PageSection(models.Model):
 	header = models.CharField(max_length=2000)
 	collapsed = models.BooleanField() 

 	def __unicode__(self):
 		return str(self.header)

class Paragraph(models.Model):
	item = models.ForeignKey(PageSection)
	header = models.CharField(max_length=3000)
	header.blank = True
	body = models.TextField()
	# it is SO annoying that I would have to do some major coding to make an inline within an inline.... so this is my ugly solution
	link_1_URL = models.URLField()
	link_1_URL.blank = True
	link_1_text = models.CharField(max_length=3000)
	link_1_text.blank = True
	
	link_2_URL = models.URLField()
	link_2_URL.blank = True
	link_2_text = models.CharField(max_length=3000)
	link_2_text.blank = True
	
	link_3_URL = models.URLField()
	link_3_URL.blank = True
	link_3_text = models.CharField(max_length=3000)
	link_3_text.blank = True
	
	link_4_URL = models.URLField()
	link_4_URL.blank = True
	link_4_text = models.CharField(max_length=3000)
	link_4_text.blank = True
	
	link_5_URL = models.URLField()
	link_5_URL.blank = True
	link_5_text = models.CharField(max_length=3000)
	link_5_text.blank = True

	def __unicode__(self):
		index = list(self.item.paragraph_set.all()).index(self)
		return str(index+1)+" of section '"+str(self.item)+"'"

#************* For education page ******************
class EducationPageSection(PageSection):
	def __unicode__(self):
		return str(self.header)

#************* For guide page ******************
class GuidePageSection(PageSection):
	def __unicode__(self):
		return str(self.header)




