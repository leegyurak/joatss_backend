import anthropic
import json
import os

from rest_framework.response import Response
from rest_framework.views import APIView

from joatssapp.serializers import JoatssSerializer


class JoatssView(APIView):

    def post(self, request):
        serializer = JoatssSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = anthropic.Anthropic(
            api_key=os.environ['CLAUDE_API_KEY'],  # 환경 변수를 설정했다면 생략 가능
        )

        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=0.0,
            messages=[
                {"role": "user", "content": f"문장을 바꿔주는 데 다음과 같은 형식을 지켜서 바꿔줘. 1. 무조건 끝은 좋았쓰! 로 끝나야해 (~~ 하면 되니까 좋았쓰!) 2. 해당 문장을 긍정적인 의미로 바꿔야해. 3. 무조건 한 문장이어야 해 바꿀 문장은 '{serializer.validated_data['text']}'이야"}
            ]
        )

        answer: str = json.loads(message.model_dump_json())["content"][0]["text"]
        if not answer.endswith("좋았쓰!"):
            answer = "대답이 이상해서 개발자가 가로챘지만 다시 하면 될 것 같으니까 좋았쓰!"
        return Response({
            "result": answer
        })
