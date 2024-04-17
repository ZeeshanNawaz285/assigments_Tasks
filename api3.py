import requests
import json

def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data from API. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_data_to_json_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while saving data to {filename}: {e}")

def save_specific_data_to_file(data, specific_key, filename):
    try:
        specific_data = [item[specific_key] for item in data]
        with open(filename, 'w') as file:
            file.write('\n'.join(map(str, specific_data)))
        print(f"Specific data saved to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while saving specific data to {filename}: {e}")

if __name__ == "__main__":
    #api_url = "https://jsonplaceholder.typicode.com/posts"
    api_url =  "https://aws.amazon.com/about-aws/whats-new/recent/feed/"

    api_data = fetch_data_from_api(api_url)
    
    
    if api_data:
        save_data_to_json_file(api_data, "apioutput.json")
        
        
        specific_key = 'title' 
        save_specific_data_to_file(api_data, specific_key, "specific_data.txt")
