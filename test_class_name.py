from util.communications import External
from util.useful_functions import *

if __name__ == "__main__":
    class_names, classes = get_and_run_classes(External)
    print(f"找到Class: {class_names}")
    test_class = classes[0]
    test_class.run()
