from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from hw_3.spiders.lamoda import LamodaSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule('hw_3.settings')
    crawler_process = CrawlerProcess(settings=crawler_settings)
    crawler_process.crawl(LamodaSpider)
    crawler_process.start()
