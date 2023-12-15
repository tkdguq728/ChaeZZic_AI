import openai

# OpenAI API 키 설정
api_key = "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"
openai.api_key = api_key

# GPT-3를 사용하여 직무와 프로젝트 관련 질문 생성
def generate_job_and_project_questions(job_description, project_description):
    prompt = f"""첫째, 직무 설명와 프로젝트 설명을 확인하세요.
                 둘째, 그에 대한 예상 면접 질문을 생성하세요.
                 셋째, 질문은 1개만 생성하세요
                 넷째, 질문은 한 문장으로 완성시키세요
                 다섯째, 질문은 의문형으로 생성
                 여섯째, 직무에 대한 직접적인 질문은 제외
                 여섯째, 프로젝트에 대한 직접적인 질문은 제외
                 일곱째, 질문은 가능한 한 개발에 관련되도록 생성해주세요
                 여덟째, 프로젝트에 대한 설명은 제외하세요
                 여덟째, 생성한 질문만 출력하세요.
                 아홉쨰, 생성한 질문에 대한 답변도 생성해줘
                 열번째, 사용한 언어에 대한 질문은 제외해줘
                 열한번째, 커뮤니케이션에 대한 질문을 1개만 생성해줘
                 \n\n직무 설명: {job_description}\n\n프로젝트 설명: {project_description}"""
    
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=500,  # 생성할 최대 토큰 수
        n=3,  # 질문 수
        stop=None,  # 생성 중지 단어 설정 (생략 가능)
        temperature=1.0,  # 다양성 조절 (0.2부터 1.0까지의 값 사용)
    )
    
    # 생성된 직무와 프로젝트 관련 질문 추출
    job_and_project_questions = [question.text.strip() for question in response.choices]
    
    return job_and_project_questions
