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
metrics.info('app_info', 'Application Info', version='1.0.3')


@app.route('/')
def hello_world():
    return 'Hello, World!' # Requests tracked by default

@app.route('/skip')
@metrics.do_not_track()
def skip():
    return 'ok'

@app.route('/<item_type>')
@metrics.do_not_track()
@metrics.counter('invocation_by_type', 'Number of invocations by type', labels={'item_type': lambda: request.view_args['type']})
def by_type(item_type):
    return 'ok'

@app.route('/long-running')
@metrics.gauge('in_progress', 'Long running requests in progress')
def long_running():
    return 'ok'

@app.route('/status/<int:status>')
@metrics.do_not_track()
@metrics.summary('requests_by_status', 'Request latencies by status', labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path', labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def echo_status(status):
    return 'Status: %s' % status, status


# @app.route('/metrics/')
# @IN_PROGRESS.track_inprogress()
# @TIMINGS.time()
# def metrics():
#     REQUESTS.labels(method='GET', endpoint="/metrics", status_code=200).inc()
#     return generate_latest(REGISTRY)


if __name__ == "__main__":
    app.run(host='0.0.0.0')