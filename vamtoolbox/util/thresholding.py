import numpy as np


def threshold(x: np.ndarray, thresh) -> np.typing.NDArray[np.bool]:

    x_thresh = np.array(x >= thresh, dtype=np.bool)

    return x_thresh
