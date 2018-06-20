'''
定义一个学生类，用来形容学生
'''
# 定义一个空类
class Student():
   # 一个空类，pass代表直接跳过
   # pass 必须有
    pass
# 定义一个对象
mingyue = Student()

# 定义一个类，用来描述听python的学生

class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"
    # 注意def doHomework的缩进层级，和变量同级
    # 系统默认有一个self参数
    def DoHomework(self):
        print("在做作业")

        #在函数末尾使用return语句
        return None
# 实例化
yue = PythonStudent()
print(yue.name)
print(yue.age)
# 注意成员函数的调用没有传递进入参数
yue.DoHomework()
