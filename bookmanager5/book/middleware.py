from django.utils.deprecation import MiddlewareMixin

class BookMiddlewareMixin(MiddlewareMixin):
    def process_request(self, request):
        print('request每次请求前都会调用')
        pass

    def process_response(self, request, response):
        print('response每次响应前都会调用')
        return response

class BookMiddlewareMixin2(MiddlewareMixin):
    def process_request(self, request):
        print('request每次请求前都会调用222')
        pass

    def process_response(self, request, response):
        print('response每次响应前都会调用222')
        return response




