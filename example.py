# -*- coding: utf-8 -*-
import re
from scraper import vipsister23, yamachan01
from manager import downloader
import ini

# 다운로드 폴더 설정
path = ini.download_folder

# 이미지를 다운로드 할 Webpage 의 url
print()
print('vipsister23 혹은 yamachan01 의 페이지 주소를 입력하세요: ', end='')
url = input().strip()

# 서비스 대상 사이트 체크, 분기
sc = None
if re.match(r'http(s)?://(www.)?vipsister23.com/.*', url):
    sc = vipsister23.Scraper()
elif re.match(r'http(s)?://(www.)?yamachan01.com/.*', url):
    sc = yamachan01.Scraper()
else:
    print('Error: url 을 다시 확인해주세요. 스크립트를 종료합니다.')
    exit(1)

# 이미지 수집
title, images = sc.get_imges_from_url(url)

print()
print(f'다운로드 할 페이지 제목 : {title}')

# 이미지 다운로드
for image in images:
    downloader.download(path, image, title)

print('done!')
