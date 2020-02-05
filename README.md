# Vipsister23 의 사진을 수집하자!

웹사이트 [Vipsister23](http://vipsister23.com)의 짤을 수집하기 위한 스크립트

## 실행
### 전제조건
    `Python`이 설치되어 있는 환경일 것
### 사전준비
    1. 다운받은 `vipsister23-scraper`의 압축을 해제한다
    2. `ini.py` 파일을 메모장으로 열어 다운받을 폴더의 경로를 자신의 것으로 변경한다
### 실행방법
1. 커맨드 프롬프트(또는 터미널)을 연다
1. `vipsister23-scraper` 를 다운받은 폴더로 이동(cd)한다
1. 필요한 라이브러리를 설치하기 위해 아래의 커맨드를 커맨드 프롬프트에 입력 후 실행(엔터)한다.
    ```
    $ python -m pip install -r requirements.txt
    ```
1. 아래의 명령어를 실행한다
    ```
    $ python example.py
    ```
1. `url` 을 붙여넣기 한 후 엔터키를 입력한다
1. 정상적으로 실행될 경우 아래와 같은 메시지가 출력된다
    ```
    SuhongnoMacBook-Pro:img-scraper suhong$ python example.py
    vipsister23의 페이지 주소를 입력하세요: http://vipsister23.com/archives/9564599.html

    다운로드 할 페이지 : 【画像】広瀬すず、巨乳だった
    Downloading... /Users/suhong/Downloads/【画像】広瀬すず、巨乳だった/eaea9c2c.jpg
    Downloading... /Users/suhong/Downloads/【画像】広瀬すず、巨乳だった/7ea12ecc.jpg
    Downloading... /Users/suhong/Downloads/【画像】広瀬すず、巨乳だった/feb91183.jpg
    Downloading... /Users/suhong/Downloads/【画像】広瀬すず、巨乳だった/61fc3b44.jpg
    Downloading... /Users/suhong/Downloads/【画像】広瀬すず、巨乳だった/30afa3f3.jpg
    Downloading... /Users/suhong/Downloads/【画像】広瀬すず、巨乳だった/59efbe72.jpg
    Downloading... /Users/suhong/Downloads/【画像】広瀬すず、巨乳だった/15b169e3.jpg
    Downloading... /Users/suhong/Downloads/【画像】広瀬すず、巨乳だった/91496627.jpg
    Downloading... /Users/suhong/Downloads/【画像】広瀬すず、巨乳だった/b7d64045.jpg
    Downloading... /Users/suhong/Downloads/【画像】広瀬すず、巨乳だった/d35f0166.jpg
    done!
    ```
