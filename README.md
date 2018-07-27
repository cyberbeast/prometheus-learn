# prometheus-learn
Learning environment for prometheus

## Objectives
- Set up Flask with a "flaky" endpoint.
- Set up "prometheus-flask-exporter" client to report metrics.
- Set up Prometheus server to collect and monitor metrics from the Flask service.
- Set up Graphana to accept a prometheus compatible data source and visualize different metrics.
- Integrate a simple load-tester to simulate load conditions on the flaky endpoint.

## To-do's
- Define concrete metrics

## Deploy/Build Instructions
```
$ docker-compose up --build
```
