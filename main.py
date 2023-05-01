import re
import os


def remove_unnecessary_words(text):
    unnecessary_words = ['はい', 'えっと','えーと','えーっと','まあ','じゃあ','あの',]
    for word in unnecessary_words:
        text = re.sub(r'\b' + word + r'\b', '', text)
    return text


def optimize_text(text):
    lines = text.split('\n')
    optimized_lines = []

    for line in lines:
        if not line.strip():
            continue
        if optimized_lines and not optimized_lines[-1].strip():
            optimized_lines.pop()
        optimized_lines.append(line.strip())

    optimized_text = ' '.join(optimized_lines)
    return optimized_text


file_path = 'audio1.txt'


# Replace 'your_file_path.txt' with the path to your text file
with open('audio1.txt', 'r', encoding='utf-8') as file:
    original_text = file.read()

with open(file_path, 'r', encoding='utf-8') as file:
    original_text = file.read()

text_without_unnecessary_words = remove_unnecessary_words(original_text)
optimized_text = optimize_text(text_without_unnecessary_words)

file_name, file_extension = os.path.splitext(file_path)
optimized_file_path = file_name + '_optimized' + file_extension

with open(optimized_file_path, 'w', encoding='utf-8') as optimized_file:
    optimized_file.write(optimized_text)

print(f"Optimized text has been saved to: {optimized_file_path}")
