import openai
import random
import base64

# OpenAI API 키 설정
api_key = "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"
openai.api_key = api_key

# GPT-3를 사용하여 코드 관련 질문 생성
def generate_code_related_questions(code):
    prompt = f"""첫 번째, 코드를 확인
                 두 번째, 코드에서 함수와 제어문에 대한 부분을 확인
                 세 번째, 확인한 부분에서 면접 예상 질문을 생성
                 네 번째, 질문은 한 개만 생성
                 다섯 번째, 질문은 한글로 생성
                 여섯 번째, 찾은 함수와 제어문에 대한 질문을 생성
                 일곱 번쟤, 찾은 함수와 제어문에 대한 질문을 생성하고, 코드이 전체에 대한 질문은 제외해줘
                 일곱 번째, 함수의 구현이나 반환 혹은 연결된 부분에 대한 질문을 위주로 생성
                 여덟 번째, 생성한 질문만 출력해줘
                 아홉 번째, 생성한 질문에 대한 답변까지 생성해서 출력
                 열 번째, 생성한 질문에 대한 설명은 제거해줘
                 :\n{code}"""
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3 엔진 선택
        prompt=prompt,
        max_tokens=500,  # 생성할 최대 토큰 수
        n=2,  # 생성할 코드 관련 질문 수
        stop=None,  # 생성 중지 단어 설정 (생략 가능)
        temperature=1.0  # 다양성 조절 (0.2부터 1.0까지의 값 사용)
    )
    
    # 생성된 코드 관련 질문 추출
    code_related_questions = [question.text.strip() for question in response.choices]
    
    return code_related_questions
    
code_to_analyze = """
import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration

tokenizer = PreTrainedTokenizerFast.from_pretrained('digit82/kobart-summarization')
model = BartForConditionalGeneration.from_pretrained('digit82/kobart-summarization')

input_ids = tokenizer.encode(cleaned_readme)

input_ids = [tokenizer.bos_token_id] + input_ids + [tokenizer.eos_token_id]
input_ids = torch.tensor([input_ids])
summary_text_ids = model.generate(
    input_ids = input_ids,
    bos_token_id = model.config.bos_token_id,
    eos_token_id = model.config.eos_token_id,
    length_penalty = 1.0, # 길이에 대한 penalty 값. 1보다 작은 경우 더 짧은 문장을 생성하도록 유도하며, 1보다 클 경우 길이가 더 긴 문장을 유도
    max_length = 256, # 요약문의 최대 길이 설정
    min_length = 64, # 요약문의 최소 길이 설정
    num_beams = 5) # 문장 생성 시 다음 단어를 탐색하는 영역의 개수

print(tokenizer.decode(summary_text_ids[0], skip_special_tokens=True))
"""

# 코드 관련 질문 생성
code_questions = generate_code_related_questions(code_to_analyze)
for i, question in enumerate(code_questions, start=1):
    print(f"Question {i}: {question}")
