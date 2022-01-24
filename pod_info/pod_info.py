import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge, start_http_server
import time
import psutil
import socket
from http.server import BaseHTTPRequestHandler


class CustomCollector(BaseHTTPRequestHandler):
    def collect(self):
        host = socket.gethostname()
        ram_metrics = Gauge("memory_usage_bytes", "Memory usage in bytes.",
                            {'host': host})
        cpu_metrics = Gauge("cpu_usage", "CPU usage details",
                            {'host': host})

        while True:
            time.sleep(15)
            # Add ram metrics
            ram = psutil.virtual_memory()
            swap = psutil.swap_memory()
            ram_metrics.labels('ram_used').set(ram.used)
            print(ram.used)
            ram_metrics.labels('ram_cached').set(ram.cached)
            ram_metrics.labels('swap_memory_used').set(swap.used)
            for c, p in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
                cpu_metrics.labels('cores').set(c)
                cpu_metrics.labels('percentage_use').set(p)

if __name__=="__main__":
    start_http_server(6060)
    x = CustomCollector
    x.collect(self=x)
