from rest_framework import pagination
from rest_framework.response import Response


class APIPagination(pagination.PageNumberPagination):

    # def paginate_queryset(self, queryset, request, view=None):
    #     total_pages = len(queryset) // self.page_size + 1
    #     req_page = request.query_params.get('page')
    #     if req_page:
    #         if int(req_page) > total_pages:
    #             return []
    #         else:
    #             return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                # 'next': self.get_next_link().split(':8000')[-1] if self.get_next_link() else None,
                'previous': self.get_previous_link()
                # 'previous': self.get_previous_link().split(':8000')[-1] if self.get_previous_link() else None
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })