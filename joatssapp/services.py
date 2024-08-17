import re

from joatssapp.dtos import JoatssDto
from joatssapp.exceptions import FailedToGetJoatssAnswerError
from joatssapp.processors import JoatssProcessor
from joatssapp.repositories import JoatssRepository
from joatssapp.utils import is_choseong_only


class JoatssService:
    def __init__(self) -> None:
        self.repository: JoatssRepository = JoatssRepository()
        self.processor: JoatssProcessor = JoatssProcessor()

    def get_joatss_answer(self, ip: str, text: str):
        self.repository.create_traffic(ip=ip)
        if is_choseong_only(text):
            raise FailedToGetJoatssAnswerError('초성 보다는 완벽한 문장이 좋았쓰!')
        if text == '':
            raise FailedToGetJoatssAnswerError('빈 문장 보다는 완벽한 문장이 좋았쓰!')
        answer: str = re.split(r'(?<=[.!?])\s+', self.processor.create_joatss_message(text=text))[-1]
        if not answer.endswith('좋았쓰!'):
            raise FailedToGetJoatssAnswerError('대답이 이상해서 개발자가 가로챘지만 다시 하면 될 것 같으니까 좋았쓰!')
        return JoatssDto(
            answer=answer,
        )
