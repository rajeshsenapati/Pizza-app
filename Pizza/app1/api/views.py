from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
#from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication

from app1.api.permission import AdminOrReadOnly, ReviewOwnerOrReadOnly
from app1.models import PizaModel, StorsModel, ReviewModel
from app1.api.serializers import PizzaSerializer, StorsSerializer, ReviwSerializer


class ReviewCreate(generics.CreateAPIView):

    serializer_class = ReviwSerializer

    def get_queryset(self):
        return ReviewModel.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        pizza = PizaModel.objects.get(pk=pk)

        user = self.request.user
        review_queryset = ReviewModel.objects.filter(pizzalist=pizza, customer=user)

        if review_queryset.exists():
            raise ValidationError("You already Revied this Item.")

        if pizza.avg_rating == 0:
            pizza.avg_rating = serializer.validated_data['rating']
        else:
            pizza.avg_rating = (pizza.avg_rating + serializer.validated_data['rating'])/2

        pizza.number_rating = pizza.number_rating + 1
        pizza.save()

        serializer.save(pizzalist=pizza, customer=user)


class ReviewList(generics.ListAPIView):

    permission_classes = [IsAuthenticated]

    # queryset = ReviewModel.objects.all()
    serializer_class = ReviwSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return ReviewModel.objects.filter(pizzalist=pk)


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [ReviewOwnerOrReadOnly]

    queryset = ReviewModel.objects.all()
    serializer_class = ReviwSerializer


# class ReviewDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = ReviewModel.objects.all()
#     serializer_class = ReviwSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = ReviewModel.objects.all()
#     serializer_class = ReviwSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewList(APIView):

#     def get(self, request):
#         review = ReviewModel.objects.all()
#         serializer = ReviwSerializer(review, many=True)
#         return Response(serializer.data)
        
#     def post(self, request):
#         serializer = ReviwSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class ReviewDetails(APIView):

#     def get(self, request, pk):
#         try:
#             reviews = ReviewModel.objects.get(pk=pk)
#         except ReviewModel.DoesNotExist:
#             return Response({'error': 'Review Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ReviwSerializer(reviews)

#     def put(self, request, pk):
#         reviews = ReviewModel.objects.get(pk=pk)
#         serializer = ReviwSerializer(reviews, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, pk):
#         reviews = ReviewModel.objects.get(pk=pk)
#         reviews.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class Storslists(viewsets.ModelViewSet):

    permission_classes = [AdminOrReadOnly]

    queryset = StorsModel.objects.all()
    serializer_class = StorsSerializer

# class Storslists(viewsets.ReadOnlyModelViewSet):
#     queryset = StorsModel.objects.all()
#     serializer_class = StorsSerializer


# class Storslists(viewsets.ViewSet):

#     def list(self, request):
#         queryset = StorsModel.objects.all()
#         serializer = StorsSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StorsModel.objects.all()
#         stor = generics.get_object_or_404(queryset, pk=pk)
#         serializer = StorsSerializer(stor, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StorsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class StorsList(APIView):
    
#     def get(self, request):
#         stors = StorsModel.objects.all()
#         serializer = StorsSerializer(stors, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = StorsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class StorsDetails(APIView):

#     def get(self, request, pk):
#         try:
#             stors = StorsModel.objects.get(pk=pk)
#         except StorsModel.DoesNotExist:
#             return Response({'error': 'Stors not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = StorsSerializer(stors)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         stors = StorsModel.objects.get(pk=pk)
#         serializer = StorsSerializer(stors, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, pk):
#         stors = StorsModel.objects.get(pk=pk)
#         stors.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



class PizzaList(APIView):

    def get(self, request):
        pizza = PizaModel.objects.all()
        serializer = PizzaSerializer(pizza, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PizzaDetails(APIView):

    def get(self, request, pk):
        try:
            pizza = PizaModel.objects.get(pk=pk)
        except PizaModel.DoesNotExist:
            return Response({'error': 'Pizza not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PizzaSerializer(pizza)
        return Response(serializer.data)

    def put(self, request, pk):
        pizza = PizaModel.objects.get(pk=pk)
        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        pizza = PizaModel.objects.get(pk=pk)
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Function Based View
# @api_view(['GET', 'POST'])
# def pizza_list(request):
#     if request.method == 'POST':
#         serializer = PizzaSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     else:
#         pizza = PizaModel.objects.all()
#         serializer = PizzaSerializers(pizza, many=True)
#         return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def pizza_details(request,pk):
#     if request.method == 'GET':
#         pizza = PizaModel.objects.get(pk=pk)
#         serializer = PizzaSerializers(pizza)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         pizza = PizaModel.objects.get(pk=pk)
#         serializer = PizzaSerializers(pizza, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     if request.method == 'DELETE':
#         pizza = PizaModel.objects.get(pk=pk)
#         pizza.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)