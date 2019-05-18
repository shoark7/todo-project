# Parkito's todo list README

#### Last modified: 2019-05-18
#### 지원분야: 웹/서버

<br>

## 로컬에서 테스트하기

운영체제는 리눅스를 기준으로 하고, 파이썬을 위한 가상환경 구성이 가능하다고 가정합니다. 저는 `pipenv`를 사용하고 있습니다.  

전체 코드를 복사-붙여넣기 하시면 바로 `127.0.0.1:8000`로 테스트 해보실 수 있는데요. 시스템 환경변수 등은 건드리지 않으니 걱정 안 하셔도 됩니다. 그리고 `pipenv`이 들어간 코드는 사용하시는 가상환경 구성방법에 맞게 변형하시면 됩니다.

```sh
git clone https://github.com/shoark7/todo-project.git
cd todo-project
export SECRET_KEY='1231u24jkasdkfajskfh;k1jhasddfaskdfhla'
pipenv install django python-decouple
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```


만약 전역 파이썬 모듈 스페이스를 써도 상관없다고 하시면 다음 코드를 붙여넣으시면 됩니다.


```sh
git clone https://github.com/shoark7/todo-project.git
cd todo-project
export SECRET_KEY='1231u24jkasdkfajskfh;k1jhasddfaskdfhla'
pip install django python-decouple
python manage.py migrate
python manage.py runserver
```

확인해주셔서 감사합니다. :)
