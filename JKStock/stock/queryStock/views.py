from django.shortcuts import render

# Create your views here.

#Dividend Yield
import traceback
import json
import re
import urllib.request
import urllib.parse
from urllib.request import urlopen
from urllib.error import HTTPError

import ssl
import pandas as pd
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context


class QueryStock:
    def __init__(self, url):
        self.url = url

    def get(self, query_parms={}):
        try:
            status_code = 200

            data = []
            try:
                url ='https://goodinfo.tw/StockInfo/StockDividendPolicyList.asp?MARKET_CAT=%E4%B8%8A%E5%B8%82&INDUSTRY_CAT=%E5%85%A8%E9%83%A8&YEAR='
                target_url = url+str(2017)

                data = bytes(urllib.parse.urlencode({}), encoding='utf-8')
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
                req = urllib.request.Request(target_url, data, headers)
                response = urllib.request.urlopen(req)
                print(response.status)
                html = response.read()
                content = html.decode("utf8")
                print("-------------------------")
                print(content)

                # bf_soup = BeautifulSoup(content)
                # print(bf_soup)
                # table = bf_soup.find("table")
                # table_body = table.find('tbody')
                # trs = table_body.find_all('tr')
                # for tr in trs:
                #     tds = tr.find_all('td')
                #     tds = [ele.text.strip() for ele in tds]
                #     data.append([ele for ele in tds if ele])  # Get rid of empty values
                # print(data)

            except HTTPError:
                print("Not Found")


            # image_url = div["style"].split("'")[1]
            # print(image_url)
            #
            # name = image_url[image_url.rfind("/", 2) + 1:]
            # print(name)
            #
            # image = urlopen(image_url).read()
            # f = open("./images/" + name, "wb")
            # f.write(image)
            # f.close()

            response = urlopen(self.url)
            lines = json.load(response)
            df = pd.DataFrame.from_dict(lines)
            df = df.rename(index=str, columns={
                "證券代號": "stock_code",
                "證券名稱": "stock_name",
                "殖利率(%)": "diviedend_yield",
                "股利年度": "year",
                "本益比": "pe",    #P/E Ration
                "股價淨值比": "pbr",#Price Book Ratio
                "財報年/季": "season",
            })
            return df.to_dict('records'), status_code
        except HTTPError as e:
            print(e)
            traceback.print_exc()
        except Exception as e:
            print(e)
            traceback.print_exc()
