# Automate_amazonScraper_with_Scrapy
Scrapy integrated with Flask Api.

An automated web scraper that extracts information as per user input.
It is integrated with Flask to genrate a path api, each time you change the path's input,
category to scrape will change.

For example : http://127.0.0.1:5000/amazonapi/laptops, http://127.0.0.1:5000/amazonapi/men shoes,
http://127.0.0.1:5000/amazonapi/helmets, http://127.0.0.1:5000/amazonapi/earbuds

As per query provided, the crawler go and crawl the whole webpages accordingly from page 1 to n.
And extracts it's Title, Price, Brand Name, Emi availability, Description and url.
Then, it uses regex to cleanup the following outputs and at last store them in a json output file to read ans display.
