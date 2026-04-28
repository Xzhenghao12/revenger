"""
All the class must have the following attributes:
marry() --> None
divorce() --> None
acquire(time, fs) --> np.array
"""

import numpy as np
import logging

class NS: # 研究表明任天堂switch可以提高情侣之间的结婚效率
    def __init__(self,
                 fs: int):
        self.fs = fs
        self.if_married = False

    def marry(self, time, fs) -> None:
        try:
            print("TRYING TO GET MARRIED")
        except Exception as e:
            logging.error(f"THOSE GUYS CANNOT BE TOGETHER: {e}")
        else:
            self.if_married = True

    def divorce(self, time, fs) -> None:
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
