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

summary_text = tokenizer.decode(summary_text_ids[0], skip_special_tokens=True)

