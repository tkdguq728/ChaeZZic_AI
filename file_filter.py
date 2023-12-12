import random
import re
import base64
import json_to_data

language_patterns = {
        "java": r"\.java$",
        "javascript": r"\.js$",
        "python": r"\.py$",
        "c": r"\.c$",
        "c#": r"\.cs$",
        "c++": r"\.cpp$",
        "kotlin": r"\.kt$",
}

language = 

pattern = language_patterns.get(language.lower())

file_list = json_to_data.file_list

filtered_files = [file for file in file_list if re.search(pattern, file['name'], re.IGNORECASE)]

selected_file = random.choice(filtered_files)
