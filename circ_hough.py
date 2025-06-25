import numpy as np

def circ_hough(in_img_array: np.ndarray, R_max: float, dim: np.ndarray, V_min: int):
    height, width = in_img_array.shape
    num_x, num_y, num_r = dim

    # Create 3D Hough for voting
    hough_votes = np.zeros((num_y, num_x, num_r), dtype=int)

    # Create bins of pixels, adding a R_min to eliminate the small "false" circles 
    R_min = 60.0
    x_bins = np.linspace(0, width, num_x + 1)
    y_bins = np.linspace(0, height, num_y + 1)
    r_bins = np.linspace(R_min, R_max, num_r + 1)

    # "White" pixels
    ys, xs = np.nonzero(in_img_array)   # from sobel || log

    # Check for radius
    for r_idx in range(num_r):
        r = (r_bins[r_idx] + r_bins[r_idx + 1]) / 2
        # Check for every "white" point 
        for x, y in zip(xs, ys):
            # Find the possible centers
            for theta in range(0, 360, 30):  # Adjust for faster, less accurate results
                a = x - r * np.cos(np.deg2rad(theta))
                b = y - r * np.sin(np.deg2rad(theta))
                # Check if the possible center exists
                if 0 <= a < width and 0 <= b < height:
                    # Find a, b bins
                    x_idx = np.searchsorted(x_bins, a, side='right') - 1
                    y_idx = np.searchsorted(y_bins, b, side='right') - 1
                    if 0 <= x_idx < num_x and 0 <= y_idx < num_y:
                        hough_votes[y_idx, x_idx, r_idx] += 1

    # Find centers and radii if votes >= minimun votes
    centers = []
    radii = []

    for y_idx in range(num_y):
        for x_idx in range(num_x):
            for r_idx in range(num_r):
                if hough_votes[y_idx, x_idx, r_idx] >= V_min:
                    # Mapping
                    x_c = (x_bins[x_idx] + x_bins[x_idx + 1]) / 2
                    y_c = (y_bins[y_idx] + y_bins[y_idx + 1]) / 2
                    r_c = (r_bins[r_idx] + r_bins[r_idx + 1]) / 2

                    centers.append([y_c, x_c])  # Numpy array (y, x)
                    radii.append(r_c)

    return np.array(centers, dtype=float), np.array(radii, dtype=float)
