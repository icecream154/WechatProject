import json
from django.http import HttpResponse, Http404, HttpResponseBadRequest

from wechat_service.utils.request_processor import fetch_parameter_dict


def test_api(request):
    parameter_dict = fetch_parameter_dict(request, 'GET')
    return HttpResponse(json.dumps({'message': parameter_dict['username'] + ' welcome!'}))
