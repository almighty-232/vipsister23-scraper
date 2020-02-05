# -*- coding: utf-8 -*-
import re
from vipsister23 import scraper
from manager import downloader
import ini

# 다운로드 폴더 설정
path = ini.download_folder

# 이미지를 다운로드 할 vipsister23 의 url
print()
print('vipsister23의 페이지 주소를 입력하세요: ', end='')
url = input().strip()
if not re.match(r'http://vipsister23.com/.*.html', url):
    print('Error: url 을 다시 확인해주세요. 스크립트를 종료합니다.')
    exit(1)

# 이미지 수집
title, images = scraper.get_imges_from_url(url)

print()
print(f'다운로드 할 페이지 제목 : {title}')

# 이미지 다운로드
for image in images:
    downloader.download(path, image, title)

print('done!')
