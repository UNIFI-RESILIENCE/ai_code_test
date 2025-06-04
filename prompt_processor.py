import json
import requests
import time
import os
import re


#openai/chatgpt-4o-latest
#deepseek/deepseek-chat-v3-0324
MODEL = "openai/chatgpt-4o-latest"  # Or another simple model from OpenRouter
token = os.getenv("OPENROUTER_API_KEY") 

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def infer_function_name(prompt):
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


    system_prompt = "You are an assistant that helps convert programming questions into descriptive  function names."
    user_prompt = f"Avoid infering name based on competitive programming \
                    platforms. Also avoid common function names like A, based, B etc.. Based on the following problem, suggest a concise and descriptive Python function name:\n\n{prompt}\n\nFunction name:  "
   
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    response.raise_for_status()
    content = response.json()
    
    answer = content["choices"][0]["message"]["content"].strip()

    answer = answer.split()[0].strip().strip("():")  # just the function name
    answer = answer.replace("-", "_")
    print(answer)
    return answer


def transform_data1(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    transformed = []
    for item in data:
        #prompt = f"{item['question_title']}\n\n{item['question_content']}"
        prompt = f"{item['question_content']}"
        print(f"Inferring function name for: {item['question_id']}")
        function_name = infer_function_name(prompt)
        transformed.append({
            "function_name": function_name,
            "prompt": prompt,
            "test_code": ""
        })
        
        time.sleep(1.5)  # be nice to the API

    with open(output_file, 'w') as f:
        json.dump(transformed, f, indent=4)

def transform_data2(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    transformed = []
    for item in data:
        #combined_prompt = item['prompt'].strip() + "\n\n" + item['test'].strip()
        combined_prompt = item['prompt'] + "\n\n" + item['test']
        print(f"Inferring function name from LLM prompt + test...")
        function_name = infer_function_name(combined_prompt)
        transformed.append({
            "function_name": function_name,
            "prompt": combined_prompt,
            "test_code": ""
        })
        time.sleep(1.5)

    with open(output_file, 'w') as f:
        json.dump(transformed, f, indent=4)

# Run
transform_data1('coding_challange_problems.json', 'transformed_challange.json')
transform_data2('prompt_with_unit_test.json', 'transformed_prompt.json')
