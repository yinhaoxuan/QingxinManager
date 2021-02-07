from django.http import JsonResponse
import json


def gen_response(code: int, data: str):
    return JsonResponse({
        'code': code,
        'data': data
    }, status=code)


def process_post(request, keys):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
        except Exception as e:
            return False, gen_response(400, f"JSON Decode Error: {e}")
        try:
            res = {}
            for key in keys:
                res[key] = body[key]
        except Exception as e:
            return False, gen_response(400, f"Data Format Error: {e}")
        return True, res
    else:
        return False, gen_response(405, f'method {request.mothod} not allowed')
def process_get(request, keys):
    if request.method == 'GET':
        try:
            res = {}
            for key in keys:
                res[key] = request.GET.get(key)
        except Exception as e:
            return False, gen_response(400, f"Data Format Error: {e}")
        return True, res
    else:
        return False, gen_response(405, f'method {request.mothod} not allowed')

