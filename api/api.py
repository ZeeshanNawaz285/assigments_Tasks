'''
# import requests module 
import requests 
  
# Making a get request 
response = requests.get('https://api.github.com/') 
  
# print response 
print(response) 
  
# print request status_code 
print(response.status_code) '''

import requests

# Define the base URL of the JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"

def get_users():
    """
    Fetches a list of users from the JSONPlaceholder API.
    """
    url = f"{BASE_URL}/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch users. Status code: {response.status_code}")
        return None

def main(output):
    # Fetch list of users
    users = get_users()
    if users:
        print("List of users:")
        for user in users:
            print(f"User ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
            try:
               with open(output, 'w') as file:
                 file.write(users)
               print(f"Data saved to {output} successfully.")
            except Exception as e:
               print(f"An error occurred while saving data to {output}: {e}")

# Example usage
if __name__ == "__main__":
    
  
    filename = "output.txt"
    main(filename)



#if __name__ == "__main__":
#    main()
