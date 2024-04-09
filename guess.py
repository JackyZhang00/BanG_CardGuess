import cv2
import os
from PIL import Image
from IPython.display import display
import json
import re
import time

# 输入文件

image_file = r'test.png'

start_time = time.time()

read_filename = 'combined_files.json'
full_read_filename = 'files.json'
read_file_path = os.path.join(read_filename)

with open(read_file_path, 'r', encoding='utf-8') as f:
    file_names = json.load(f)

# 读取局部图片和目标图片集合
template_image = cv2.imread(image_file, 1)
new_height, new_width,channel = template_image.shape
# print(new_width,new_height)
# template_image = cv2.resize(template_image, (new_width, new_height),interpolation=cv2.INTER_AREA)
smaller_template_image = cv2.resize(template_image, (int(new_width/10), int(new_height/5)),interpolation=cv2.INTER_AREA)
target_images = file_names

# 保存记录
val = []
loc = []

# 遍历目标图片集合
for target_image_path in target_images:
    # 读取目标图片
    target_image = cv2.imread(target_image_path, 1)
    
    # 模板匹配
    res = cv2.matchTemplate(target_image, smaller_template_image, cv2.TM_CCOEFF_NORMED)
    
    # 找到匹配结果中的最大值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(target_image_path+' '+str(max_val))
    val.append(max_val)
    loc.append(max_loc)

    index = val.index(max(val))
    if max_val > 0.9:
        number = re.search(r'\d+', target_image_path).group(0)
        # match = re.search(r'\d+', target_image_path)
        # number = match.group(0)
        break
else:
    index = val.index(max(val))
    target_image_path = target_images[index]
    match = re.search(r'\d+', target_image_path)
    number = match.group(0)

val,loc = [],[]
# 进一步从图片中筛选图片
template_image = cv2.imread(image_file, 0)

read_file_path = os.path.join(full_read_filename)
with open(read_file_path, 'r', encoding='utf-8') as f:
    file_names = json.load(f)
target_images = file_names[50*int(number):50*int(number)+50]

for target_image_path in target_images:
    # 读取目标图片
    target_image = cv2.imread(target_image_path, 0)
    
    # 模板匹配
    res = cv2.matchTemplate(target_image, template_image, cv2.TM_CCOEFF_NORMED)
    
    # 找到匹配结果中的最大值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(target_image_path+' '+str(max_val))
    val.append(max_val)
    loc.append(max_loc)

    if max_val > 0.95:
        break

index = val.index(max(val))
print(f"找到匹配的图片：{target_images[index]}")
target_image = cv2.imread(target_images[index], 1)
cv2.rectangle(target_image, loc[index], (loc[index][0] + template_image.shape[1], loc[index][1] + template_image.shape[0]), (0, 255, 0), 2)

match = re.search(r'(\d{2})', target_images[index])

# 如果匹配成功，提取数字
if match:
    character = match.group(0)
    # print(f"提取的前两个数字是: {character}, 角色是 {character_sheet[character]}")
# else:
#     print("未在文件名中找到数字。")

# pyperclip.copy('@花音Kanon /cck ' + character_sheet[character])
# pyperclip.copy(character_sheet[character])
end_time = time.time()

# 显示用
template_image = cv2.imread(image_file, 1)

cv2.imshow('Matched Image', target_image)
cv2.imshow('template_image',template_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"耗时：{end_time-start_time} s")


