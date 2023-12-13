import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration


def summarize_readme(cleaned_readme):
    # 모델 및 토크나이저 로드
    tokenizer = PreTrainedTokenizerFast.from_pretrained('digit82/kobart-summarization')
    model = BartForConditionalGeneration.from_pretrained('digit82/kobart-summarization')

    # 입력 텍스트를 인코딩
    input_ids = tokenizer.encode(cleaned_readme, return_tensors='pt')

    # 시작 토큰 및 종료 토큰 추가
    input_ids = [tokenizer.bos_token_id] + input_ids.tolist() + [tokenizer.eos_token_id]
    input_ids = torch.tensor(input_ids)

    # 요약 생성
    summary_text_ids = model.generate(
        input_ids=input_ids,
        bos_token_id=model.config.bos_token_id,
        eos_token_id=model.config.eos_token_id,
        length_penalty=1.0,
        max_length=256,
        min_length=64,
        num_beams=5
    )

    # 요약 결과 디코딩
    summary_text = tokenizer.decode(summary_text_ids[0], skip_special_tokens=True)

    return summary_text

