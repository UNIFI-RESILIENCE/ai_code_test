import requests

def fetch_data(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Print the response in JSON format
        print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    # URL of the REST API
    api_url = "https://jsonplaceholder.typicode.com/posts/1"

    # Fetch and print the data from the API
    fetch_data(api_url)
```

### Explanation:
1. **Import the `requests` library**: This library is used to send HTTP requests.
2. **Define the `fetch_data` function**: This function takes a URL as an argument, sends a GET request to the URL, and prints the JSON response.
3. **Send a GET request**: The `requests.get(url)` function sends a GET request to the specified URL.
4. **Raise an exception for HTTP errors**: The `response.raise_for_status()` method will raise an HTTPError if the HTTP request returned an unsuccessful status code.
5. **Print the JSON response**: The `response.json()` method parses the JSON response and prints it.
6. **Exception handling**: The program handles HTTP errors and other exceptions to provide meaningful error messages.

### Running the Program:
Save the code to a file (e.g., `fetch_api_data.py`) and run it using Python:

```sh
python fetch_api_data.py