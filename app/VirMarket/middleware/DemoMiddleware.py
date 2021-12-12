from django.db.models import F
from VirMarket_CS.models import newstats

class DemoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def stats(self, os_info):
        if 'Windows' in os_info:
            newstats.objects.all().update(win=F('win') + 1)
        elif 'mac' in os_info:
            newstats.objects.all().update(mac=F('mac') + 1)
        elif 'iphone' in os_info:
            newstats.objects.all().update(iphone=F('iphone') + 1)
        elif 'Android' in os_info:
            newstats.objects.all().update(android=F('android') + 1)
        else:
            newstats.objects.all().update(other=F('other') + 1)

    def __call__(self, request):
        if 'admin' not in request.path:
            self.stats(request.META['HTTP_USER_AGENT'])
        
        response = self.get_response(request)

        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print(f'view name: {view_func.__name__}')

    #def process_exception(self, request, exception):

    # def process_template_response(self, request, response):
    #     response.context_data['new_data'] = self.context_response
    #     return response

        