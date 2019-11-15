# from django.utils.deprecation import MiddlewareMixin
# from django.http import HttpResponse
# from user import models
# from user import views
#
#
# class LoginMiddleware(MiddlewareMixin):
#     def process_request(self,request):
#         if not request.path in ['user/login/']:
#             token = request.META.get("HTTP_TOKEN")
#             if not token:
#                 return HttpResponse('404')
#             try:
#                 user_id = request.data['user_id']
#                 if not user_id:
#                     user_id = request.GET.get('user_id')
#             except Exception as e:
#                 return HttpResponse('404')
#             data = views.check_toke(token,user_id)
#             if not data:
#                 return HttpResponse('404')
