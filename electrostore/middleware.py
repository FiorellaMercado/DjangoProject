from .models import usuario

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = usuario.objects.get(id=user_id)
                request.user = user
            except usuario.DoesNotExist:
                request.user = None
        else:
            request.user = None

        response = self.get_response(request)
        return response