import json

from rest_framework.decorators import api_view
from django.http import JsonResponse

from .models import Bahasa, Country, ForeignTranslation


@api_view(['GET'])
def translate(request):
    if request.method == 'GET':
        try:
            string = request.data.get('string')
            source = request.data['data']['source']
            target = request.data['data']['target']
            if source == 'id':
                result = ForeignTranslation.objects.get(
                    bahasa__text=string,
                    country__iso=target
                ).text

            else:
                bahasa = ForeignTranslation.objects.get(
                    text=string,
                    country__iso=source
                ).bahasa
                if target == 'id':
                    result = bahasa.text
                else:
                    result = ForeignTranslation.objects.get(
                        bahasa=bahasa,
                        country__iso=target
                    ).text
            response = {
                'data': result
            }
            return JsonResponse(
                response,
                status=200
            )
        except:
            return JsonResponse(
                {'message': 'translation not found'},
                status=400
            )
