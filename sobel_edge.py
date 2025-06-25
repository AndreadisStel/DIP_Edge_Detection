import numpy as np
from  fir_conv import fir_conv


def sobel_edge(
    in_img_array: np.ndarray,
    thres: float
) -> np.ndarray:
    
    Gx = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=float)

    Gy = np.array([
        [+1, +2, +1],
        [ 0,  0,  0],
        [-1, -2, -1]
    ], dtype=float)

    gx = fir_conv(in_img_array, Gx)
    gy = fir_conv(in_img_array, Gy)

    g = np.sqrt(gx**2 + gy**2)

    out = (g > thres).astype(int)

    num_edges = np.sum(out)
    print(f"Found {num_edges} edges.")

    return out