import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_input = request.form.get("text")
        result = f"Ты ввел: {user_input}"
    return render_template("index.html", result=result)

@app.route('/map')
def map_page():
    return render_template('map.html')

@app.route('/news')
def news_page():
    return render_template('news.html')

@app.route('/route')
def route_page():
    return render_template('route.html')

@app.route('/complaints')
def complaint_page():
    return render_template('complaint.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
