import scrapy

# class NproductsSpider(scrapy.Spider):
#     name = 'nproducts'
#     allowed_domains = ['www.skincarisma.com']
#     start_urls = ['http://www.skincarisma.com/search?']

#     def parse(self, response):

#         for link in response.css('div.product-row a::attr(href)'):
#             yield response.follow(link.get(), callback=self.parse_categories)

#     def parse_categories(self, response):
#         infos = response.xpath('//div[@class="d-none d-md-block card"]')
#         for info in infos:
#             yield {
#                 'name': info.xpath('//h1[@class="card-title font-125"]//text()').get(),
#                 'brand': info.xpath('//h2[@class="font-090 d-inline-block text-muted"]//text()').get(),

#             }





class NproductsSpider(scrapy.Spider):
    name = 'nproducts'
    allowed_domains = ['skinsort.com']
    start_urls = ['https://skinsort.com/products']

    def parse(self, response):

        for link in response.css('span.text-blue-gray-900 a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categories)

        next_page = response.xpath('//a[@rel="next"]/@href').get()
        if next_page is not None: 
            yield response.follow(next_page, callback=self.parse)

    def parse_categories(self, response):
        infos = response.xpath('//div[@class="w-full flex flex-wrap lg:flex-col lg:flex-nowrap mx-auto relative"]')
        for info in infos:
            yield {
                'name': ((info.xpath('//div/h1//text()').extract())[-1]).strip(),
                'brand': info.xpath('//div/h1/span/a[@class="hover:underline"]//text()').get(),
                'type': info.xpath('//div/h3/a[@class="hover:underline"]//text()').get(),
                'ingredients': info.xpath('//a[@class="pb-0.5 mx-2 text-dark hover:underline"]//text()').getall()

            }




# response.xpath('.//a[@itemprop="url"]/@href'):



