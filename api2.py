'''import requests
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

def save_data_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
            file.write(str(data))
            
        print(f"Data saved to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while saving data to {filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Specify the URL of the publicly available API
    api_url = "https://jsonplaceholder.typicode.com/posts"

    # Fetch data from the API
    api_data = fetch_data_from_api(api_url)
    
    # Save data to a text file
    if api_data:
        save_data_to_file(api_data, "output.json")
        
'''

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

def save_data_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
            file.write(str(data))
            
        print(f"Data saved to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while saving data to {filename}: {e}")


def get_names_from_file(filename1):
    Title1 = []
    with open(filename1, 'r') as file:
        for line in file:
            if line.startswith("title:"):
                Title1 = line.split(":")[1].strip()
                Title1.append(Title)
    return Title1

# Example usage
if __name__ == "__main__":

   # api_url = "https://jsonplaceholder.typicode.com/posts"

    # Fetch data from the API
  #  api_data = fetch_data_from_api(api_url)
    
    # Save data to a text file
  # if api_data:
  #      save_data_to_file(api_data, "output.json")


        filename1 = "output.json"
        Title = get_names_from_file(filename1)
        print("Names extracted from the file:")
        print(Title)



# Example usage
#if __name__ == "__main__":
    # Specify the URL of the publicly available API
 