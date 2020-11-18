from rest_framework import serializers
from storeapp.models import Categories, User,SubCategories, Item


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'password','last_name','username', 'phone')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.username = validated_data.get('email')
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
       
        instance.__dict__.update(validated_data)
        instance.save()
        return instance    

class CategoriesSerializer(serializers.ModelSerializer):
     class Meta:
        model = Categories
        fields = ('id', 'category_name','picture')

class SubCategoriesSerializer(serializers.ModelSerializer):
     class Meta:
        model = SubCategories
        fields = ('id','category_id', 'subcategory_name')


class ItemSerializer(serializers.ModelSerializer):
     class Meta:
        model = Item
        fields = ('id','subcategory_id', 'item_name','item_description','item_price','item_amount','item_quantity','item_flag',)
