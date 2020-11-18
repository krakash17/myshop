from .models import User
from rest_framework.response import Response
from storeapp.serializers import CategoriesSerializer, ItemSerializer, SubCategoriesSerializer, UserProfileSerializer
from rest_framework import viewsets
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from storeapp.permissions import  IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from storeapp.models import Categories, SubCategories,Item

from rest_framework.parsers import JSONParser 
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class UserView(APIView):
    # permission_classes = (IsAuthenticated,)


    # @api_view(["GET",])
    # def user_list(self,request):
    #     users = User.objects.all()
    #     serializer = UserProfileSerializer(users,many="true")
    
    #     return Response(serializer.data) 
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserProfileSerializer(users,many="true")
        return Response(serializer.data)

    # def create(self, request):
    #     users = User.objects.all()
    #     serializer = UserProfileSerializer(users,many="true")
    #     return Response(serializer.data)  
        

class CategoriesView(APIView):
        
     def get(self, request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories,many="true")
        return Response(serializer.data)

     def post(self, request):
        categories_serializer = CategoriesSerializer(data=request.data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response(categories_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     


class CategoryView(APIView):
    def get(self, request,pk):
        categories = Categories.objects.get(pk=pk)
        serializer = CategoriesSerializer(categories)
        return Response(serializer.data)
        
    def patch(self,request,pk):
        categories = Categories.objects.get(pk=pk)
        categories_serializer = CategoriesSerializer(categories, data=request.data, partial=True) 
        if categories_serializer.is_valid(): 
           categories_serializer.save() 
           return Response(categories_serializer.data)   

    def delete(self,request,pk):
        categories = Categories.objects.get(pk=pk)
        categories.delete()
        return Response({'message': 'Category were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    
class SubCategoriesView(APIView):
        
     def get(self, request):
        subcategories = SubCategories.objects.all()
        serializer = SubCategoriesSerializer(subcategories,many="true")
        return Response(serializer.data)

     def post(self, request):
        subcategories_data = JSONParser().parse(request)
        subcategories_serializer = SubCategoriesSerializer(data=subcategories_data)
        if subcategories_serializer.is_valid():
            subcategories_serializer.save()
            return Response(subcategories_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(subcategories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubCategoryView(APIView):
    def get(self, request,pk):
        subcategories = SubCategories.objects.get(id=pk)
        serializer = SubCategoriesSerializer(subcategories)
        return Response(serializer.data)
        
    def patch(self,request,pk):
        subcategory = SubCategories.objects.get(id=pk)
        subcategory_serializer = SubCategoriesSerializer(subcategory, data=request.data, partial=True) 
        if subcategory_serializer.is_valid(): 
            subcategory_serializer.save() 
            return Response(subcategory_serializer.data)
        return Response(subcategory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        subcategory = SubCategories.objects.get(pk=pk)
        subcategory.delete()
        return Response({'message': 'SubCategory were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class ItemsView(APIView):
        
     def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items,many="true")
        return Response(serializer.data)

     def post(self, request):
        items_data = JSONParser().parse(request)
        items_serializer = ItemSerializer(data=items_data)
        if items_serializer.is_valid():
            items_serializer.save()
            return Response(items_serializer.data, status=status.HTTP_201_CREATED) 
        return Response(items_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemView(APIView):
    def get(self, request,pk):
        item = Item.objects.get(id=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
        
    def patch(self,request,pk):
        item = Item.objects.get(id=pk)
        item_serializer = ItemSerializer(item, data=request.data, partial=True) 
        if item_serializer.is_valid(): 
            item_serializer.save() 
            return Response(item_serializer.data)
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response({'message': 'Item were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)        



class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer  

    @api_view(["GET",])
    def user_update(self,request,):
        users = User.objects.all()
        return Response(users)     

    @api_view(["GET", "PUT"])
    def user_update(self,request, pk):
        user = User.objects.get(id=pk)
        if request.method == "PUT":
           serializer = UserProfileSerializer(user, data=request.data)
           if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
           else:
                return Response({"error": serializer.errors, "error": True}) 
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)      


class CategoryImageViewSet(APIView):
      def get(self, request,pk):
        item = Item.objects.get(id=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
        
      def post(self,request,pk):

        # file = request.data['file']
        # image = UploadImageTest.objects.create(image=file)
        # return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


        categories = Categories.objects.get(id=pk)
        file = request.data['file']
        Categories.objects.create(picture=file)
        return Response({'message': 'image uploades'}, status=200)

      def delete(self,request,pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response({'message': 'Item were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 

    #   @api_view(["GET", "PUT","POST"]) 
    #   def UserProfile(self, request, pk):

    #       user = User.objects.get(id=pk)
    #       if request.method == "POST":
    #          image = request.data['image']
    #          User.objects.create(image=image)
    #          return Response({'message': 'image uploades'}, status=200)
    #       if request.method == "PUT":
    #          image = request.data['image']
    #          User.objects.create(image=image)
    #          return Response({'message': 'image uploades'}, status=200)   
         
          
       