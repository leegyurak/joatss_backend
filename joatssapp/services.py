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
        if text == '':
            raise FailedToGetJoatssAnswerError('빈 문장 보다는 완벽한 문장이 좋았쓰!')
        if text.endswith('?'):
            prompt: str = (
                "질문에 대답을 다음과 같은 형식을 지켜서 해줘."
                "1. 무조건 끝은 좋았쓰! 로 끝나야해 (~~ 하면 되니까 좋았쓰!)."
                "2. 대답은 긍정적인 의미여야 해."
                "3. 무조건 한 문장이어야 해"
                "4. 너의 이름은 좋았쓰! 변환기야"
                f"질문은 {text}이야"
            )
        else:
            prompt: str = (
                "문장을 다음과 같은 형식을 지켜서 바꿔줘."
                "1. 무조건 끝은 좋았쓰! 로 끝나야해 (~~ 하면 되니까 좋았쓰!)."
                "2. 바꾼 문장은 긍정적인 의미여야 해."
                "3. 무조건 한 문장이어야 해"
                f"바꿀 문장은 {text}이야"
            )
        answer: str = re.split(r'(?<=[.!?])\s+', self.processor.get_answer_of_claude(prompt=prompt))[-1]
        if not answer.endswith('좋았쓰!'):
            raise FailedToGetJoatssAnswerError('결과가 이상해서 개발자가 가로챘지만 다시 하면 될 것 같으니까 좋았쓰!')
        return JoatssDto(
            answer=answer,
        )
