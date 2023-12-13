def extract_readme_code(code_list):
    # "readme" 파일에 해당하는 코드 추출
    readme_code_list = []
    for code in code_list:
        if "readme" in code["name"].lower():
            readme_code_list.append({"name": code["name"], "contents": code["contents"]})
    
    return readme_code_list
