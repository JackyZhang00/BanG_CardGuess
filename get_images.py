import requests
import os
import json

# 读取已有文件列表

filename = 'files.json'
read_file_path = os.path.join(filename)

with open(read_file_path, 'r', encoding='utf-8') as f:
    file_names = json.load(f)

# 目标网站的URL模板
url_template = 'https://bestdori.com/assets/jp/characters/resourceset/res0{chara_id}{resource_set_id}_rip/card_normal.png'

# 用于保存图片的目录
save_dir = 'bestdori_images'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 假设我们有一个包含资源集ID的列表
chara_ids = [str(i).zfill(2) for i in range(1,41)]
resource_set_ids = [str(i).zfill(3) for i in range(1,100)]  # ID

# 遍历资源集ID列表，下载并保存图片
for chara_id in chara_ids:
    for resource_set_id in resource_set_ids:
        filename = f'{save_dir}/{chara_id}{resource_set_id}_card_normal.png'
        # filename = os.path.join(save_dir, f'{chara_id}{resource_set_id}_card_normal.png')

        if filename in file_names:
            print(f'{filename} 已存在')
            continue

        # 构造完整的图片URL
        img_url = url_template.format(chara_id=chara_id,resource_set_id=resource_set_id)
        
        # 发送HTTP请求获取图片内容
        img_data = requests.get(img_url).content

        # 保存图片到本地
        with open(filename, 'wb') as f:
            f.write(img_data)
            print(f'图片已保存: {filename}')

directory = 'bestdori_images'

# 以字节为单位设置文件大小的阈值
size_threshold = 100 * 1024  # 100kB

# 遍历指定目录
for filename in os.listdir(directory):
    # 构造完整的文件路径
    file_path = os.path.join(directory, filename)
    
    # 检查文件是否存在并且是文件类型
    if os.path.isfile(file_path):
        # 获取文件大小
        file_size = os.path.getsize(file_path)
        
        # 如果文件大小小于阈值，则删除该文件
        if file_size < size_threshold:
            os.remove(file_path)
            print(f'已删除文件：{filename}，大小：{file_size}字节')