from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from orders.models import MtOrder as Order
from orders.order_serializer import MtOrderSerializer as OrderSerializer
from datetime import datetime, timedelta
import pytz

class OrderListPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class OrderSaleList(ListAPIView):

    permission_classes = (IsAuthenticated, )
    authentication_class = JSONWebTokenAuthentication

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['order_id']

    pagination_class = OrderListPagination

    def get_queryset(self):
        days = self.request.query_params.get('days',None)
        if days is None:
            return super().get_queryset()
        else:
            queryset = Order.objects.filter(date_created__gte=datetime.now(pytz.timezone('Asia/Kolkata'))-timedelta(days=int(days)))
            return queryset

        return queryset
