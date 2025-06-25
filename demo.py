import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from circ_hough import circ_hough
from sobel_edge import sobel_edge
from log_edge import log_edge

def load_and_preprocess_image(path):
    img = Image.open(path).convert('L')  # Grayscale
    img_array = np.array(img).astype(float) # typecast
    img_norm = img_array / 255.0  # [0, 1]
    return img_norm



img_name = 'input.jpg'


def main(): 

    img_edges = load_and_preprocess_image(img_name)
    
    # Sobel threshold and edges
    thres = 0.5
    edges_sobel = sobel_edge(img_edges, thres)

    # LoG edges
    edges_log = log_edge(img_edges)

    # Εμφάνιση αποτελεσμάτων
    fig, axs = plt.subplots(1, 3, figsize=(15,5))
    axs[0].imshow(img_edges, cmap='gray')
    axs[0].set_title('Input image (grayscale)')
    axs[0].axis('off')

    axs[1].imshow(edges_sobel, cmap='gray')
    axs[1].set_title(f'Sobel Edge Detection (thres={thres})')
    axs[1].axis('off')

    axs[2].imshow(edges_log, cmap='gray')
    axs[2].set_title('LoG Edge Detection')
    axs[2].axis('off')

    plt.show()

    # Save images
    #Image.fromarray((img_edges * 255).astype(np.uint8)).save('output_original.png')
    #Image.fromarray((edges_sobel * 255).astype(np.uint8)).save('output_sobel.png')
    #Image.fromarray((edges_log * 255).astype(np.uint8)).save('output_log.png')



    # == Find circles == #

    # Read img as grayscale
    img = Image.open(img_name).convert("L")

    # Change dimensions for faster search
    max_dim = 300
    scale = max_dim / max(img.size)
    new_size = (int(img.size[0] * scale), int(img.size[1] * scale))
    img = img.resize(new_size, Image.ANTIALIAS)

    # Read img as numpy array
    img_array = np.array(img, dtype=float) / 255.0

    # Find edges
    binary_edges = sobel_edge(img_array, thres)

    # circ hough
    R_max = 300.0
    dim = np.array([100, 100, 50])
    V_min = 55

    centers, radii = circ_hough(binary_edges.astype(int), R_max, dim, V_min)

    # Results
    plt.imshow(img_array, cmap='gray')
    for (y, x), r in zip(centers, radii):
        circle = plt.Circle((x, y), r, color='red', fill=False, linewidth=2)
        plt.gca().add_patch(circle)
    plt.title("Circles found with Hough")
    plt.axis('off')
    plt.show()



if __name__ == '__main__':
    main()
