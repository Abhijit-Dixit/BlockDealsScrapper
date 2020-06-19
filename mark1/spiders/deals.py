# -*- coding: utf-8 -*-
import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['https://www.moneycontrol.com/stocks/marketstats/bulk-deals/nse/']
    start_urls = ['https://www.moneycontrol.com/stocks/marketstats/bulk-deals/nse/']

    def parse(self, response):
        rows=response.xpath('//*[@class="fidi_tbl MB20 bulkdls1 CTR"]/table/tbody/tr')
        for row in rows:
            l1=row.xpath('./td/text()').extract()
            l2=row.xpath('./td/span/text()').extract()
            s="";
            for c in l1[3]:
                if c!=',':
                    s+=c
            print("Stock: ",l2[0])
            print("Action: ",l2[1])
            print("Txn Val: ",float(l1[2])*float(s))
            print('\n')

