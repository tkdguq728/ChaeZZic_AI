from flask import Flask, request, jsonify
from code_filter import extract_code_by_language
from readme_filter import extract_readme_code
from readme_processing import remove_markdown
from readme_sum import summarize_readme
from gen_code import generate_code_related_questions
from gen_jobproj import generate_job_and_project_questions
from extract_repo_info import extract_job_and_portfolio
from extract_repo_info import extract_repo_info
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app, origins="43.200.7.70:3000")

@app.route('/generate_AI', methods=['POST'])
def generate_Ai():
    try:
        # JSON 데이터 수신
        json_data = request.get_json()

        # JSON 데이터를 리스트로 변환
        data_list = json_data if isinstance(json_data, list) else [json_data]

        # job, portfolio 구분
        job, portfolio = extract_job_and_portfolio(data_list)

        # 질문 저장할 리스트
        all_repo_questions = []

        for project in portfolio:
            # language랑 file_list 추출
            language = project['lang'] if 'lang' in project else ''
            files = project.get("file", [])

            # language에 따른 코드 추출후에 random하게 선택
            code_list = extract_code_by_language(files, language)
            selected_code_file = random.choice(code_list)
            selected_code = selected_code_file.get("contents")

            # readme 추출
            readme_contents = next((file_info["contents"] for file_info in files if file_info.get("name", "").lower() == "readme.md"), None)

            # readme 파일 전처리
            readme_processing = remove_markdown(readme_contents)
            readme_summarize = summarize_readme(readme_processing)

            # 직무와 README 질문 생성
            job_and_project_questions = generate_job_and_project_questions(job, readme_summarize)

            # 코드 관련 질문 생성
            code_related_questions = generate_code_related_questions(selected_code)

            # 질문 통합
            all_questions = job_and_project_questions + code_related_questions

            all_repo_questions.append(all_questions)

        questions_list = []
        for project_questions in all_repo_questions:
            for question in project_questions:
                questions_list.append({"question": question})

        return jsonify({"questions": questions_list}), 200

    except ValueError as ve:
        # JSON 디코딩 오류 처리
        error_message = f"JSON 디코딩 오류: {str(ve)}"
        app.logger.error(error_message)  # 로깅
        return jsonify({"error": error_message}), 400

    except Exception as e:
        # 예외 세부 정보를 반환
        error_message = f"에러가 발생했습니다: {str(e)}"
        app.logger.error(error_message)  # 로깅
        return jsonify({"error": error_message}), 500

@app.route('/send_data_to_react', methods=['GET'])
def send_data_to_react():
    try:
        # generate_AI 함수의 응답을 가져옴
        generate_ai_response_data = generate_Ai_logic()

        # 리액트로 전달할 데이터
        data_for_react = {"questions": generate_ai_response_data.get("questions")}

        return jsonify(data_for_react), 200
    except Exception as e:
        app.logger.error(f"에러가 발생했습니다: {str(e)}")  # 로깅
        return jsonify({"message": "에러가 발생했습니다."}), 500

def generate_Ai_logic():
    # /generate_AI 엔드포인트의 로직을 직접 호출
    response = app.test_client().post('/generate_AI', json={})
    return response.get_json()
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
