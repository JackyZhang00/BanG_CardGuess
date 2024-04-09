# 图片3*3拼接

from PIL import Image
import json
import os

read_filename = 'files.json'
read_file_path = os.path.join(read_filename)

# N = 4

with open(read_file_path, 'r', encoding='utf-8') as f:
    file_names = json.load(f)

# 图片路径列表，假设你已经有了9张图片
for i in range(0,len(file_names)):
    image_paths = file_names[50*i:50*i+50]

# 加载图片并计算每张图片的大小
    images = [Image.open(x) for x in image_paths]
    width, height = images[0].size

    # 计算拼接后图片的大小
    total_width = width * 10
    total_height = height * 5

    # 创建一个新的空白图片，用于存放拼接后的结果
    combined_image = Image.new('RGB', (total_width, total_height))

    # 拼接图片
    x_offset = 0
    y_offset = 0
    for img in images:
        combined_image.paste(img, (x_offset, y_offset))
        x_offset += width
        if x_offset >= total_width:
            x_offset = 0
            y_offset += height

    # 保存拼接后的图片
    dir = 'combined_fifty'
    file_name = 'combined_image_' + str(i) + '.jpg'
    combined_image.save(os.path.join(dir, file_name))

    # 打印完成信息
    print("图片拼接完成，已保存为 'combined_image_ "+ str(i) + "'.jpg'")