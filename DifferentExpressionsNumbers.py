from flask import Flask

app = Flask(__name__)

template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Flask Test</title>
  </head>

  <body>
    <h1> Claculator Analog </h1>
    <h2> For Devision --> /divide/10/2 </h2>
    <h2> For Devision --> /divide/10/2 </h2>
    <h2> For Devision --> /divide/10/2 </h2>
    <h2> For Devision --> /divide/10/2 </h2>
    {content}
  </body>
</html>
""".strip()


@app.route('/')
def defScreen():
   return ()


@app.route('/divide/<int:number_1>/<int:number_2>')
def divide(number_1, number_2):
    if number_2 == 0:
      return template.replace("{content}", "Error: division by zero")
    result = number_1 / number_2
    return template.replace("{content}", f"Here is your quotient: {result}")

# @app.route('/multiplication/<int:number_1>/<int:number_2>')
# def multiplication(number_1, number_2):
#     result = number_1 * number_2
#     return template.replace("{content}", f"Here is your quotient: {result}")

