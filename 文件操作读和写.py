"""
上传图片，要求:
图片要以.jpg或.gif或.png格式结尾
图片名称不超过6位
如果后缀正确,名称超过6位,则自动生成随机6位数字
"""
import random
import time
total_pic_name = []
print("---------欢迎进入图片上传系统---------")
while True:
    picture_name = input("请输入图片名称:")
    if (picture_name.endswith(".jpg") or picture_name.endswith(".gif") or picture_name.endswith(".png")) and 4 < len(picture_name) <= 10:
        print("图片上传成功,正在保存中")
        time.sleep(2)
        total_pic_name.append(picture_name)
        print("保存成功")
    elif len(picture_name) > 10 and (picture_name.endswith(".jpg") or picture_name.endswith(".gif") or picture_name.endswith(".png")):
        picture_name = str(random.randint(0,999999)) + ".jpg"
        total_pic_name.append(picture_name)
        print("图片名称过长,正在随机生成名称")
        print("图片正在保存")
        time.sleep(2)
        print("保存成功")
    else:
        print("上传格式错误,上传失败")
    answer = input("是否继续上传(q表示退出)")
    if answer == "q":
        break
print(f"你上传的图片有:{total_pic_name}")
