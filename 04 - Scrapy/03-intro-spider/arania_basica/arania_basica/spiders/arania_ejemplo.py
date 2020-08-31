import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse (self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()
        precios = response.css(
            'div.product_price > p.price_color::text'
        ).extract()
        stock = response.css(
            'div.product_price > p.instock::text'
        ).extract()
        imagen = response.css(
            'div.image_container > a::attr(href)'
        ).extract()

        estrella = response.css(
            'article.product_pod > p::attr(class)'
        ).extract() 
        print(titulos)
        print(precios)
        print(stock)
        print(estrella)
  