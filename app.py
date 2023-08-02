import psutil
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    if cpu_metric > 80 or mem_metric > 80:
        return f"Current CPU usage : {cpu_metric} and Memory usage : {mem_metric}"

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')