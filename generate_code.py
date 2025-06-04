import json
import requests
import os

def read_prompts(file_path: str) -> list:
    """Read prompts from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_code(prompt: str) -> str:
    """Generate code using the OpenRouter API."""
    url = "https://openrouter.ai/api/v1/chat/completions"
    token = os.getenv("OPENROUTER_API_KEY")

    if not token:
        return "Error: OPENROUTER_API_KEY environment variable not set."

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    system_prompt = "You are a code assistant that helps generate codes."
    user_prompt = f"Based on the following problem description, generate the optimum code for this prompt \n\n{prompt}\n\n"
    #"anthropic/claude-3-sonnet"
    data = {
        "model": "openai/chatgpt-4o-latest",
        "messages": [
            {
                "role": "user",
                "content": user_prompt
            },
            {
                "role": "system", 
                "content": system_prompt},
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_data = response.json()

        if 'choices' in response_data and len(response_data['choices']) > 0:
            content = response_data['choices'][0].get('message', {}).get('content', '').strip()

            if "```python" in content:
                start_index = content.find("```python") + len("```python")
                end_index = content.rfind("```")
                code_content = content[start_index:end_index].strip()
                return code_content
            else:
                print("No code block detected. Raw content returned.")
                return content.strip()
        else:
            print(f"Unexpected response structure: {response_data}")
            return "Error: No valid content found."

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")

    return "Error: Failed to generate code."

def save_code(file_name: str, code: str):
    """Save the generated code to a file."""
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as file:
        file.write(code)

def main():
    prompts = read_prompts('transformed_prompt.json')
    for item in prompts:
        print(f"Generating code for prompt: {item['function_name']}")
        code = generate_code(item['prompt'])
        file_name = f"LLM_GEN/{item['function_name']}.py"
        save_code(file_name, code)
        print(f"Saved generated code to {file_name}\n")

if __name__ == "__main__":
    main()
