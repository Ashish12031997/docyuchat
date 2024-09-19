from rest_framework.serializers import Serializer, CharField


class QuestionSerializer(Serializer):
    question = CharField()
