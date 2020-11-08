from flask import Flask, render_template
from flask import request


app = Flask(__name__)

@app.route('/mypage/me', methods=['GET'])
def me():
    return render_template("me.html")

@app.route('/mypage/contact', methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route('/mypage/contact', methods=['POST'])
def post_message():
    message = request.form['message']
    print(message)
    return render_template("contact.html", message=message)

if __name__ == "__main__":
    app.run(debug = True, port=8001)
