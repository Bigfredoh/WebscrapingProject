import scrapy
from scrapy import Request


class NbaspiderSpider(scrapy.Spider):
    page_apha = 'a'
    name = 'nbaspider'
    start_urls = ['https://www.basketball-reference.com/players/a/']


    def parse(self, response):
        all_players =  response.css('div#div_players table tbody tr th a::attr(href)').getall()
        for player in all_players:
            link = response.urljoin(player)
            yield Request(url = link, callback=self.parse_playername)



    def parse_playername(self, response):
        pass
