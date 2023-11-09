from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

view_metric = Counter('view', 'Home view')

@app.route("/")
def hello_world():
    view_metric.inc()
    return "<h1>Hellow world form python</h1>"

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(debug=True)
