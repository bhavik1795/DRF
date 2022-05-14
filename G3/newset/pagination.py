from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'records'   # Client can set how many records he want to fetch per page ( Eg. p=1&records=10 --> he can get 10 records/page )
    max_page_size = 7 # restrict client from fetching records
    # last_page_strings = 'end'    # By default it is set as "last" ( Eg. p=last)


# class MyLimitOffsetPagination(LimitOffsetPagination): # Eg. mylimit=3&myoffset=8 ('mylimit' = shows records, 'myoffset' = if it set 8 then record starts from 9 )
#     default_limit = 5       
#     limit_query_param = 'mylimit'
#     offset_query_param = 'myoffset'
#     max_limit = 6


class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    #    you have to create "created" field in model which stores 'Time Stamp' in its record and on the besis of that 'CursorPagination' orders to that field and we can see the records.