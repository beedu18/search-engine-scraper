# from project_name import settings
from search_engine_scrapper import config
from scrapy import Spider, Request

# This variable stores different search engine configurations
engine = config.ENGINES

class generic_scrapper(Spider):
    global engine

    counter = 0
    
    # Pages you need to scrape
    pages = 10

    # Choose the search engine 
    # "google" "bing" "yandex" (currently only these have been configured)   
    name = "google"
    
    # Your search query
    query = "site:thehindu.com and bjp"
    
    def start_requests(self):
        url = engine[self.name]["base_url"] + self.query
        headers = engine[self.name]["header"]
        yield Request(url, headers = headers)

    def parse(self, response):
        if self.pages > 0:
            self.pages -= 1
            print(f'\n####Got New Response {self.pages}#####\n')
            results = response.css(engine[self.name]["container"])
            
            #loop through results and extract information
            for result in results:
                try:
                    title = result.css(engine[self.name]["title"]).get()
                except:
                    title = ""
                
                try:
                    date = result.css(engine[self.name]["date"]).get()
                except:
                    date = ""
                
                try:
                    link = result.css(engine[self.name]["link"]).get()
                except:
                    link = ""
                
                self.counter += 1
                yield {
                    "count": self.counter,
                    "date": date, 
                    "title": title,
                    "link": link
                }

            # 'next page' url used for pagination
            try:
                next_link = engine[self.name]["hostname"] \
                            + response.css(engine[self.name]["next_link"]).get()
    
            except Exception as e:
                print(f'Pagination Error - {e}')
                return
    
            else:
                yield Request(next_link, 
                    headers = engine[self.name]["header"], 
                    callback = self.parse)
                # print(f'\n###Link: {next_link}\n')