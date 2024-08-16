import anthropic
import json
import os
import re

from rest_framework.response import Response
from rest_framework.views import APIView

from joatssapp.serializers import JoatssSerializer


class JoatssView(APIView):
    def is_choseong_only(self, text):
        # 한글 초성 Unicode 범위 (ㄱ부터 ㅎ까지)
        choseong_pattern = re.compile(r'^[ㄱ-ㅎ\s]+$')
        
        # 문자열이 초성만으로 이루어져 있는지 확인합니다.
        return bool(choseong_pattern.match(text))

    def post(self, request):
        serializer = JoatssSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = anthropic.Anthropic(
            api_key=os.environ['CLAUDE_API_KEY'],  # 환경 변수를 설정했다면 생략 가능
        )
        if self.is_choseong_only(serializer.validated_data['text']):
            return Response({
                "result": "초성보다는 풀 문장이 더 좋았쓰!"
            })

        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=0.0,
            messages=[
                {"role": "user", "content": f"문장을 바꿔주는 데 다음과 같은 형식을 지켜서 바꿔줘. 1. 무조건 끝은 좋았쓰! 로 끝나야해 (~~ 하면 되니까 좋았쓰!) 2. 해당 문장을 긍정적인 의미로 바꿔야해. 3. 무조건 한 문장이어야 해 바꿀 문장은 '{serializer.validated_data['text']}'이야"}
            ]
        )

        answer: str = json.loads(message.model_dump_json())["content"][0]["text"]
        answer = re.split(r'(?<=[.!?])\s+', answer)[1]
        if not answer.endswith("좋았쓰!"):
            answer = "대답이 이상해서 개발자가 가로챘지만 다시 하면 될 것 같으니까 좋았쓰!"
        return Response({
            "result": answer
        })
