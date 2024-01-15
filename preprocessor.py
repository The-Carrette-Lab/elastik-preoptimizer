import numpy as np
class Preprocessor:
    raw: np.array
    avg_value: int

    def __init__(self, raw: np.array):
        self.raw = raw
        self.avg_value = np.average(raw)

    def preprocess(self, lower_value: int) -> np.array:
        return_array = np.copy(self.raw)

        # background exclusion
        for (x, y, z), value in np.ndenumerate(return_array):
            value = return_array[x][y][z]

            if value < self.avg_value or value < lower_value:
                return_array[x][y][z] = 0

        # normalization
        return_array = (return_array - np.min(return_array)) / \
            (np.max(return_array) - np.min(return_array))

            
        return return_array
    