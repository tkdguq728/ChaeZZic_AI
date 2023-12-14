def link_questions_to_repo(reponame, questions):
    # reponame에 해당하는 질문 딕셔너리 생성 및 추가
    repo_questions = {
        "Repository Name": reponame,
        "Questions": questions
    }
    return repo_questions
