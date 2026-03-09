import threading

_user = threading.local()


class UserLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        _user.value = request.user
        _user.ip = request.META.get("REMOTE_ADDR")
        
        response = self.get_response(request)
        
        return response 
    
    
    
def get_current_user():
    return getattr(_user, "value", None)
        
def get_current_ip():
    return getattr(_user, "ip", None)