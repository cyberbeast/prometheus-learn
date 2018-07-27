import random
import time

from flask import Flask, request, abort
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application Info', version='0.1')


@app.route('/')
def hello_world():
    return 'Hello, World!' # Requests tracked by default

@app.route('/flaky')
def long_running():
    time.sleep(random.uniform(0,1))
    return 'done'

if __name__ == "__main__":
    app.run(host='0.0.0.0')