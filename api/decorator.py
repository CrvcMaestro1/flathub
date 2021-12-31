import functools

from rest_framework.exceptions import APIException
from rest_framework.response import Response


def wrapper_response(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        result = {'status': True, 'exception_message': ''}
        try:
            result['data'] = f(*args, **kwargs)
            return Response(result)
        except APIException as apiex:
            result['status'] = False
            result['exception_message'] = str(apiex)
        except Exception as ex:
            result['status'] = False
            result['exception_message'] = str(ex)
        return Response(result)

    return func
