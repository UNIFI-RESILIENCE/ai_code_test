import json
import requests

def read_prompts(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_code(prompt: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer ",
        "Content-Type": "application/json"
    }
    data = {
        "model": "anthropic/claude-3-sonnet",
        "prompt": prompt,
        "max_tokens": 1000
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['text']

def save_code(file_name: str, code: str):
    with open(file_name, 'w') as file:
        file.write(code)

def main():
    test_files = [
        "/home/jnkoro/Documents/Thesis 2025/Implementation/HotelProject-main/src/test/java/hotel/HotelRoomViewTest.java",
        "/home/jnkoro/Documents/Thesis 2025/Implementation/HotelProject-main/src/test/java/hotel/RoomControllerTest.java",
        "/home/jnkoro/Documents/Thesis 2025/Implementation/HotelProject-main/src/test/java/hotel/RoomPostgresRepositoryTest.java",
        "/home/jnkoro/Documents/Thesis 2025/Implementation/HotelProject-main/src/test/java/hotel/RoomTest.java"
    ]

    for test_file in test_files:
        with open(test_file, 'r') as file:
            test_code = file.read()
            prompt = f"Generate Java code to implement the unit tests in the following file:\n\n{test_code}"
            generated_code = generate_code(prompt)
            save_code(f"{test_file.split('/')[-1].replace('.java', '')}.java", generated_code)

if __name__ == "__main__":
    main()
