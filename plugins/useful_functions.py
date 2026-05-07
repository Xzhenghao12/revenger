import inspect
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
import serial.tools.list_ports

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

def find_port_by_manufacturer(target_manufacturer):
    """
    根据制造商名称查找对应的 COM 端口
    :param target_manufacturer: 目标制造商名（如 "FTDI", "Silicon Labs"）
    :return: 匹配到的端口号（如 "COM3"），未找到则返回 None
    """
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # manufacturer 有可能为 None，需要先判断
        if port.manufacturer and target_manufacturer in port.manufacturer:
            return port.device
    return None