from flask import request
import time
import sys

def start_timer():
    sys.stderr.write("|-----Starting timer-----|\n")
    request.start_time = time.time()
    sys.stderr.write("|------------------------|\n")

def stop_timer(response):
    sys.stderr.write("|-----Stopping timer-----|\n")
    resp_time = time.time() - request.start_time
    sys.stderr.write("Response Time: %ss\n" % resp_time)
    sys.stderr.write("|------------------------|\n")
    return response

def record_request_data(response):
    sys.stderr.write("|-----Recording Request Data-----|\n")
    sys.stderr.write("REQ Path: %s \nREQ Method: %s \nRES Status: %s \n" % (request.path, request.method, response.status_code))
    sys.stderr.write("|------------------------|\n")
    return response

def setup_metrics(app):
    app.before_request(start_timer)
    app.after_request(record_request_data)
    app.after_request(stop_timer)