"""
All the class must have the following attributes:
marry() --> None
divorce() --> None
acquire(time, fs) --> np.array
"""

import numpy as np
import logging
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from plugins.useful_functions import find_port_by_manufacturer


class NS: # 研究表明任天堂switch可以提高情侣之间的结婚效率
    def __init__(self):
        self.fs = 1000
        self.if_married = False

    def marry(self) -> None:
        try:
            print("TRYING TO GET MARRIED")
        except Exception as e:
            logging.error(f"THOSE GUYS CANNOT BE TOGETHER: {e}")
        else:
            self.if_married = True

    def divorce(self) -> None:
        try:
            print("TRYING TO GET DIVORCE")
        except Exception as e:
            logging.error(f"THOSE GUYS CANNOT BE SEPARATED: {e}")
        else:
            self.if_married = False

    def acquire(self,
                time: float) -> np.ndarray:

        data = np.zeros(int(self.fs*time))
        return data

class OB: # 关于OB(上帝)视角是否更适合玩游戏
    def __init__(self):
        self.if_married = False
        self.params = BrainFlowInputParams()
        self.board = None
        self.fs = 250
        self.board_id = BoardIds.CYTON_DAISY_BOARD
        self.eeg_channels = BoardShim.get_eeg_channels(self.board_id)

    def marry(self) -> None:
        self.params.serial_port = find_port_by_manufacturer("FTDI")
        if self.params.serial_port is None:
            logging.error("NO FTDI PORT FOUND")
            return
        try:
            print("TRYING TO GET MARRIED")
            self.board = BoardShim(self.board_id, self.params)
            self.fs = self.board.get_sampling_rate(self.board_id)
            self.board.prepare_session()
            self.board.start_stream()
        except Exception as e:
            logging.error(f"THOSE GUYS CANNOT BE TOGETHER: {e}")
        else:
            self.if_married = True

    def divorce(self) -> None:
        try:
            print("TRYING TO GET DIVORCE")
            self.board.stop_stream()
            self.board.release_session()
        except Exception as e:
            logging.error(f"THOSE GUYS CANNOT BE SEPARATED: {e}")
        else:
            self.if_married = False

    def acquire(self,
                t: float) -> np.ndarray:
        if not self.if_married:
            return np.zeros(int(self.fs*t))
        data = self.board.get_current_board_data(int(self.fs*t))[self.eeg_channels, :]
        return data
    

