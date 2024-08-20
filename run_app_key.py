from multiprocessing import Process
from app_key import run_app, create_app
from config_app.config import get_config
from utils.llm_manager import get_llm1, get_llm2, get_llm3

config_app = get_config()
ports = config_app['server']['port_key']
processes = []

# Tạo các ứng dụng với các LLM tương ứng
llms = [create_app(llm) for llm in [get_llm1()]]

for llm, port in zip(llms, ports):
    p = Process(target=run_app, args=(llm, port))
    print("apps", llm)
    p.start()
    processes.append(p)

for p in processes:
    p.join()
