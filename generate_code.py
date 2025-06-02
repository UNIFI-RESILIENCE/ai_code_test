import json
import requests

def read_prompts(file_path: str) -> list:
    """Read prompts from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_code(prompt: str) -> str:
    """Generate code using the OpenRouter API."""
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "anthropic/claude-sonnet-4",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_data = response.json()

        # Debugging output to verify the structure
        print(f"Response data: {response_data}")

        # Verify response structure and extract content
        if 'choices' in response_data and len(response_data['choices']) > 0:
            content = response_data['choices'][0].get('message', {}).get('content', '').strip()

            # Extract only the code block
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
    with open(file_name, 'w') as file:
        file.write(code)

def main():
    prompts = read_prompts('python_prompts.json')
    for item in prompts:
        print(f"Generating code for prompt: {item['function_name']}")
        code = generate_code(item['prompt'])
        file_name = f"{item['function_name']}.py"
        save_code(file_name, code)
        print(f"Saved generated code to {file_name}\n")

if __name__ == "__main__":
    main()
