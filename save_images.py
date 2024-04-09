import os
import json

# 读取所有图片
directory = 'bestdori_images'

# 创建一个空列表，用于存储文件名
file_names = []

# 遍历指定目录中的所有文件和文件夹
for item in os.listdir(directory):
    # 构造完整的路径
    full_path = os.path.join(directory, item)
    
    # 检查该路径是否为文件
    if os.path.isfile(full_path):
        # 将文件名添加到列表中
        file_names.append('bestdori_images/'+item)

directory = 'bestdori_after_training_images'
for item in os.listdir(directory):
    # 构造完整的路径
    full_path = os.path.join(directory, item)
    
    # 检查该路径是否为文件
    if os.path.isfile(full_path):
        # 将文件名添加到列表中
        file_names.append('bestdori_after_training_images/'+item)

# 设置保存文件的目录和文件名
# save_directory = 'config'
save_filename = 'files.json'

# 构造完整的保存文件路径
save_file_path = os.path.join(save_filename)

# 将file_names列表转换为JSON格式的字符串，并保存到文件
with open(save_file_path, 'w', encoding='utf-8') as f:
    json.dump(file_names, f)
