# 提取已有文件列表
import os
import requests
import json

# 设置你想要提取文件名的目录
directory = 'bestdori_images'

# 创建一个空列表，用于存储提取的文件名前5个字符
file_prefixes = []

# 遍历指定目录中的所有文件
for filename in os.listdir(directory):
    # 构造完整的文件路径
    file_path = os.path.join(directory, filename)
    
    # 检查文件是否存在并且是文件类型
    if os.path.isfile(file_path):
        # 获取文件名前5个字符
        file_prefix = filename[:5]
        
        # 将提取的文件名前5个字符添加到列表中
        file_prefixes.append(file_prefix)

# 打印结果列表
# print(file_prefixes)
        
# 读取已有文件列表

filename = 'files.json'
read_file_path = os.path.join(filename)

with open(read_file_path, 'r', encoding='utf-8') as f:
    file_names = json.load(f)
        
# 目标网站的URL模板
url_template = 'https://bestdori.com/assets/jp/characters/resourceset/res0{resource_set_id}_rip/card_after_training.png'

# 用于保存图片的目录
save_dir = 'bestdori_after_training_images'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 假设我们有一个包含资源集ID的列表
# chara_ids = [str(i).zfill(2) for i in range(36,41)]
resource_set_ids = file_prefixes  # 示例ID

# 遍历资源集ID列表，下载并保存图片
for resource_set_id in resource_set_ids:

    filename = f'{save_dir}/{resource_set_id}_card_after_training.png'

    if filename in file_names:
        print(f'{filename} 已存在')
        continue
    # 构造完整的图片URL
    img_url = url_template.format(resource_set_id=resource_set_id)
    
    # 发送HTTP请求获取图片内容
    img_data = requests.get(img_url).content
    
    # 获取图片的文件名（基于资源集ID）
    
    
    # 保存图片到本地
    with open(filename, 'wb') as f:
        f.write(img_data)
        print(f'图片已保存: {filename}')