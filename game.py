import random

# 石头剪子布游戏,石头:0,剪子:1,布:2
print("石头剪子布游戏,石头:0,剪子:1,布:2")
while True:
    pc = random.randint(0, 2)
    num = int(input("请输入数字:"))
    if num == pc:
        print("平局")
    elif (pc == 0 and num == 1) or (pc == 1 and num == 2) or (pc == 2 and num == 0):
        print("电脑获胜")
    elif (pc == 0 and num == 2) or (pc == 1 and num == 0) or (pc == 2 and num == 1):
        print("玩家获胜")
    if 2 < num or num < 0:
        print("输入错误")
    back = input("是否继续玩:(q键退出,任意见继续)")
    if back == "q":
        break
