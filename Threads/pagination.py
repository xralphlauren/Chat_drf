from rest_framework.pagination import LimitOffsetPagination


class ThreadsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 1000
