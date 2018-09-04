# -*- coding: utf-8 -*-
import scrapy
from Repository.items import RepositoryItem


class CoursesSpider(scrapy.Spider):
    name = 'courses'

    @property
    def start_urls(self):

        urls_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (urls_tmpl.format(i) for i in range(1, 5))
    def parse(self, response):
        for course in response.css('li.col-12'):
            item = repositoryItem()
            item['name'] = course.css('a::text').extract_first().strip()
            item['update_time'] = course.css('relative-time::attr(datetime)').extract_first().strip()
            course_url = response.urljoin(course.css('a::attr(href)').extract_first())
            request = scrapy.Request(course_url, callback=self.parse_author)            request.meta['item'] = item
            yield request

    def parse_author(self, response):
        item = response.meta['item']
        item['commits'] = response.xpath('(//span[@class="num text-emphasized"])[1]/text()').extract_first().extract_first() 
        item['branches'] = response.xpath('(//span[@class="num text-emphasized"])[2]/text()').extract_first()
        item['releases'] = response.xpath('(//span[@class="num text-emphasized"])[3]/text()').extract_first()
        yield item
