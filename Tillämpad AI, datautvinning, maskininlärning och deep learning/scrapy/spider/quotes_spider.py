from pathlib import Path

import scrapy

# classe per salvare le pagine html in file in locale
class QuotesSpider(scrapy.Spider):
    name = "quotes"                                                 # questo name deve essere univoco e lo si cita nei comandi

    # metodo per iniziare le request
    def start_requests(self):
        # lista degli url da visitare
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)      # yield: restituisce una lista di oggetti Request

    # metodo per salvare le pagine html in file in locale
    def parse(self, response):
        page = response.url.split("/")[-2]                          # prende l'ultimo elemento della lista
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')