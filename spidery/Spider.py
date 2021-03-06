# -*- coding: utf-8 -*-

class Spider(object):
    
    def __init__(self, urls):
        self.urls = urls
        self.filter = set([])
        self.steps = {
            'fetch': None,
            'parse': None,
            'presist': None,
        }
        
    def fetch(self, f):
        self.steps['fetch'] = f
        return f
        
    def parse(self, f):
        self.steps['parse'] = f
        return f

    def presist(self, f):
        self.steps['presist'] = f
        return f
    
    def consume_one(self):
        url = self.urls.pop(0)
        
        if self.steps['fetch']:
            response = self.steps['fetch'](url)
            
            if self.steps['parse']:
                result = self.steps['parse'](response)
                    
                for item, urls in result:    
                    if urls:
                        for url in urls:
                            if url not in self.filter:
                                self.urls.append(url)
                                self.filter.add(url)
                    
                    if item:
                        if self.steps['presist']:
                            self.steps['presist'](item)
            
    def consume_all(self):
        while self.urls:
            self.consume_one()
