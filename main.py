from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("instructor_page.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        result = request.form
        print(result)
    return render_template('addForm.html')


if __name__ == '__main__':
    app.run(debug=True)
