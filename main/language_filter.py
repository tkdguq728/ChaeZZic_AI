def extract_language(code_list):
    # "readme" 파일에 해당하는 코드 추출
    language_list = []
    for code in code_list:
        if "language" in code["name"].lower():
            language_list.append({"name": code["name"], "contents": code["contents"]})
    
    return language_list
