from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('hide.html')

if __name__=="__main__":
    app.run(debug=True)
