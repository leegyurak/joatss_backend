 
<h1 align="center">
  <br>
  <a href="https://joatss.devgyurak.com/"><img src="https://joatss.devgyurak.com/static/media/%EC%A2%8B%EC%95%98%EC%93%B0-%EB%B0%88.2cc9bf1cf644a30b163f.png" alt="좋았쓰! 변환기" width="200"></a>
  <br>
  좋았쓰! 변환기 (BE)
  <br>
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql" alt="MySQL">
  <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions" alt="Github Action">
</p>

<p align="center">
  <a href="#주요 기능">주요 기능</a> •
  <a href="#환경 세팅 및 실행">환경 세팅 및 실행</a> •
  <a href="#사용하기">사용하기</a> •
  <a href="#License">License</a>
</p>

![스크린샷](https://github.com/user-attachments/assets/05933c2a-77d5-4d75-81ef-b64484577a88)

## 주요 기능

* 문장 입력
  - 본인이 하고 싶은 말이나 좋아하는 문장을 입력해보세요!
* 결과 출력
  - 당신이 쓴 문장을 좋았쓰! 밈의 문장으로 바꾸어 줍니다.

## 환경 세팅 및 실행
- [Git](https://git-scm.com), [Python](https://www.python.org/downloads/), [MySQL](https://www.mysql.com/), 그리고 [Poetry](https://python-poetry.org/)가 필요해요!

```bash
# Clone this repository
$ git clone https://github.com/leegyurak/joatss_backend

# Go into the repository
$ cd joatss_backend

# Enter vitual environment
$ poetry shell

# Install dependencies
$ poetry install

# Add Environment Variable
$ DJAGNO_SECRET_KEY=${add your secret key}
$ CLAUDE_API_KEY=${add your API key}
$ MYSQL_HOST=${add your MySQL host}
$ MYSQL_PORT=${add your MySQL port}
$ MYSQL_USER=${add your MySQL user}
$ MYSQL_PASSWORD=${add your MySQL password}
$ MYSQL_DATABASE=${add your MySQL database}

# Run migrate
$ python manage.py migrate

# Run server
$ python manage.py runserver
```

> 도커 파일을 빌드해도 실행 가능합니다!

## 사용하기

- [좋았쓰! 변환기 접속](https://joatss.devgyurak.com) 

## License

MIT

---

[issues-badge]: https://img.shields.io/github/issues/mkosir/react-parallax-tilt
[issues-url]: https://github.com/leegyurak/joatss_backend/issues
