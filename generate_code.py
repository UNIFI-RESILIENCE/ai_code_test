import json
import requests
import os
import time

def read_prompts(file_path: str) -> list:
    """Read prompts from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_code(prompt: str, model_name: str) -> str:
    """Generate code using the OpenRouter API."""
    url = "https://openrouter.ai/api/v1/chat/completions"
    token = os.getenv("OPENROUTER_API_KEY")

    if not token:
        return "Error: OPENROUTER_API_KEY environment variable not set."

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    system_prompt = "You are a code assistant that helps generate python codes."
    user_prompt = f"Based on the following problem description, generate the optimum code for this prompt \n\n{prompt}\n\n. \
                    Do not include firstline function description in the generated code \
                    Format the code properly. All comments must be properly commented. The audience is software engineers."
    #"anthropic/claude-sonnet-4"
    data = {
        "model": model_name,
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
            #print(content)
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
    #openai/chatgpt-4o-latest , "deepseek/deepseek-chat-v3-0324" ,"qwen/qwen-2.5-coder-32b-instruct"
    llm_models=["openai/chatgpt-4o-latest" , "deepseek/deepseek-chat-v3-0324" ,"qwen/qwen-2.5-coder-32b-instruct"]
    #"coding_challenge", "humaneval"
    dataset=["coding_challenge", "humaneval", "benchmark"]
    type_flag = ''
    i = 0
    while i < len(dataset):
        if dataset[i] == "humaneval":
            prompts = read_prompts('transformed_prompt.json')
            type_flag = "humaneval"
        elif dataset[i] == "coding_challenge":
            prompts = read_prompts("transformed_challange.json")
            type_flag = "challenge"
        else:
            type_flag = "benchmark"
            prompts = read_prompts("humaneval_benchmark.json") 
        for model in llm_models:
            file_name_pref = ''
            if model == 'openai/chatgpt-4o-latest':
                file_name_pref = "LLM_GEN_GPT4"
            elif model == 'qwen/qwen-2.5-coder-32b-instruct':
                file_name_pref = "LLM_GEN_QWEN"
            else:
                file_name_pref = "LLM_GEN_DEEPCODER"

            for item in prompts:
                
                if dataset[i]=="benchmark":
                    function_name = int(item["task_id"].split('/')[-1])
                else:
                    function_name=item['function_name']
                print(f"Generating code for prompt: {type_flag} {function_name}")
                code = generate_code(item['prompt'], model)
                file_name = f"{file_name_pref}_{type_flag}/{function_name}.py"
                save_code(file_name, code)
                print(f"Saved generated code to {type_flag} {file_name}\n")
                time.sleep(1.5) 
        i += 1

if __name__ == "__main__":
    main()
