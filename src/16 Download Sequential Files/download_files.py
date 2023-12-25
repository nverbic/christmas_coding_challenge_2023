'''
Download Sequential Files

Output:
Downloaded: images\image001.jpg
...
Downloaded: images\image050.jpg
'''
import os
import requests
from io import BytesIO
from PIL import Image


def increment_url(current_url):
    base, ext = os.path.splitext(current_url)
    numeric_part = int(base.split("e")[-1])
    numeric_part += 1
    return f"{base.rsplit('e', 1)[0]}e{numeric_part:03d}{ext}"

def download_files(current_url, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    current_file_url = current_url

    while True:
        response = requests.get(current_file_url)

        # Check if the file exists (status code 200)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))

            # Extract the file name from the URL
            file_name = os.path.basename(current_file_url)

            # Save the file
            file_path = os.path.join(output_dir, file_name)
            image.save(file_path, format='JPEG')
            print(f"Downloaded: {file_path}")

            # Increment file path
            current_file_url = increment_url(current_file_url)
        else:
            # Break the loop if the file doesn't exist
            break

if __name__ == '__main__':
    download_files('http://699340.youcanlearnit.net/image001.jpg', 'images')
