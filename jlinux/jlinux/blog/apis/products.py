from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from jlinux.api.pagination import LimitOffsetPagination
from jlinux.blog.models import Product

from jlinux.blog.services.products import create_product
from jlinux.blog.selectors.products import get_products

class ProductApi(APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 15
    
    class InPutSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)
    
    class OutPutSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Product
            fields = ("name", "created_at", "updated_at")
    
    @extend_schema(request=InPutSerializer, responses=OutPutSerializer)
    def post(self, request):
        serializer = self.InPutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_product(name=serializer.validated_data.get("name"))
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST
                )
        
        return Response(data=self.OutPutSerializer(query, context={"request":request}).data)
    
    @extend_schema(responses=OutPutSerializer)
    def get(self, request):
        query = get_products()
        return Response(data=self.OutPutSerializer(query, context={"request":request}, many=True).data)