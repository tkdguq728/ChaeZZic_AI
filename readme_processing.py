# README 파일 전처
import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration
import re

tokenizer = PreTrainedTokenizerFast.from_pretrained('digit82/kobart-summarization')
model = BartForConditionalGeneration.from_pretrained('digit82/kobart-summarization')

def remove_markdown(readme_text):
    # 코드 블럭 제거
    readme_text = re.sub(r'```.*?```', '', readme_text, flags=re.DOTALL)
    # HTML 태그 제거
    readme_text = re.sub(r'<[^>]+>', '', readme_text)
    # 이미지 태그 제거
    readme_text = re.sub(r'!\[.*?\]\(.*?\)', '', readme_text)
    # 링크 제거
    readme_text = re.sub(r'\[.*?\]\(.*?\)', '', readme_text)
     # '#' 기호 제거
    readme_text = re.sub(r'#', '', readme_text)
    # '*' 기호 제거
    readme_text = re.sub(r'\*', '', readme_text)
    return readme_text
