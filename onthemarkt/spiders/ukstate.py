import scrapy
from ..items import UkRealstateItem


class UkstateSpider(scrapy.Spider):
    name = 'ukstate'
    start_urls = ['https://www.onthemarket.com/for-sale/property/london/']

    def parse(self, response):
        items = UkRealstateItem()
        all_content = response.css('li.property-result')
        for content in all_content:
            title = content.css('span.title').css('::text').extract()
            address = content.css('.address').css('::text').extract()
            price = content.css('a.price').css('::text').extract()
            phone = content.xpath('//*[@id="properties"]/li[2]/div[6]/span/span/strong').css('::text').extract()
            description = content.xpath('//*[@id="properties"]/li[1]/div[3]/p[3]').css('::text').extract()

            items['title'] = title
            items['address'] = address
            items['price'] = price
            items['phone'] = phone
            items['description'] = description
            yield items

            for page in range(0, 41):
                next_page = 'https://www.onthemarket.com/for-sale/property/london/'+ '?page=' + str(page)
                yield response.follow(next_page, callback = self.parse)
