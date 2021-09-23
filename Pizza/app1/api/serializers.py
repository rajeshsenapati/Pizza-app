from django.db.models import fields
from app1.models import PizaModel, StorsModel, ReviewModel
from rest_framework import serializers


class ReviwSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ReviewModel
        #fields = "__all__"
        exclude = ('pizzalist',)


class PizzaSerializer(serializers.ModelSerializer):
    reviews = ReviwSerializer(many=True, read_only=True)

    #length_name = serializers.SerializerMethodField()

    class Meta:
        model = PizaModel
        fields = "__all__"
        #exclude = ['name']


class StorsSerializer(serializers.ModelSerializer):
    #pizza_list = PizzaSerializer(many=True, read_only=True)
    #pizza_list = serializers.StringRelatedField(many=True)
    pizza_list = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='pizza_details'
    )

    class Meta:
        model = StorsModel
        fields = '__all__'

    # def get_length_name(self, object):
    #     length = len(object.name)
    #     return length

    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('name and description should not be same!!!!')
    #     else:
    #         return data

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short!')
    #     else:
    #         return value


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short!')


# class PizzaSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return PizaModel.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('name and description should not be same!!!!')
#         else:
#             return data

#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short!')
#         else:
#             return value