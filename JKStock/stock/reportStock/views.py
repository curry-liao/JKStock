import json
from django.http import HttpResponse
from rest_framework.views import APIView
# import stock.queryStock
from queryStock.queryAgent import QueryAgent

# from rest_framework.response import Response
# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User


class ReportStockView(APIView):
    # https://quality.data.gov.tw/dq_download_json.php?nid=11764&md5_url=63da90da53affbda60bab24f31be3d59
    def get(self, request):
        # gov_opendata_url = "https://quality.data.gov.tw/dq_download_json.php?nid=11764&md5_url=63da90da53affbda60bab24f31be3d59"
        # result, status_code = QueryAgent(url=gov_opendata_url).get(request.query_params)

        stock_data = QueryAgent(url="").get()
        return HttpResponse(json.dumps(stock_data), status=200, content_type='application/json')