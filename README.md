# Parkito's todo list README

#### Last modified: 2019-05-18
#### 지원분야: 웹/서버

<br>

## 로컬에서 테스트하기

운영체제는 리눅스를 기준으로 하고, 파이썬을 위한 가상환경 구성이 가능하다고 가정합니다. 저는 `pipenv`를 사용하고 있습니다.  

밑의 로컬 테스트 파일에서 `pipenv`이 들어간 코드는 사용하시는 가상환경 구성방법에 따라 변형하시면 됩니다.



```sh
git clone https://github.com/shoark7/todo-project.git
cd todo-project
export SECRET_KEY='1231u24jkasdkfajskfh;k1jhasddfaskdfhla'
pipenv install django python-decouple
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```


