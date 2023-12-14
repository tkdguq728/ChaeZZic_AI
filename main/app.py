from flask import Flask, request, jsonify
from code_filter import extract_code_by_language
from readme_filter import extract_readme_code
from readme_processing import remove_markdown
from readme_sum import summarize_readme
from gen_code import generate_code_related_questions
from gen_jobproj import generate_job_and_project_questions
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/generate_AI', methods=['POST'])
def generate_Ai():
    try:
      # JSON 데이터 수신
      json_data = request.get_json()
        
      # JSON 데이터를 리스트로 변환
      data_list = json.loads(json_data)

      # job, portfolio 구분  
      job, portfolio = extract_job_and_portfolio(data)

      # 질문 저장할 리스트트
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

      return jsonify(all_repo_questions), 200
    except Exception as e:
      return jsonify({"message": "에러가 발생했습니다."}), 500

@app.route('/send_data_to_react', methods=['GET'])
def send_data_to_react():
    try:
        # JSON 데이터 수신 (아래 라인을 통해 실제로 /generate_AI 엔드포인트에 요청을 보냄)
        response = app.test_client().post('/generate_AI', json={})
        
        # generate_AI 함수의 응답을 가져옴
        generate_ai_response_data = response.get_json()

        # 리액트로 전달할 데이터
        data_for_react = {"questions": generate_ai_response_data.get("questions")}

        return jsonify(data_for_react), 200
    except Exception as e:
        return jsonify({"message": "에러가 발생했습니다."}), 500
        
if __name__ == '__main__':
    app.run(host='43.200.7.70', port=5000, debug=True)
