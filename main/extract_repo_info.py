def extract_job_and_portfolio(data):
    job = data.get("job")
    portfolio = data.get("portfolio", [])
    return job, portfolio

def extract_repo_info(projects):
    repo_info_list = []
    for project in projects:
        reponame = project.get("reponame")
        lang = project.get("lang")
        files = project.get("file", [])
        repo_info = {"reponame": reponame, "lang": lang, "files": files}
        repo_info_list.append(repo_info)
    return repo_info_list
