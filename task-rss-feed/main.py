
# comparing data from two files old and new 


import xml.etree.ElementTree as ET
import requests
import json 
from datetime import datetime, timedelta
import time


def save_url_data_to_file(url, output_file):
    
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            f.write(response.content)
        print("Data saved to", output_file)
    else:
        print("Failed to retrieve data from the URL")


def extract_specific_keys(xml_file, key_name):
    tree = ET.parse(xml_file)  
    return [element.text for element in tree.iter() if element.tag == key_name]

def save_to_file(data, output_file):
    with open(output_file, 'w') as f:
         json.dump(data, f, indent=4)
         #f.write("\n".join(data))




while True:
    update_timeset = 1
    next_update_time = datetime.now() + timedelta(minutes=update_timeset)
    print(f"Next update in 10 sec at {next_update_time.strftime('%H:%M:%S')}")
    time.sleep(update_timeset * 60/6)


    api_url =  "https://aws.amazon.com/about-aws/whats-new/recent/feed"

    xml_file_path = 'url_data.xml'
    latest_data = save_url_data_to_file(api_url, xml_file_path)


    key_to_extract = 'title'

    extracted_data = extract_specific_keys(xml_file_path, key_to_extract)

    output_file_path = 'RSS-feed.json'
    save_to_file(extracted_data, output_file_path)

    with open('old-feed.json', 'r') as file:
        data1 = json.loads(file.read())

    with open('RSS-feed.json', 'r') as file:
        data2 = json.loads(file.read())

    for item in data2:
        if item not in data1:
            data1.append(item)


    with open('old-feed.json' , 'w') as file :
        json.dump(data1, file, indent=4)

