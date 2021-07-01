# 크롤링(bash)



## sed 명령어

- 문자열의 특정내용을 변경 및 줄단위 추출
- 파일이름을 지정하면 해당파일을 처리, 파일이름을 미지정하면 표준입력 기반으로 처리

```bash
sed <옵션> <명령어> <파일이름>
```



- 예제) smaple.txt 파일 내용의 ''장 :' 부분을 '장' 으로 바꾸기

```bash
1장 : 크롤러를 지탱하는 기술
2장 : TTTP 이해하기
3장 : 문자 개찜 해결하기
4장 : 스크레이핑 테크닉
5장 : 인증하기
6장 : 크롤링 응용 테크닉
7장 : 자바스크립트 가지고 놀기
```

- 명령어 실행시 다음과 같이 출력

```bash
명령어 : sed s/장 :/장/ sample.txt

1장 크롤러를 지탱하는 기술
2장 TTTP 이해하기
3장 문자 개찜 해결하기
4장 스크레이핑 테크닉
5장 인증하기
6장 크롤링 응용 테크닉
7장 자바스크립트 가지고 놀기
```

- sample.txt 파일의 수정내용을 new_sample.txt로 저장

```bash
sed s/장 : /장/ sample.txt > new_sample.txt
```



## grep 명령어

- 표준입력, 패턴에 맞는 줄을 찾아 표준출력에 출력하는 명령어

``` bash
grep <패턴> <파일이름>

index.html 에서 title을 포함하고 있는 제목 불러오기
grep class =\"title-text\" index.html

출력 ex)
<span class = "title-text">파이썬으로 배우는 알고리즘 (개정판)/</span>
```



## grep / sed 명령어로 파일내용 정리

```bash
앞부분의 <span class = "title-text"> 삭제하기

grep class = \"title-text\" index.html | sed -e 's/.*\"title-text\"//'

명령어 실행 후
파이썬으로 배우는 알고리즘 (개정판)/ </span>

뒤에 </span> 삭제하기

grep class = \"title-text\" index.html | sed -e 's/.*\"title-text\"//;
sed -e 's/<\/span\>//'

명령어 실행 후
파이썬으로 배우는 알고리즘 (개정판)
```

