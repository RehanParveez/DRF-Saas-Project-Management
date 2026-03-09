from notifications.models import ApiRequest

class ApiRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            ApiRequest.objects.create(user=request.user, method=request.method, path=request.path)
        return response