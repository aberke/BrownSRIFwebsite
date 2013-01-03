from django.contrib import admin
from main_site.models import Stock, SemesterPitch, Pitch, EducationPageSection, GuidePageSection, Paragraph


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
	readonly_fields = ('full_name', 'URL_Snippet', 'embed_iframe',)

	def full_name(self, instance):
		return str(instance.ticker)+" - "+str(instance.company)
	full_name.short_description = "Company"

	def URL_Snippet(self,instance):
		if instance.company:
			E = 'Edit pitch details'
		return "<span>Save the powerpoint as a GoogleDoc Presentation.  In the <strong>Sharing settings</strong>, edit <strong>Who has access</strong> to make the presentation <strong>Public on the web</strong>.  From url in the browser's address bar, copy the text following <strong>../presentation/d/</strong> up to <strong>/edit...</strong>.  <p>Eg, If in the address bar you see the following url <strong>https://docs.google.com/a/brown.edu/presentation/d/1S3G5eQ6AmbPIpVnUElvD8sYzmykhXhFuvfmJ7PtjoW0/edit#slide=id.g39c5f8cf_0_25</strong>, then copy into the box below <strong>1S3G5eQ6AmbPIpVnUElvD8sYzmykhXhFuvfmJ7PtjoW0</strong>.</p><p>Alternatively, or additionally, directly embed an iframe as specified below.</p></span>"
	URL_Snippet.allow_tags=True
	URL_Snippet.short_description = "Include Powerpoint with URL snippet"

	def embed_iframe(self, instance):
		return "<span>Save the powerpoint as a GoogleDoc Presentation.  In the <strong>Sharing settings</strong>, edit <strong>Who has access</strong> to make the presentation <strong>Public on the web</strong>.  Then click on <strong>Publish to the web</strong>.  This option can be found under <strong>File</strong>.  Under <strong>Get a link to the published document</strong> set <strong>Presentation size</strong> to <strong>Small</strong>.  Take the text from the <strong>Embed code</strong> box.</span>"
	embed_iframe.short_description = "Include Powerpoint by directly embedding iframe"
	embed_iframe.allow_tags=True

	fieldsets = [
				('Edit pitch details', {'fields': [('company','ticker', 'buy_sell'), 
									('pitch_date', 'passed',), 
									('ESG_For', 'ESG_Against', 'Finance_For', 'Finance_Against'),
									'URL_Snippet', 'url_Snippet',
									'embed_iframe', 'embed_Iframe_Text',
									], 
							'classes': ('collapse',),
				}), 
			]
	model = Pitch
	extra = 1

class SemesterPitch_Admin(admin.ModelAdmin):
	list_display = ('semester', 'year', 'num_pitches')
	inlines = [PitchInLine]
	fields = ('semester','year',)

admin.site.register(SemesterPitch, SemesterPitch_Admin)

# *************** For Education/Pitch-Guide Page ***********************
class Paragraph_Admin(admin.StackedInline):
	model = Paragraph
	extra = 1
	fieldsets = [
		('Text Content', {'fields':['header','body',],
					'description': 'Provide paragraph with optional header',
			}),
		('Links', {'fields':[('link_1_URL', 'link_1_text'),
							('link_2_URL', 'link_2_text'),
							('link_3_URL', 'link_3_text'),
							('link_4_URL', 'link_4_text'),
							('link_5_URL', 'link_5_text')],
					'description': 'Provide up to 5 URLs to link to and optionally provide text to display instead of URL itself.  This text will link to the provided URL.',
			})
		]

class PageSection_Admin(admin.ModelAdmin):
	list_display = ('header',)
	fieldsets =[
		('Page Section', {'fields':['header','collapsed',],
					'description': 'Provide a header for this section and provide paragraph(s) below.  You can choose to have this section be collapsible.'
			}),
		]
	inlines = [Paragraph_Admin]
	extra = 1


admin.site.register(EducationPageSection, PageSection_Admin)
admin.site.register(GuidePageSection, PageSection_Admin)




