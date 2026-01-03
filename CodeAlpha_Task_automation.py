import os
import shutil
import re
import requests

def move_jpg_files(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    files = os.listdir(source_dir)
    for file in files:
        if file.lower().endswith(".jpg"):
            shutil.move(os.path.join(source_dir, file), os.path.join(target_dir, file))

def extract_emails(input_file, output_file):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    try:
        with open(input_file, 'r') as f:
            content = f.read()
        emails = re.findall(email_pattern, content)
        with open(output_file, 'w') as f:
            for email in set(emails):
                f.write(email + '\n')
    except FileNotFoundError:
        pass

def scrape_title(url, save_file):
    try:
        response = requests.get(url)
        title_search = re.search('<title>(.*?)</title>', response.text, re.IGNORECASE)
        if title_search:
            title = title_search.group(1)
            with open(save_file, 'w') as f:
                f.write(title)
    except:
        pass

if __name__ == "__main__":
    # move_jpg_files('source_folder', 'destination_folder')
    # extract_emails('input.txt', 'output.txt')
    # scrape_title('https://www.google.com', 'title.txt')
    pass