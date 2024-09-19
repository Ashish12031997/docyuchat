from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from embeddings.serializers.question import QuestionSerializer
from embeddings.controllers.openai import OpenAI
import numpy as np

from embeddings.models import Resume


class ask(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data["question"]
            print(question)
            openai = OpenAI()
            user_input_embeddings = openai.get_embedding(question)

            embedding_vector = "[" + ",".join(map(str, user_input_embeddings)) + "]"

            knn_results = Resume.objects.raw(
                "SELECT * FROM public.resume ORDER BY vector <-> %s::vector LIMIT 1",
                [embedding_vector],
            )
            system_message = "you are friendly chatbot. you will question and answer only about Ashish like skills, work, education and experience, projects. if you are asked other questions which are not related to ashish then respond with I am not design to answer this question."
            results = [result.summary for result in knn_results]
            # print("knn results---", results)
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": question},
                {
                    "role": "assistant",
                    "content": f"Answer question related to Ashish: {results}",
                },
            ]
            # print(messages)
            res = openai.get_completion_from_messages(messages)
            print("res", res)
            return Response({"message": res}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
