import requests

# url = "https://apis-public.congtrinhviettel.com.vn/llm"
url = "http://10.248.243.99:1114/llm"
data = {
    "InputText": "có bán sản phẩm điều hòa 60 tr không",
    "IdRequest": "15092024",
    "NameBot": "ChatBot",
    "User": "23123",
    "GoodsCode": "",
    "ProvinceCode": "",
    "ObjectSearch": "",
    "PriceSearch": "",
    "DescribeSearch": "",
}

response = requests.post(url, data=data)
print(response.json())
# - Nếu thông tin không có trong dữ liệu xin hãy trả lời: "Hiện tại tôi không có thông tin về sản phẩm này. Anh/chị cho tôi biết cần sản phẩm nào? Có tầm giá bao nhiêu? Tôi sẽ giúp Anh/chị tìm kiếm. Cảm ơn Anh/chị."

# gunicorn -w 4 -k uvicorn.workers.UvicornWorker test:app --threads 2 --worker-connections 100 --host 0.0.0.0 --port 1113
# uvicorn test:app --workers 4 --limit-concurrency 20 --host 0.0.0.0 --port 1113
# uvicorn test:app --workers 4 --limit-concurrency 20 --host 0.0.0.0 --port 1113 --log-level debug