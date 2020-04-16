import scrapy
from scrapy.cmdline import execute
from tutorial.items import PuppyItem
from tutorial.items import PuppyDeets
import sqlite3



class Spider(scrapy.Spider):
	puppies_db = "C:/Users/nfa87/OneDrive/Desktop/Development/Scrapy_Tutorial/tutorial/puppies.db"
	conn = sqlite3.connect(puppies_db)
	c = conn.cursor()

	name = "puppies"
	start_urls = ['https://ws.petango.com/webservices/adoptablesearch/wsAdoptableAnimals.aspx?species=Dog&gender=A&agegroup=UnderYear&location=&site=&onhold=A&orderby=name&colnum=3&css=http://ws.petango.com/WebServices/adoptablesearch/css/styles.css&authkey=io53xfw8b0k2ocet3yb83666507n2168taf513lkxrqe681kf8&recAmount=&detailsInPopup=No&featuredPet=Include&stageID=&wmode=opaque']

	def parse(self, response):
		self.logger.info('Parse function called on {}'.format(response.url))

		items = PuppyItem()

		#GRAB ALL TOPICAL PUPPY DETAILS
		animals = response.css("div.list-animal-info-block")
		for animal in animals:
			puppyName = animal.css('div.list-animal-name a::text').get(),
			puppy_id = animal.css('div.list-animal-id::text').get(),
			puppy_sex = animal.css('div.list-animal-sexSN::text').get(),
			puppy_breed = animal.css('div.list-animal-breed::text').get(),
			puppy_age = animal.css('div.list-animal-age::text').get(),
			puppy_link = animal.css('div.list-animal-name a::attr(href)').get()
			# puppy_link = 'https://ws.petango.com/webservices/adoptablesearch/' + animal.css('div.list-animal-name a::attr(href)').get()

			items['puppyName'] = puppyName
			items['puppy_id'] = puppy_id
			items['puppy_sex'] = puppy_sex
			items['puppy_breed'] = puppy_breed
			items['puppy_age'] = puppy_age
			items['puppy_link'] = puppy_link

			yield items

			t = (str(items['puppyName'][0]), str(items['puppy_id'][0]), str(items['puppy_sex'][0]), str(items['puppy_breed'][0]), str(items['puppy_age'][0]), str(items['puppy_link']),)
			print(t)
			s = str(items['puppy_id'][0])
			print(s)
			n = str(items['puppyName'][0])
			print(n)
			u = str(items['puppy_link'])


			# DIVE INTO DETAILS PAGE
			self.logger.info('get puppy details')
			# detail_page = str(self.c.execute("SELECT url FROM puppies WHERE id IN ('{}')".format(s)))
			# print(detail_page)
			# GO TO THE PUPPY DETAILS
			yield response.follow(puppy_link, callback=self.parse_puppy)

	def parse_puppy(self, response):
		self.logger.info('getting the details now')

		items = PuppyDeets()

		puppy = response.xpath('//*[@class="detail-table"]//tr')
		# GRAB PUPPY DETAILS
		for puppyDetails in puppy:
			puppyID = puppyDetails.xpath('//*[@id="lblID"]/text()').extract(),
			puppy_status = puppyDetails.xpath('//*[@id="lblStage"]/text()').extract(),
			puppy_intake_date = puppyDetails.xpath('//*[@id="lblIntakeDate"]/text()').extract()

			items['puppyID'] = puppyID
			items['puppy_status'] = puppy_status
			items['puppy_intake_date'] = puppy_intake_date

			yield items

execute(['scrapy','crawl','puppies'])