import uvicorn
from fastapi import FastAPI, File, UploadFile, Form
from config_app.config import get_config
from main_run import handle_request
import datetime
from chat import predict_rasa_llm
from concurrent.futures import ThreadPoolExecutor
import asyncio

config_app = get_config()
max_workers = config_app['server'].get('max_workers', None)  # Lấy từ config hoặc để mặc định
executor = ThreadPoolExecutor(max_workers=max_workers)
numberrequest = 0

app = FastAPI()
@app.post('/key_llm')
async def post(
    InputText: str = Form(None),
    IdRequest: str = Form(...),
    NameBot: str = Form(...),
    User: str = Form(...)
):  
    numberrequest +=1
    loop = asyncio.get_event_loop()
    results = await loop.run_in_executor(
            executor,
            predict_rasa_llm,
            InputText,
            IdRequest,
            NameBot,
            User,
            # llm
        )
    return results
    # print('numberrequest',  numberrequest)
    # return app

# def create_app(llm):

def run_app(port):
    uvicorn.run(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    # print(' numberrequest',  numberrequest)/
    pass
