import json
import requests
from django.http import HttpResponse, Http404, HttpResponseBadRequest

from wechat_service.utils.request_processor import fetch_parameter_dict


def test_api(request):
    parameter_dict = fetch_parameter_dict(request, 'GET')
    return HttpResponse(json.dumps({'message': parameter_dict['username'] + ' welcome!'}))


def do_request(request_type: str, url: str, params: dict = None, headers: dict = None, data: dict = None):
    response = requests.request(request_type, url, params=params, headers=headers, data=data)
    # print(response.request.headers)
    response_dict = None
    if response.status_code == 200:
        try:
            response_dict = json.loads(response.text)
        except json.decoder.JSONDecodeError as ex:
            print(ex)
    elif response.status_code != 404:
        response_dict = response.text
    return response.status_code, response_dict


# 8f6096488ae98408f07ba23a766d526f
def fetch_wx_user(request):
    api_url = "https://api.weixin.qq.com/sns/jscode2session"
    # appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code
    code = fetch_parameter_dict(request, 'GET')['code']
    params = {
        'appid': 'wx459cd21fbb11658a',
        'secret': '8f6096488ae98408f07ba23a766d526f',
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    status_code, response_dict = do_request('GET', api_url, params=params)
    return HttpResponse(response_dict)