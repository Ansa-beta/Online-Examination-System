from rest_framework import serializers
# from examapp.models import QuestionDb   We do not need models here, because there is no choices in this project

class QuestionSerializer(serializers.Serializer):
    question=serializers.CharField(max_length=100)
    option_a=serializers.CharField(max_length=100)
    option_b=serializers.CharField(max_length=100)
    option_c=serializers.CharField(max_length=100)
    option_d=serializers.CharField(max_length=100)
    correct_answer=serializers.CharField(max_length=100)
    