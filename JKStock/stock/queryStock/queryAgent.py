from django.shortcuts import render

# Create your views here.

import traceback
import json
import urllib.request
import urllib.parse
from tabulate import tabulate
from urllib.request import urlopen
from urllib.error import HTTPError

import ssl
import pandas as pd
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context


class QueryAgent():

    def __init__(self, url):
        self.url = url

    def get(self, query_parms={}):
        try:
            try:
                url = 'https://goodinfo.tw/StockInfo/DayTrading.asp?STOCK_ID=2367'
                data = bytes(urllib.parse.urlencode({}), encoding='utf-8')
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
                req = urllib.request.Request(url, data, headers)
                response = urllib.request.urlopen(req)
                if response.status == 200:
                    html = response.read()
                    html_decode_utf8 = html.decode("utf8")
                    soup = BeautifulSoup(html_decode_utf8, 'html.parser')

                    table_div = soup.find('div', attrs={'id': 'divDayTradingDetail'})

                    table = table_div.find('table', attrs={'class': 'solid_1_padding_4_2_tbl'})

                    table_rows = table.find_all('tr')

                    stock_data = []
                    thead = []
                    subthead = []
                    for tr in table_rows:
                        tds = tr.find_all('td')

                        if tds[0].text == '期別' and len(thead) == 0:
                            [thead.append(td.text) for td in tds if td.text != '現股當沖' and td.text != '融資融券']
                        elif tds[0].text.startswith('成交張數') and len(subthead) == 0:
                            [subthead.append(td.text) for td in tds]
                        elif tds[0].text.find("/") > -1:
                            row = [td.text for td in tds]
                            stock_dict = dict(zip(thead+subthead, row))
                            stock_data.append(stock_dict)
                        else:
                            continue

                    # print(stock_data)

                    # df = pd.DataFrame(stock_data, columns=thead+subthead)
                    # print(tabulate(df, headers='keys'))

            except HTTPError:
                print("Not Found")

            return stock_data
        except HTTPError as e:
            print(e)
            traceback.print_exc()
        except Exception as e:
            print(e)
            traceback.print_exc()
