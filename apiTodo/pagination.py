from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class SmallPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'sayfa'

class LargePageNumberPagination(PageNumberPagination):
    page_size = 5 

class MyLimitOfsetPagination(LimitOffsetPagination):
    page_size = 2
    limit_query_param = 'sayfadaki_eleman_sayisi' 
    