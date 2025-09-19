from flask import Flask

app = Flask(__name__)

template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Intro to Flask</title>
    <link rel="icon" href="/favicon.ico" type="image/png">
  </head>

  <body>
    <h1> Lab 03 <h2>
    {content}
  </body>
</html>
""".strip()


@app.route('/add/<int:number_1>/<int:number_2>')
def showintegers(number_1, number_2):
    sum = number_1 + number_2
    return template.replace("{content}", f"Here is you sum: {sum}")