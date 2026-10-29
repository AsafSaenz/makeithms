class EmpresaActualMiddleware:
    """Expone `request.empresa` con la empresa del usuario autenticado."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, "user", None)
        request.empresa = getattr(user, "empresa", None) if user and user.is_authenticated else None
        return self.get_response(request)
