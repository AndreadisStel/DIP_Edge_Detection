import numpy as np
from fir_conv import fir_conv

def log_edge(
    in_img_array: np.ndarray
) -> np.ndarray:
    
    log_mask = np.array([
        [ 0,  0, -1,  0,  0],
        [ 0, -1, -2, -1,  0],
        [-1, -2, 16, -2, -1],
        [ 0, -1, -2, -1,  0],
        [ 0,  0, -1,  0,  0]
    ], dtype=float)

    log = fir_conv(in_img_array, log_mask)

    log_height, log_width = log.shape
    out = np.zeros((log_height, log_width), dtype=int)

    # use a minimum difference, not real line
    min_dif = 0.5

    for i in range(1, log_height - 1):
        for j in range(1, log_width - 1):

            neighbors = [
                log[i-1, j-1], log[i-1, j], log[i-1, j+1],
                log[i,   j-1], log[i,   j+1],
                log[i+1, j-1], log[i+1, j], log[i+1, j+1]
            ]
            for neighbor in neighbors:
                if (log[i, j] * neighbor) < 0 and abs(log[i, j] - neighbor) > min_dif:
                    out[i, j] = 1
                    break

    num_edges = np.sum(out)
    print(f"Found {num_edges} edges with LoG.")
    
    return out