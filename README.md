# 커뮤니티 댓글 csv 데이터 모음

[fastAPI 기반 한국어 악플 탐지기](https://github.com/Team-M1/korean-malicious-comments-api)를 만들기 위해 직접 수집한 데이터 모음입니다.



디시인사이드의 댓글은 [DC Crawler](https://github.com/seunghyukcho/dc-crawler)를 포크해서 [수정한 크롤러](https://github.com/Team-M1/dc-crawler)를 사용하였고,

아카라이브의 댓글은 크롤러를 직접 만들어서 사용하였습니다. [아카라이브 크롤러](https://github.com/Bing-su/arcalive-crawler-python)

각 데이터가 어디에서 수집되었는지는 각각의 파일명에 나와있습니다.



#### all_data.csv

모든 데이터를 하나의 파일로 합친 것입니다.



#### kmcd_data.csv

[ZIZUN/korean-malicious-comments-dataset](https://github.com/ZIZUN/korean-malicious-comments-dataset)의 데이터에 이 저장소의 기준으로 레이블을 붙인 것입니다.





### 레이블

0, 1, 2 셋으로 각 댓글에 레이블을 붙였습니다.

| 레이블 | 0        | 1                  | 2         |
| ------ | -------- | ------------------ | --------- |
| 의미   | 악플아님 | 비속어 사용 ~ 악플 | 심한 악플 |

이 기준은 방송통신심의위원회의 [인터넷내용등급서비스](http://www.safenet.ne.kr/dstandard2.do)에서 언어 세부사항쪽의 내용을 참고하였으며,  
우리의 목표가 되는 커뮤니티들이 일상보다 비속에 관대한 점을 참고하여,  
심의 level3 = 1, level4 = 2를 목표로 하였으나,  
심의 기준으로는 level4일지라도 커뮤니티에서 자주 사용되는 몇몇 비속어(씹ㅇㅇ, 좆ㅇㅇ 등)는 단독으로만 사용된 경우 레이블을 1로 했습니다.

이 기준은 다소 주관적입니다.  
그래서 대신 일관성을 유지하기 위해 한 명이 모든 작업을 진행했습니다.  

데이터는 총 55172개가 있으며,  
0: 46574, 1: 7426, 2: 1172  
레이블별 데이터의 수는 이와 같습니다.  
비율로는 85:13:2 정도입니다.



------



###  data_preprocess.py

데이터를 전처리하려는 목적으로 만든 파일입니다. 실제로는 사용하지 않았습니다.  
`r"[^ .,?!/@$%~％·∼()\x00-\x7Fㄱ-ㅣ가-힣]+"` 이 패턴으로 한번 처리한 뒤,  
3번 이상 반복되는 문자를 3글자로 줄이고, 2칸 이상의 공백을 1칸으로 줄이는 기능을 하는 함수 `text_preprocessing`이 들어있습니다.





### json_to_raw_csv.py

가장 처음에 수집했던 `실시간베스트갤러리-210819.csv`는 csv파일로 수집했지만, 이후에 크롤러가 파일을 json형식으로 저장하도록 변경했습니다. `json_to_raw_csv.py`는 이렇게 수집된 json파일에서 모든 데이터에 대해 레이블으로 0이 붙어있는 csv파일을 생성해줍니다.



```py
python main.py raw_data/베스트_라이브_210904.json
```

처럼 사용합니다.

`-t`(옵션): 제목도 저장합니다.  
`-c`(옵션): 본문도 저장합니다. 