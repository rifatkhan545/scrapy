import scrapy
from ..items import RealStateItem


class PropertySpider(scrapy.Spider):
    name = 'property'
    start_urls = ['https://www.propertyshare.in/commercial-properties']

    def parse(self, response):
        items = RealStateItem()
        all_content = response.css('div.info-body')
        for content in all_content:
            area = content.css('.info-content:nth-child(1) .value').css('::text').extract()
            price = content.css('.info-content:nth-child(2) .value').css('::text').extract()
            investment = content.css('.info-content:nth-child(5) .value').css('::text').extract()
            investor = content.css('.property-investment-info .title').css('::text').extract()

            items['area'] = area
            items['price'] = price
            items['investment'] = investment
            items['investor'] = investor

            yield items





