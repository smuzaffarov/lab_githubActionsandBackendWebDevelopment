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
    <h1> Calculator Analog </h1>
    <nav>
      <a href="/">Home</a>
      <a href="/divide/10/2">Divide</a>
      <a href="/multiplication/10/10">Multiplication</a>
      <a href="/sqrt/4">Square Root</a>
    </nav>
    <h2> For Division --> /divide/10/2 </h2>
    <h2> For Multiplication --> /multiplication/10/2 </h2>
    <h2> For Square Root --> /sqrt/4 </h2>
    {content}
  </body>
</html>
""".strip()

# / home page
@app.route('/')
def defScreen():
    return template.replace("{content}", "Welcome to the Calculator!")

# / devide
@app.route('/divide/<int:number_1>/<int:number_2>')
def divide(number_1, number_2):
    if number_2 == 0:
      return template.replace("{content}", "Error: division by zero")
    result = number_1 / number_2
    return template.replace("{content}", f"Here is your answer: {result}")

# / multiplication
@app.route('/multiplication/<int:number_1>/<int:number_2>')
def multiplication(number_1, number_2):
    result = number_1 * number_2
    return template.replace("{content}", f"Here is your answer: {result}")

# . sqrt
@app.route('/sqrt/<int:number_1>')
def sqrt(number_1):
    if number_1 < 0:
        return template.replace("{content}", "Error: negative number")
    result = number_1 ** 0.5
    return template.replace("{content}", f"Here is your answer: {result}")


if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
