import re

def extract_code_by_language(code_list, language):
    # 입력된 언어에 해당하는 정규 표현식 패턴 가져오기
    pattern = language_patterns.get(language)
    
    if not pattern:
        return []  # 주어진 언어에 대한 정규 표현식 패턴이 없으면 빈 리스트 반환
    
    # 코드 리스트에서 주어진 언어에 해당하는 코드 추출
    filtered_code_list = []
    for code in code_list:
        if re.search(pattern, code["name"], re.IGNORECASE):
            filtered_code_list.append({"name": code["name"], "contents": code["contents"]})
    
    return filtered_code_list

# 예제 사용
language_patterns = {
    "java": r"\.java$",
    "javascript": r"\.js$",
    "python": r"\.py$",
    "c": r"\.c$",
    "c#": r"\.cs$",
    "c++": r"\.cpp$",
    "kotlin": r"\.kt$",
}

# 입력으로 주어진 코드 리스트
code_list = [
    {"name": "1.py", "contents": "Python code 1"},
    {"name": "2.py", "contents": "Python code 2"},
    {"name": "readme.md", "contents": "README contents"},
    {"name": "4.js", "contents": "JavaScript code"},
]

# 언어 선택 (예: "python")
selected_language = "python"

# 선택된 언어에 해당하는 코드 추출
filtered_code = extract_code_by_language(code_list, selected_language)
print(filtered_code)
