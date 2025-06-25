import numpy as np

def fir_conv(
    in_img_array: np.ndarray,
    h: np.ndarray
) -> np.ndarray:
    
    # Dimensions
    in_height, in_width = in_img_array.shape
    h_height, h_width = h.shape

    # Convolution
    h_flipped = np.flip(np.flip(h, axis=0), axis=1)

    # Zero padding
    mask_origin_row = h_height // 2
    mask_origin_col = h_width // 2

    top_padding = mask_origin_row
    bottom_padding = h_height - 1 - mask_origin_row
    left_padding = mask_origin_col
    right_padding = h_width - 1 - mask_origin_col

    padded_height = in_height + top_padding + bottom_padding
    padded_width = in_width + left_padding + right_padding
    padded_input = np.zeros((padded_height, padded_width), dtype=float)

    for i in range(in_height):
        for j in range(in_width):
            padded_input[i + top_padding, j + left_padding] = in_img_array[i, j]

    out = np.zeros_like(in_img_array, dtype=float)


    for i in range(in_height):
        for j in range(in_width):
            temp_region = padded_input[i:i + h_height, j:j + h_width]   # n * n dimensions, depend by H
            out[i, j] = np.sum(temp_region * h_flipped)

    return out