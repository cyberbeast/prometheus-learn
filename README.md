# prometheus-learn
Learning environment for prometheus

## Objectives
- Set up Flask with a "flaky" endpoint.
- Set up "[prometheus_flask_exporter](https://github.com/rycus86/prometheus_flask_exporter)" client to report metrics.
- Set up Prometheus server to collect and monitor metrics from the Flask service.
- Set up Grafana to accept a prometheus compatible data source and visualize different metrics.
- Integrate a simple multi-threaded load-tester to simulate load conditions on the flaky endpoint.

## To-do's
- Define concrete metrics
- Evaluate performance with multi-threaded loads across different endpoints.

## Deploy/Build Instructions
```
$ docker-compose up --build
```
