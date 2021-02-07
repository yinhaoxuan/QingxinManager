from django.http import JsonResponse
import json


def gen_response(code: int, data: str):
    return JsonResponse({
        'code': code,
        'data': data
    }, status=code)


def preprocess(request, keys):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
        except Exception as e:
            return False, gen_response(400, "JSON Decode Error: {}".format(e))
        try:
            res = {}
            for key in keys:
                res[key] = body[key]
        except Exception as e:
            return False, gen_response(400, "Data Format Error: {}".format(e))
        return True, res
    else:
        return False, gen_response(405, 'method {} not allowed'.format(request.method))

