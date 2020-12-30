from django.utils.deprecation import MiddlewareMixin
class BookMiddlewareMixin(MiddlewareMixin):
    def process_request(self,request):
        print('request 每次请求前都会调用')
        pass
    def process_response(self,request,response):
        print('response每次相应前都会调用')
        return response






