ENGINES = {
    "google": {
        "base_url": "https://www.google.com/search?q=",
        "container": "div.g",
        "title": "h3.LC20lb.DKV0Md::text",
        "link": "a::attr(href)",
        "date": "span.MUxGbd.wuQ4Ob.WZ8Tjf::text",
        "hostname": "https://www.google.com",
        "next_link": "#pnnext::attr(href)",
        "header": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.5",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "cache-control": "no-cache",
        }
    },
    "bing": {
        "base_url": "https://www.bing.com/search?q=",
        "container": "li.b_algo",
        "title": "a::text",
        "link": "a::attr(href)",
        "date": "span.news_dt::text",
        "hostname": "https://www.bing.com",
        "next_link": "a.sb_pagN.sb_pagN_bp.b_widePag.sb_bp::attr(href)",        
        "header": {
            "accept":"text/html,application/xhtml+xml,application/xml", 
            "accept-language": "en-GB,en;q=0.9", 
            "cache-control": "no-cache", 
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        }
    },
    "yandex": {
        "base_url": "https://yandex.com/search/?text=",
        "container": "li.serp-item",
        "title": "div.OrganicTitle-LinkText.organic__url-text::text",
        "link": "a.Link.Link_theme_normal::attr(href)",
        "date": "",
        "hostname": "https://yandex.com",
        "next_link": "a.link.link_theme_none.link_js_inited::attr(href)",
        "header": {
            "accept":"text/html,application/xhtml+xml,application/xml", 
            "accept-language": "en-GB,en;q=0.9", 
            "cache-control": "no-cache", 
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        }
    }
}
