
class Cors:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # before view

        response = self.get_response(request)

        # after view

        response['Access-Control-Allow-Origin'] = '*'

        return response