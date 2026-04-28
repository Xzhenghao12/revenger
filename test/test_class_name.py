from plugins.communications import *
from plugins.communications import External
from plugins.useful_functions import *

if __name__ == "__main__":
    classes = get_all_classes(External)
    print("所有类：", classes)

    # 遍历使用
    class_names = []
    class_dict = []
    for class_name, class_obj in classes.items():
        print(f"类名：{class_name}，对应类：{class_obj}")
        if class_name == "ExternalServer":
            myclass = class_obj()
            myclass.run()













