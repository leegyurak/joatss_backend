import json
import os

from anthropic import Anthropic
from anthropic.types import Message


class JoatssProcessor:
    def __init__(self) -> None:
        self.client: Anthropic = Anthropic(
            api_key=os.environ['CLAUDE_API_KEY'],  # 환경 변수를 설정했다면 생략 가능
        )

    def create_joatss_message(self, text: str) -> str:
        prompt: str = (
            "문장을 바꿔주는 데 다음과 같은 형식을 지켜서 바꿔줘."
            "1. 무조건 끝은 좋았쓰! 로 끝나야해 (~~ 하면 되니까 좋았쓰!)."
            "2. 해당 문장을 긍정적인 의미로 바꿔야해."
            "3. 무조건 한 문장이어야"
            f"바꿀 문장은 {text}이야"
        )
        message: Message = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=0.0,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return json.loads(message.model_dump_json())["content"][0]["text"]