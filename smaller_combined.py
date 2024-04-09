from PIL import Image
import json
import os

def resize_image(image_path, output_path, new_width, new_height):
    # 打开图片
    img = Image.open(image_path)
    
    # 确保图片尺寸是整数
    new_width = int(new_width)
    new_height = int(new_height)
    
    # 调整图片大小
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS) # 使用ANTIALIAS提高图片质量
    
    # 保存调整尺寸后的图片
    img.save(output_path)
    
    print(f"图片已成功缩小到 {new_width}x{new_height} 并保存为 {output_path}")

# 使用示例
    
# 获取原始图片路径
read_filename = 'combined_files.json'
read_file_path = os.path.join(read_filename)
# 读取文件，并将JSON字符串转换回Python列表
with open(read_file_path, 'r', encoding='utf-8') as f:
    file_names = json.load(f)

for original_image_path in file_names:
# original_image_path = 'path/to/your/original/image.jpg'  # 原始图片路径
    resized_image_path = original_image_path.replace('.jpg', '_smaller.jpg')
    # resized_image_path = 'path/to/your/resized/image.jpg'  # 调整尺寸后的图片保存路径
    desired_width = 1334  # 期望的宽度
    desired_height = 1002  # 期望的高度
    resize_image(original_image_path, resized_image_path, desired_width, desired_height)
    os.remove(original_image_path)