import scrapy
from scrapy import Request


class TotalspiderSpider(scrapy.Spider):
    name = 'nairaland'
    page_number = 0
    start_urls = ['https://www.nairaland.com/news/']

    def parse(self, response):
        links =  response.xpath('//div[@class="body"]/table[@summary="links"]/tr/td/a/@href').getall()
        for link in links:
            yield Request(url=link, callback=self.parse_categories)

        next_page = 'https://www.nairaland.com/news/' + str(TotalspiderSpider.page_number)
        if TotalspiderSpider.page_number <= 2:
            TotalspiderSpider.page_number += 1
            yield Request(url=next_page, callback=self.parse)

    def parse_categories(self, response):
        news_container = response.css('div.body')
        for content in news_container:
            yield {
                'news': content.css('p.bold a:nth-child(4)::text').get(),
                'news_category':(content.css('p.bold a:nth-child(3)::text').get()),
                'views': content.css('p.bold::text').getall(),
                'poster':content.css('a.user::text').get(),
                'time':content.css('span.s b:nth-child(1)::text').get(),
                'date':content.css('span.s b:nth-child(2)::text').get(),
                'news_link': response.urljoin(content.css('p.bold a:nth-child(4)::attr(href)').get())

            }


