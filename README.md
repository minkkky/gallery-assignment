# gallery-assignment
오픈 갤러리 Django 개발 테스트 과제  
- 기간 : 22.09.09 ~ 22.09.16  

Intro
---
[V] 회원가입 및 로그인, 작가 등록 신청  
[V] 등록된 작품 및 작가, 전시 목록 확인  
[V] 허가된 작가 계정의 작품 및 전시 등록  
[   ] 관리자의 통계 확인 및 작가 등록 신청에 대한 처리 페이지
  - 기능 구현은 안 되어 있음

Project
---
### 기술  
- Python
- Django
  - Django rest framework
- Javascript

### 실행환경 - 로컬 서버
- 레포지토리 클론  
`git clone https://github.com/minkkky/gallery-assignment.git`  
- 패키지 설치  
`pip install -r requirements.txt`  
- 마이그레이션  
`python manage.py makemigrations`  
`python manage.py migrate`   
- 서버 실행  
`python manage.py runserver`  

### ERD
![gallery erd 916](https://user-images.githubusercontent.com/104331869/190525676-f551ef49-2cc4-412e-b92c-d53fbb618106.png)

### API


