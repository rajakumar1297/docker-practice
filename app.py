from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return """<hhml> <body>
    <form action="/grret" method="post">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    
    </body> </hhml>"""


@app.route('/grret', methods=['POST'])
def grret():
    name = request.form.get('name')
    return f'Hello, {name}'

if __name__ == '__main__':
    app.run(debug=True)