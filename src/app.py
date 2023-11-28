from flask import Flask
from prometheus_client import Counter, generate_latest
from flask_healthz import healthz, HealthError

app = Flask(__name__)
app.register_blueprint(healthz, url_prefix="/healthz")

view_metric = Counter('view', 'Home view')

def liveness():
    try:
        print("OK")
    except Exception:
        raise HealthError("Liveness probe fail")

def readiness():
    try:
        print("OK")
    except Exception:
        raise HealthError("Readiness probe fail")

app.config.update(
    HEALTHZ = {
        "live": "app.liveness",
        "ready": "app.readiness",
    }
)

@app.route("/")
def hello_world():
    view_metric.inc()
    return "<h1>Hellow world form python</h1>"

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(debug=True)
