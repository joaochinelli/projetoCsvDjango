from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser

from csv.models import Csv
from csv.api import serializers 


class CsvViewSet(APIView):

    # parser_classes = [MultiPartParser]

    def get(self, request, format=None):
        return Response({'ok':'ok'})
    
    def post(self, request, format=None):

        # file_obj = request.data['file']

        # print(file_obj)

        # Csv.objects.create(
        #     identificadorUrl = '',
        # )

        # self.http_method_names.append("post")

        return Response({
            # 'data': file_obj,
            'message' : 'Sucesso',
        }) 