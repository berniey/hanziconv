#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Bernard Yue
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import unicode_literals, absolute_import
import requests
import bs4
import pprint


class Main(object):
    """"""
    def run(self):
        """Program entry point
        """
        _url = 'http://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/stctable.php'
        _params = '?s=stroke&n={}'

        tran = ''
        simp = ''
        for stroke in range(7, 33):
            try:
                url = '{}{}'.format(_url, _params.format(stroke))
                temp1, temp2 = self.getChars(url)
                print('Found {:3} characters for {:2} strokes'.format(len(temp1),
                    stroke))
                tran += temp1
                simp += temp2
            except RuntimeError:
                pass
        print('There are in total {:4} characters'.format(len(tran)))
        return self.format(tran, 40), self.format(simp, 40)

    def getChars(self, url):
        """returns list of tranditionals and simplified characters
        """
        tran = []
        simp = []

        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        for item in soup.find_all('table'):
            if 'class' in item.attrs and        \
                    'radical_table' in item.attrs['class']:
                data = item.find_all('th')
                if not data:
                    raise RuntimeError('Target data not found.'
                            '  Formatted changed?')
                else:
                    """if data[0] != ... raise error"""
                    for target in data[2:]:
                        alltext = target.next_siblings.next().getText()
                        alltext = ''.join(alltext.split())
                        alltext = alltext.replace(u'〔', '')
                        alltext = alltext.replace(u'〕', '')
                        if len(alltext) % 2 != 0:
                            print("ignoring error data - {}".format(alltext))
                            continue
                        tran.extend(alltext[::2])
                        simp.extend(alltext[1::2])
            else:
                """raise not found error"""
        return ''.join(tran), ''.join(simp)

    @staticmethod
    def format(mylist, size):
        """Yield successive n-sized chunks from l."""
        for i in xrange(0, len(mylist), size):
            yield mylist[i:i + size]


if __name__ == '__main__':
    x, y = Main().run()
    for item, name in ((x, 'tranditional'), (y, 'simplified')):
        print('{} list'.format(name))
        for i in item:
            print(i)
