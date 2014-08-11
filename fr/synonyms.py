#!/usr/bin/env python

"""synonymes.py: French synonymes modules. Data source: http://www.crisco.unicaen.fr/des/synonymes/"""

__author__      = "Oscar LASM aka moas"
__copyright__   = "Copyright 2014 - Terrien"

import os
import requests
from scrapy.selector import Selector

class Crisco(object):

    def __init__(self):

        self.url_source = "http://www.crisco.unicaen.fr/des/synonymes/"
        self.cache_html = {}

    def memoize():
        def wrapper(func):
            def wrapped(self, word, *args, **kwargs):
                url = "{0}{1}".format(self.url_source, word)
                if not self.cache_html.has_key(url):
                    self.cache_html[url] = func(self, word, url = url, *args, **kwargs)
                return self.cache_html[url]
            return wrapped
        return wrapper

    @memoize()
    def __load(self, word, *args, **kwargs):
        url = "{0}{1}".format(self.url_source, word)
        req = requests.get(url)
        if req.status_code != 200:
            raise 
        return req.content

    def __genesis(self, word):
        html = self.__load(word)
        sel = Selector(text=html)
        num_synonym = sel.xpath('//i[@class="titre"]/text()').re("(?P<val>\d+) synonymes")
        return sel, num_synonym

    def synonyms_of(self, word):
        sel, num_synonym = self.__genesis(word)
        if not num_synonym:
            synonymes = []
        else:
            synonymes = sel.xpath("//a[contains(@href,'/des/synonymes/')]/text()")[1:int(num_synonym[0])+1]
        for _w in synonymes:
            yield _w.extract()

    def antonyms_of(self, word):
        sel, num_synonym = self.__genesis(word)
        num_synonym = 0 if not len(num_synonym) else int(num_synonym[0])

        num_antonym = sel.xpath('//i[@class="titre"]/text()').re("(?P<val>\d+) antonymes")
        if not num_antonym:
            antonymes = []
        else:
            antonymes = sel.xpath("//a[contains(@href,'/des/synonymes/')]/text()")[num_synonym+1:num_synonym+int(num_antonym[0])+1]
        for _w in antonymes:
            yield _w.extract()


