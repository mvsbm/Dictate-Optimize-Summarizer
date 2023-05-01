import os
import openai

openai.api_key = "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"

def split_text(text, max_length=2048):
    tokens = text.split()
    chunks = []
    current_chunk = []

    for token in tokens:
        if len(current_chunk) + len(token) + 1 > max_length:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
        current_chunk.append(token)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def summarize_text(text, model="gpt-3.5-turbo", n=1, max_length=100):
    chunks = split_text(text, max_length)
    summaries = []

    for chunk in chunks:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes text."
                },
                {
                    "role": "user",
                    "content": f"短縮してください: {chunk}"
                }
            ],
            max_tokens=max_length,
            temperature=0.1,
        )
        summaries.append(response.choices[0].message["content"].strip())

    return " ".join(summaries)


file_path = "audio1_optimized.txt"

with open(file_path, "r", encoding="utf-8") as file:
    original_text = file.read()

summary = summarize_text(original_text)

file_name, file_extension = os.path.splitext(file_path)
summary_file_path = file_name + "_summary" + file_extension

with open(summary_file_path, "w", encoding="utf-8") as summary_file:
    summary_file.write(summary)

print(f"Summary has been saved to: {summary_file_path}")
