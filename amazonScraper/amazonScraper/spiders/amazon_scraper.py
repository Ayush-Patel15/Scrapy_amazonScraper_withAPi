#import statements
import scrapy
import re


#cleaning of returned values
def clean(inp):
    return re.sub('\\n','',str(inp))


#cleaning of price value
def clean_alpha(inp):
    return re.sub(r'[\\a-z]' ,'',str(inp))

#declaration of spider class
class Amazon(scrapy.Spider):
    name = 'amazon'

    def __init__(self,query):
        self.start_urls = [
            'https://www.amazon.in/s?k={0}'.format(query)
        ]

    #parsing the url to get the list of all products links
    def parse(self, response):
        list_of_products_links = response.css('.s-no-outline::attr(href)').extract()
        for each_product_link in list_of_products_links:
            search_url = response.urljoin(each_product_link)
            yield scrapy.Request(url=search_url, callback=self.each_product)

    #css selectors to yield required details of each product.
    def each_product(self,response):
        product_details = response.css('#centerCol')
        for details in product_details:
            product_title = response.css('#productTitle::text').extract()
            product_brand = response.css('#bylineInfo::text').extract()
            product_emi = response.css('.a-hidden+ span::text').extract()
            product_url = response.url
            product_description = response.css('#feature-bullets .a-list-item::text').extract()
            if response.css('#priceblock_ourprice'):
                product_price = response.css('#priceblock_ourprice::text').extract()
            elif response.css('#priceblock_dealprice'):
                product_price = response.css('#priceblock_dealprice::text').extract()
            else:
                product_price = 'NA'
                
    #filtering the yielded information using previously defined functions.
        filter_product_title = []
        for i in product_title:
            filter_product_title.append(clean(i))
        if len(product_emi)!=0:
            filter_product_emi = clean(product_emi[1])
        else:
            filter_product_emi = 'NA'
        filter_product_price =  clean_alpha(product_price)
        filter_product_description = []
        for each in product_description:
            filter_product_description.append(clean(each))

        amazon_items = {
            'Product Title' : filter_product_title,
            'Price' : filter_product_price,
            'EMI' : filter_product_emi,
            'Description' : filter_product_description,
            'Brand' : product_brand,
            'Url' : product_url
        }

        yield amazon_items