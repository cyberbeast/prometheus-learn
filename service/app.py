import random
import time

from flask import Flask, request, abort
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# # A counter to count the total number of HTTP requests
# REQUESTS = Counter('http_requests_total', 'Total HTTP Requests (count)', ['method', 'endpoint', 'status_code'])

# # A gauge (i.e. goes up and down) to monitor the total number of in progress requests
# IN_PROGRESS = Gauge('http_requests_inprogress', 'Number of in progress HTTP requests')

# # A histogram to measure the latency of the HTTP requests
# TIMINGS = Histogram('http_request_duration_seconds', 'HTTP request latency (seconds)')

# Static information as metric.
metrics.info('app_info', 'Application Info', version='0.1')


@app.route('/')
def hello_world():
    return 'Hello, World!' # Requests tracked by default

@app.route('/flaky')
def long_running():
    time.sleep(random.uniform(0,3))
    return 'done'

if __name__ == "__main__":
    app.run(host='0.0.0.0')