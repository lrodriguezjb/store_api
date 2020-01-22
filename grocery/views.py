from .models import Food
from .serializers import FoodSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
    )