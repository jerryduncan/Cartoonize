# Cartoonize

Using opencv in computer vision, the model converts realtime images into cartoon effects. In order to get the basic cartoon effect, we used the bilateral filter and some edge dectection mechanism. The bilateral filter reduces the color palette, or the numbers of colors that are used in the image, which is essential for the cartoon look and edge detection is to produce bold silhouettes. The real challenge, however, lies in the computational cost of bilateral filters. We will thus use some tricks to produce an acceptable cartoon effect in real time.

We will adhere to the following procedure to transform an RGB color image into a cartoon:

- Apply a bilateral filter to reduce the color palette of the image.
- Convert the original color image into grayscale.
- Apply a median blur to reduce image noise in the grayscale image.
- Use adaptive thresholding to detect and emphasize the edges in an edge mask.
- Combine the color image from step 1 with the edge mask from step 4.

# Libraries Needed
- Open cv
- Numpy (optional)
- Matplotlib
