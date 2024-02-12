import numpy as np
class Preprocessor:
    def preprocess(self, raw: np.array, lower_value: int =0) -> np.array:
        avg_value = np.average(raw)

        # background exclusion
        for (x, y, z), value in np.ndenumerate(raw):
            value = raw[x][y][z]

            if value < avg_value or value < lower_value:
                raw[x][y][z] = 0

        # normalization
        raw = (raw - np.min(raw)) / \
            (np.max(raw) - np.min(raw))

            
        return raw
    