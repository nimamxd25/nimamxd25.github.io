import requests
import os
import re
import imghdr
from PIL import Image
from io import BytesIO

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
}

file = '2022-12-07-落地式脚手架搭设要点'
with open(f'{file}.md', 'r', encoding='utf-8') as f:
    text = f.read()
    url = re.findall('https?://s1\.vika\.cn/space/[^()"\s]+', text)
    for i in range(len(url)):
        img_content = requests.get(url=url[i], headers=headers).content
        img_name = f'{file}-{i}.jpg'
        img_path = f'img/{img_name}'
        # if not os.path.exists(img_path):
        with open(img_path, mode='wb') as jpg:
            jpg.write(img_content)
            print(f'{url[i]}下载成功！')  

        ok = os.system(f'pypicgo -f {img_path}')

        github_url = f'https://raw.githubusercontent.com/nimamxd25/blogimg/main/img/{img_name}' 
        text = text.replace(url[i], github_url)


with open(f'{file}-new.md', 'w+', encoding='utf-8') as f:
    f.write(text)






# img_path = 'wallhaven-o37w99_2560x1440.png'

# ok = os.popen(f'pypicgo -f {img_path}')







