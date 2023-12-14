def extract_repo_info(project):
    reponame = project.get("repoName")
    language = project.get("language")
    files = project.get("files", [])
    return reponame, lang, files
