from flask import Flask, render_template, jsonify

app = Flask(__name__)
jobs = [{
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Birr. 10,000,000"
}, {
    "id": 2,
    "title": "Hacker",
    "location": "Addis Ababa, Ethiopia",
    "salary": "Birr. 10,000"
}, {
    "id": 3,
    "title": "Office Adminstrator",
    "location": "Adama",
}]


@app.route("/")
def index():
    return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def json_provider():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
