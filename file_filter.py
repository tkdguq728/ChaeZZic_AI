import random
import re
import base64

language_patterns = {
        "java": r"\.java$",
        "javascript": r"\.js$",
        "python": r"\.py$",
        "c": r"\.c$",
        "c#": r"\.cs$",
        "c++": r"\.cpp$",
        "kotlin": r"\.kt$",
}

language = "python"

pattern = language_patterns.get(language.lower())

filtered_files = [file for file in file_list if re.search(pattern, file['name'], re.IGNORECASE)]

selected_file = random.choice(filtered_files)

encoded_contents = selected_file['contents'].encode('utf-8')
encoded_contents_base64 = base64.b64encode(encoded_contents).decode('utf-8')
