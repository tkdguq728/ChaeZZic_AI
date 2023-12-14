def extract_job(code_list):
    # "readme" 파일에 해당하는 코드 추출
    job_list = []
    for code in code_list:
        if "job" in code["name"].lower():
            readme_code_list.append({"name": code["name"], "contents": code["contents"]})
    
    return job_list
