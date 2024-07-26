from flask import Flask

app = Flask(__name__)

@app.route('/')
def aboutflask():
    return f"""
<!DOCTYPE html>
<html>
   <head>
      <title>Flask</title>
   </head>
   <body>
      <h1>Flask</h1>
      <ol>
         <li>파일 하나로 구성된 짧은 코드로도 잘 동작하는 웹 프로그램을 만들 수 있습니다.</li>
         <li>Flask는 최소한의 기능들을 가지고 있기 때문에 개발자가 필요한 확장 모듈을 추가하며 개발할 수 있어 확장성이 높습니다.</li>
         <li>최소한의 규칙만이 존재하는 프레임워크이기 때문에 개발의 자유도가 다른 프레임워크보다 높습니다.</li>
         <li>Jinja2 문법을 이용하여 웹페이지에서 동적으로 반응해야 할 부분을 JS가 아닌 Python 코드와 유사한 방식으로 작성하여 구현할 수 있습니다.</li>
      </ol>
      <ul>
         <li>Flask</li>
         <img src="AZUREFlask.jpg" alt="flask" width="700" height="600">
      </ul>
   </body>
</html>
    """

if __name__ == '__main__':
    app.run()
