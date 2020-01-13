import scrapy


class ArticleSpider(scrapy.Spider):
    name = "article"
    start_urls = ['http://en.wikipedia.org/wiki/FreeNATS',
      'http://en.wikipedia.org/wiki/Network_monitoring',
      'http://en.wikipedia.org/wiki/Service-level_agreement',
      'http://en.wikipedia.org/wiki/High_availability',
      'http://en.wikipedia.org/wiki/Network_traffic_measurement']

    def parse(self, response):
        content = response.xpath(".//div[@class='mw-body-content']/descendant::text()").extract()
        yield {'webContent': ''.join(content), 'URL': ''.join(response.request.url)}
