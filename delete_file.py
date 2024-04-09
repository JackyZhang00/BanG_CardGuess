import os

# 设置你想要检查的目录
directories = ('bestdori_images','bestdori_after_training_images')
# directory = 'bestdori_after_training_images'

# 以字节为单位设置文件大小的阈值
size_threshold = 100 * 1024  # 100kB

# 遍历指定目录
for directory in directories:
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