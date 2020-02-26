# -*- coding: utf-8 -*-
import re
import os
import urllib.request
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


def download(path: str, url: str, subdir: str = None):
    # make subdirectory if `subdir` is not none
    if subdir:
        path = f'{path}/{subdir}'
        os.makedirs(path, exist_ok=True)
    # extract file name from url
    re_pattern = '[0-9a-z]+.(jpg|png|gif)'
    regex_result = re.search(re_pattern, url)
    if not regex_result:
        type_nm = url.split('.')[-1]
        print(f'Error: Not Supported Multimedia Type : {type_nm} Url : {url}')
    else:
        nm = regex_result.group()
        # file name
        f_name = f'{path}/{nm}'
        # download
        print(f'Downloading... {f_name}')
        urllib.request.urlretrieve(url, f_name)

