import re


def is_choseong_only(text: str) -> bool:
    choseong_pattern = re.compile(r'^[ㄱ-ㅎ\s]+$')
    return bool(choseong_pattern.match(text))
