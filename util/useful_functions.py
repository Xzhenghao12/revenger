import inspect

def get_and_run_classes(module):
    # 1. 获取模块中的所有成员
    # inspect.isclass 过滤出类
    classes = inspect.getmembers(module, inspect.isclass)
    names = []
    instances = []
    for name, cls in classes:
        # 2. 检查类是否是在该文件中定义的（排除导入的类）
        if cls.__module__ == module.__name__:
            # 3. 实例化类并调用方法
            instances.append(cls())
            names.append(name)

    return names, instances