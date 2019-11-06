#!/usr/bin/env python

import urllib
import BeautifulSoup

PATTERN = 'doel'
URL = 'http://www.vandale.nl/gratis-woordenboek/mobiel/?pattern={}&lang=nn'.format(PATTERN)

html = urllib.urlopen(URL).read()
soup = BeautifulSoup.BeautifulSoup(html)

# ipv onderstaande kan bijv: [line.getText() for line in soup.results.article.findAll('span', {'class':'f3 f0g'})]
results = soup.findAll('result')
num = len(results)

print('Aantal resultaten: {}'.format(num))
for result in results:
    headword = result.find('headword').getText()
    article = result.find('article').getText()
    index = result.find('index').getText()
    lang = result.find('lang').getText()

    print(u'Index:    {}'.format(index))
    print(u'Language: {}'.format(lang if lang else '-'))
    print(u'Headword: {}'.format(headword))
    print(u'Article:  {}'.format(article))
    print
