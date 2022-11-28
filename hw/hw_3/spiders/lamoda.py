import scrapy
import re
from scrapy.exceptions import CloseSpider


class LamodaSpider(scrapy.Spider):
    name = 'lamoda'
    allowed_domains = ['lamoda.ru']

    # С этих адресов начнется работа метода parse
    start_urls = [
            'https://www.lamoda.ru/c/477/clothes-muzhskaya-odezhda/',
            'https://www.lamoda.ru/c/355/clothes-zhenskaya-odezhda/']

    # Селекторы для поиска ссылок на странице
    _css_selectors = {
        'items': 'div.x-product-card__card .x-product-card__link'
    }

    @staticmethod
    def _follow(response, css_selector, callback, **kwargs):
        """
        Метод используется для перехода по ссылкам, которые нашлись с помощью CSS селектора на странице.
        Я применяю его только для перехода по товарам с главной страницы, но если потребуется, можно добавить
        логику перехода по брендам/категориям и тд
        """
        for link in response.css(css_selector):
            yield response.follow(link, callback=callback, cb_kwargs=kwargs)

    def parse(self, response, *args, **kwargs):
        """
        Метод парсит пагинацию мужской и женской одежды
        """
        for idx in range(2, 102):
            yield scrapy.Request(f'https://www.lamoda.ru/c/477/clothes-muzhskaya-odezhda/?page={idx}',
                                 callback=self.parse_page)
        for idx in range(2, 102):
            yield scrapy.Request(f'https://www.lamoda.ru/c/477/clothes-zhenskaya-odezhda/?page={idx}',
                                 callback=self.parse_page)

    def parse_page(self, response, *args, **kwargs):
        """
        Метод парсит ссылки на все товары на текущей странице
        """
        yield from self._follow(response,
                                css_selector=self._css_selectors['items'],
                                callback=self.parse_item,
                                cb_kwargs=kwargs)

    def parse_item(self, response, *args, **kwargs):
        """
        Метод парсит данные товара при помощи CSS селекторов.
        При возвращении словаря из метода, он будет сохранен в json, если запустить паучка из командной строки
        """
        prices = response.css('span.x-premium-product-prices__price')
        description = response.css('div.x-premium-product-description__text::text').get()
        item = {
            'brand': response.css('span.x-premium-product-title__brand-name').attrib.get('title'),
            'name': response.css('div.x-premium-product-title__model-name::text').get().strip(),
            'description': description.strip() if description else None,
            'price_before_discount': int(prices[0].attrib.get('content')),
            'final_price': int(prices[-1].attrib.get('content')),
            'discount': int(100 * (1 - int(prices[-1].attrib.get('content')) /
                                     int(prices[-0].attrib.get('content')))),
            'contains': response.css('span.x-premium-product-description-attribute__value::text').get()
        }
        yield item
