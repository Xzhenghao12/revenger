import inspect

def get_all_classes(module):
    """
    获取模块中所有自定义类
    返回：字典 {类名: 类对象}
    """
    class_dict = {}

    # 遍历模块成员，筛选出 class 类型
    for name, obj in inspect.getmembers(module, inspect.isclass):
        # 只保留当前模块定义的类（排除导入进来的类）
        if obj.__module__ == module.__name__:
            class_dict[name] = obj

    return class_dict