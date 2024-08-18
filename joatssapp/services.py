import re

from joatssapp.dtos import JoatssDto
from joatssapp.exceptions import FailedToGetJoatssAnswerError
from joatssapp.processors import AnthropicProcessor
from joatssapp.repositories import JoatssRepository
from joatssapp.utils import is_choseong_only


class JoatssService:
    def __init__(self) -> None:
        self.repository: JoatssRepository = JoatssRepository()
        self.processor: AnthropicProcessor = AnthropicProcessor()

    def get_joatss_answer(self, ip: str, text: str):
        self.repository.create_traffic(ip=ip)
        if is_choseong_only(text):
            raise FailedToGetJoatssAnswerError('초성 보다는 완벽한 문장이 좋았쓰!')
        prompt: str = (
            "문장을 바꿔주는 데 다음과 같은 형식을 지켜서 바꿔줘."
            "1. 무조건 끝은 좋았쓰! 로 끝나야해 (~~ 하면 되니까 좋았쓰!)."
            "2. 해당 문장을 긍정적인 의미로 바꿔야해."
            "3. 무조건 한 문장이어야"
            f"바꿀 문장은 {text}이야"
        )
        if text == '':
            raise FailedToGetJoatssAnswerError('빈 문장 보다는 완벽한 문장이 좋았쓰!')
        answer: str = re.split(r'(?<=[.!?])\s+', self.processor.get_answer_of_claude(prompt=prompt))[-1]
        if not answer.endswith('좋았쓰!'):
            raise FailedToGetJoatssAnswerError('대답이 이상해서 개발자가 가로챘지만 다시 하면 될 것 같으니까 좋았쓰!')
        return JoatssDto(
            answer=answer,
        )
