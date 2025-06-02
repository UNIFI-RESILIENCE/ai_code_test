import requests

def fetch_data(api_url):
    try:
        # Send a GET request to the API
        response = requests.get(api_url)
        
        # Check if the request was successful
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        # Parse the JSON response
        data = response.json()
        
        # Print the response data
        print("Response Data:")
        print(data)
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decode error: {json_err}")

if __name__ == "__main__":
    # Example API URL (this one returns a list of users from a placeholder API)
    api_url = "https://jsonplaceholder.typicode.com/users"
    
    # Fetch and print data from the API
    fetch_data(api_url)