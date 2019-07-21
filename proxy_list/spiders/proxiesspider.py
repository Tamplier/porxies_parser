import scrapy


class ProxiesSpider(scrapy.Spider):
    name = "proxies"

    def start_requests(self):
        yield scrapy.Request(url='https://free-proxy-list.net/', callback=self.parse)

    def parse(self, response):
        table = response.css('#proxylisttable tbody tr')
        for row in table:
            yield {
                'ip': row.css('td:nth-child(1)::text').get(),
                'port': row.css('td:nth-child(2)::text').get(),
                'code': row.css('td:nth-child(3)::text').get(),
                'country': row.css('td:nth-child(4)::text').get(),
                'anonymity': row.css('td:nth-child(5)::text').get(),
                'google': row.css('td:nth-child(6)::text').get(),
                'https': row.css('td:nth-child(7)::text').get(),
                'last_checked': row.css('td:nth-child(8)::text').get().strip()
            }
