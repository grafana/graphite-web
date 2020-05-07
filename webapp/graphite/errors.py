from django.http import HttpResponseBadRequest


class NormalizeEmptyResultError(Exception):
    # throw error for normalize() when empty
    pass


class InputParameterError(ValueError):
    pass


# subtype of input parameter error which only gets raised by the parameter validation
class InputValidationError(InputParameterError):
    pass


# decorator which turns InputParameterExceptions into Django's HttpResponseBadRequest
def handleInputParameterError(f):
    def new_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except InputParameterError as e:
            return HttpResponseBadRequest('Bad Request: {err}'.format(err=e))

    return new_f
