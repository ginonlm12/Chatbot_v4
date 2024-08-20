from multiprocessing import Process
from app import run_app
from config_app.config import get_config

config_app = get_config()
ports = config_app['server']['ports']
process = []

for port in ports:
    p = Process(target=run_app, args=(port,))
    p.start()
    process.append(p)

for p in process:
    p.join()