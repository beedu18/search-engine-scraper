from scrapy import FormRequest, Request, Spider
from scrapy.utils.response import open_in_browser
import json

class DDG(Spider):
    name = "ddg"
    count = 0
    def start_requests(self):
        url = "https://html.duckduckgo.com/html/"
        query = "site:cnn.com and trump"
        formdata = {"q": query, "b": ""}
        yield FormRequest(url, formdata = formdata, callback = self.parse)

    def parse(self, response):
        # open_in_browser(response)
        results = response.css("div.results")
        
        if results:
            # print(f'Results: {results}')
            for result in results:
                title = result.css("a.result__a::text").get()
                link = result.css("a.result__url::attr(href)").get()
                self.count += 1
                yield {
                    'count': self.count,
                    'title': title,
                    'link': link
                }
            
            form = None
            
            try:
                form = response.css("div.nav-link form")[-1]
            except Exception as e:
                print('####Form Exception - {e}')
                return
            
            formdata = {
                'q': form.css('input:nth-child(2)::attr(value)').get(),
                's': form.css('input:nth-child(3)::attr(value)').get(),
                'nextParams': form.css('input:nth-child(4)::attr(value)').get(),
                'v': form.css('input:nth-child(5)::attr(value)').get(),
                'o': form.css('input:nth-child(6)::attr(value)').get(),
                'dc': form.css('input:nth-child(7)::attr(value)').get(),
                'api': form.css('input:nth-child(8)::attr(value)').get(),
                'vqd': form.css('input:nth-child(9)::attr(value)').get(),
                'kl': form.css('input:nth-child(10)::attr(value)').get(),
            }

            print(f'q: {formdata["q"]} || s: {formdata["s"]} || dc: {formdata["dc"]}')

            yield FormRequest(url = "https://html.duckduckgo.com/html/", 
                                formdata = formdata,
                                callback = self.parse,
                            )
        else:
            print("Done")