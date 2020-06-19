# from django.conf import settings
# from django.http import Http404
# from django.utils.deprecation import MiddlewareMixin
#
# from flatpages_i18n.views import flatpage
#
#
# class FlatpageFallbackMiddleware(MiddlewareMixin):
#     def process_response(self, request, response):
#         if response.status_code != 404:
#             # No need to check for a flatpage for non-404 responses.
#             return response
#         try:
#             return flatpage(request, request.path_info)
#         # Return the original response if any errors happened. Because this
#         # is a middleware, we can't assume the errors will be caught elsewhere.
#         except Http404:
#             return response
#         except:
#             if settings.DEBUG:
#                 raise
#             return response
