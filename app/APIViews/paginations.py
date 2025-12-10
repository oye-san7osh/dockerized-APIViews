from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ApiPagination(PageNumberPagination):
    
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 10
    
    
    def get_page_size(self, request):
        
        size = request.query_params.get('size')
        
        if size and size.isdigit():
            return min(int(size), self.max_page_size)

        return self.page_size
    
    
    def get_paginated_response(self, data):
        
        return Response(
            {
                "status": "success",
                "page_info":
                    {
                        "current_page": self.page.number,
                        "page_size": self.get_page_size(self.request),
                        "total_items": self.page.paginator.count,
                        "total_pages": self.page.paginator.num_pages,
                        "has_next": self.page.has_next(),
                        "has_previous": self.page.has_previous(),
                    },
                "links":
                    {
                        "next_url": self.get_next_link(),
                        "previous_url": self.get_previous_link(),
                    },
                "results": data
            }
        )
        



"""from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class ApiPagination(LimitOffsetPagination):
    
    default_limit = 3
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 10
    
    
    def get_limit(self, request):
        
        if request.query_params.get('limit'):
            return int(request.query_params.get('limit'))
        return self.default_limit
    
    
    def get_offset(self, request):
        
        if request.query_params.get('offset'):
            return int(request.query_params.get('offset'))
        return 0
    
    
    def get_paginated_response(self, data):
        
        return Response(
            {
                "status": "success",
                "page_info":
                    {
                        "limit": self.limit,
                        "offset": self.offset,
                        "total_items": self.count,
                    },
                "links":
                    {
                        "next_url": self.get_next_link(),
                        "previous_url": self.get_previous_link(),
                    },
                "results": data
            }
        )
"""


"""from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class ApiPagination(CursorPagination):
    
    page_size = 3
    cursor_query_param = 'cursor'
    ordering = "-employee_id"
    
    
    def get_paginated_response(self, data):
        
        return Response(
            {
                "status": "success",
                "page_info":
                    {
                        "page_size": self.page_size,
                        "ordering": self.ordering,
                    },
                "links":
                    {
                        "next_url": self.get_next_link(),
                        "previous_url": self.get_previous_link(),
                    },
                "results": data
            }
        )
"""