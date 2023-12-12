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
