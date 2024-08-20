import json
import os
from typing import Dict, Any 

USER_STORAGE_DIR = 'logs/user_storage/'
os.makedirs(USER_STORAGE_DIR, exist_ok=True)

def load_user_data(user_id: str) -> dict:
    user_dir = os.path.join(USER_STORAGE_DIR, f'{user_id}')
    file_path = os.path.join(user_dir, 'session.json')
    if os.path.exists(file_path):
        with open(file_path,'r', encoding='utf-8') as file:
            data = json.load(file)
    return  data['save_outtext']

def set_save_outtext(user_id: str, new_value: str) -> None:
    user_dir = os.path.join(USER_STORAGE_DIR, f'{user_id}')
    os.makedirs(user_dir, exist_ok=True)
    file_path = os.path.join(user_dir, 'session.json')
    data = {}
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    data['save_outtext'] = new_value

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    
# Ví dụ sử dụng
user_id = '6456546'

response = "\n 019013000001\n  Thông số sản phẩm: nguồn điện: 220-240v\ncông suất: 9500 btu/h\ncông suất tiêu thụ: 745 w\ncường độ dòng điện: 3.4 a\nerr: 3.54 w/w\ninverter : có\nkích thước máy trong ( dxrxc): 726x210x291 (mm)\nkhối lượng thực máy trong/ khối lượng đóng gói: 8.2/10.3 kg\nkích thước máy ngoài (dxrxc): 835x300x540 (mm)\nkhối lương thực máy ngoài / khối lượng đóng gói: 21.7/23.2 kg\nloại gas/ khối lượng nạp: r32/0.38\nap suất thiết kế: 4.3/1.7 mpa\nchiều dài đường ống tối đa: 25m\nchênh lệch độ cao tối đa: 10m\nphạm vi lành lạnh hiệu quả : 12~18 m2\nhiệu suất năng lượng : 4.48 cspf\nbảo hành 3 năm cho sản phẩm\nbảo hành 5 năm cho máy nén\nsuất xứ : thái lan\n - Giá tiền: 6,014,184 đ*\n\n2. *quạt điều hòa không khí everest 6000d - Mã: M&EGD000154\n  Thông số sản phẩm: • điện áp: 220v - 50hz\n• kích thước: (dài) 440 x (rộng) 340 x (cao) 970 mm\n• lưu lượng gió: 6000m3/h\n• dung tích khay chứa nước: 45l\n• công suất: 80w\n• điều khiển từ xa: có\n• cảm biến chất lượng không khí: có\n• chức năng tạo ion: có\n• tốc độ gió: 3 tốc độ\n• hướng gió: 4 chiều trái phải, lên xuống\n - Giá tiền: 2,427,000 đ*\n\n3. *điều hòa mdv 1 chiều 12000 btu - model 2023 - Mã: 019013000004\n  Thông số sản phẩm: model: mdvg-13crdn8\ncông suất: 12.000 btu/h\nloại: 1 chiều inverter\ndiện tích sử dụng: 15 - 20m²\ngas: r32\nmức tiêu thụ điện: 1.15 kw/h\nđộ ồn: 22/19 db(a)\nkích thước dàn lạnh: 810 x 285 x 210 mm\nkích thước dàn nóng: 770 x 285 x 540 mm\ntrọng lượng dàn lạnh: 14 kg\ntrọng lượng dàn nóng: 25 kg\n - Giá tiền: 7,246,030 đ*\n\n4. *điều hòa mdv 1 chiều inverter 18000 btu - model 2023 - Mã: 019013000003\n  Thông số sản phẩm: model: mdvg-18crdn8\ncông suất: 18.000 btu/h\nloại: 1 chiều inverter\ndiện tích sử dụng: 20 - 30m²\ngas: r32\nmức tiêu thụ điện: 1.65 kw/h\nđộ ồn: 22/19 db(a)\nkích thước dàn lạnh: 969 x 320 x 241 mm\nkích thước dàn nóng: 770 x 285 x 540 mm\ntrọng lượng dàn lạnh: 18 kg\ntrọng lượng dàn nóng: 28 kg\n - Giá tiền: 11,740,520 đ*\n"
set_save_outtext(user_id, response)
print(load_user_data(user_id))
# with open(,'r', encoding='utf-8') as file:
#     data = json.loat(file)
