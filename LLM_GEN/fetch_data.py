import requests

# Define the API endpoint URL
url = "https://api.example.com/data"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print the response content
    print(response.text)
else:
    print(f"Error: {response.status_code}")
```

Here's how the code works:

1. We import the `requests` library, which is a popular Python library for making HTTP requests.

2. We define the URL of the API endpoint we want to connect to. In this example, we're using `"https://api.example.com/data"`, but you'll need to replace it with the actual URL of the API you want to access.

3. We send a GET request to the API endpoint using the `requests.get()` function and store the response in the `response` variable.

4. We check if the request was successful by checking if the `status_code` attribute of the `response` object is equal to 200 (which is the HTTP status code for a successful request).

5. If the request was successful, we print the content of the response using the `response.text` attribute, which returns the response body as a string.

6. If the request was not successful, we print an error message that includes the HTTP status code of the failed response.

Note that this is a very basic example, and you may need to modify it depending on the specific API you're accessing and any authentication or other requirements it may have. Additionally, the response content may be in a specific format (e.g., JSON or XML), so you may need to parse the response accordingly.

Here's an example of how you might parse a JSON response:

```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Process the JSON data as needed
    print(data)
else:
    print(f"Error: {response.status_code}")