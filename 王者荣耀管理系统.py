"""
王者荣耀角色管理系统
角色:名字,性别,职业
增加
删除
修改
查找
"""
import time
role = []
box = []
print("------------欢迎使用王者荣耀角色管理系统-------------")
while True:
    mode = input("请选择模式选项\n1,增加。\n2,删除。\n3,修改。\n4,查找\n5,查看所有英雄\n6,退出系统\n")
    if mode == "1":                                        #增加某个英雄
        role_name = input("\t请输入要添加的角色姓名:")
        role_sex = input("\t请输入性别:\t男或女\t")
        if role_sex == "男":
            print("\t该角色性别为男性")
        elif role_sex == "女":
            print("\t该角色性别为女性")
        else:
            print("未知性别,输入错误")
        role_profession = input("\t请输入该英雄职业\t")
        role = [role_name,role_sex,role_profession]
        box.append(role)
        role = [role_name,role_sex,role_profession]
        print(f"成功添加{role_name}到王者荣耀系统")
    elif mode == "2":                                      #删除一个英雄
        cut_name = input("请输入你要删除的英雄:")
        for role in box:
            if cut_name in role:
                print(f"正在删除{cut_name}英雄")
                box.remove(role)
                time.sleep(1)
                print("删除成功")
            else:
                print("未找到该英雄或该英雄不存在")
    elif mode == "3":                                      #修改一个英雄属性
        alter_role = input("请输入要修改的英雄名称:")
        for role in box:
            if alter_role in role:
                role_property = input("请输入你要修改的属性:\t名称\t性别\t职业")
                if role_property == "名称":
                    name = input("\t请输入你想要的名称")
                    role.insert(0,name)
                    role.pop(1)
                elif role_property == "性别":
                    sex = input("\t请输入你想要修改的性别为:")
                    if sex == role[1]:
                        print("\n你修改个毛啊,还是这个")
                    else:
                        role.insert(1,sex)
                        role.pop(2)
                elif role_property == "职业":
                    profession = input("\t请输入想要修改成的职业:")
                    print("正在修改,请稍后")
                    role.insert(2,profession)
                    role.pop(3)
                    print("修改成功")
                else:
                    print("未知属性")
            else:
                print("不存在该角色")
    elif mode == "4":                                      #查找一个英雄
        lookup_role = input("\n请输入要查找的英雄:")
        for role in box:
            if lookup_role in role:
                print(role)
            else:
                print("\t该英雄不存在")
    elif mode == "5":                                      #查找所有英雄
        print("正在打开列表")
        print("请查看")
        print(box)
    elif mode == "6":                                      #退出整个系统
        print("正在退出")
        time.sleep(2)
        print("退出成功")
        break
    else:                                                 #输入模式错误
        print("模式输入错误,重新选择")
