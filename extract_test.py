import json

input_file = 'human-eval-v2-20210705.jsonl'  # change this to your actual input file
output_file = 'Prompt_With_Unit_Test.json'

tests = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        if not line.strip():
            continue
        data = json.loads(line)
        tests.append({
            'task_id': data.get('task_id'),
            'prompt': data.get('prompt'),  # Full prompt as-is
            'test': data.get('test')
        })

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(tests, f, indent=2)

print(f"✅ Saved {len(tests)} entries with full prompt to {output_file}")
