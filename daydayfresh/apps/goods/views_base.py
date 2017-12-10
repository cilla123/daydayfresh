from django.views.generic.base import View
from django.http import JsonResponse
from django.core import serializers
import json

from goods.models import Goods

class GoodsListView(View):

    '''
    商品列表
    '''
    def get(self, requset):
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)