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
## Port Mapping Reference
- 5000 -> Flask service
- 9090 -> Prometheus
- 3000 -> Grafana

## Architecture
![Architecture](https://raw.githubusercontent.com/cyberbeast/prometheus-learn/c4dde84344a64e90c8091f79d3d7c400119a0b00/image.png)
