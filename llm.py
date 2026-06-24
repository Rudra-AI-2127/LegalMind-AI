import ollama


def ask_llm(prompt):

    try:

        response = ollama.chat(
            model="qwen2.5:7b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"Error: {e}"