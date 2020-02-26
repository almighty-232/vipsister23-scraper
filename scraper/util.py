import re
from . import vipsister23, yamachan01


def selector(url: str):
    check_result = list()
    check_result.append(vipsister23.Scraper().url_checker(url))
    check_result.append(yamachan01.Scraper().url_checker(url))
    filtered = list(filter(lambda x: x is not None, check_result))
    if len(filtered) == 0:
        raise RuntimeError('Error: 아직 구현되지 않은 웹페이지 입니다.')
    else:
        return filtered[0]
