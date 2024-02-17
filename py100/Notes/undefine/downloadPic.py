import requests
from requests.auth import HTTPBasicAuth

def download_file_with_auth(url, local_filename, username, password):
    response = requests.get(url, auth=HTTPBasicAuth(username, password), stream=True)
    with open(local_filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

url = "https://www.example.com/secure-file.pdf"  # 替换成需要认证的文件 URL
local_filename = "secure-file.pdf"  # 保存到本地的文件名
username = "your_username"  # 替换为你的用户名
password = "your_password"  # 替换为你的密码

download_file_with_auth(url, local_filename, username, password)
print(f"File '{local_filename}' downloaded and saved.")
