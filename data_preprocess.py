import re


preprocess_pattern = re.compile(r"[^ .,?!/@$%~％·∼()\x00-\x7Fㄱ-ㅣ가-힣]+")
repeat_pattern = re.compile(r"(.)\1{2,}")
space_pattern = re.compile(r"\s+")


def text_preprocessing(text: str):
    text = preprocess_pattern.sub("", text)
    text = repeat_pattern.sub(r"\1" * 3, text)
    text = space_pattern.sub(" ", text)
    return text.strip()
