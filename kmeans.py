#
# coding: utf-8
#
# hw8pr1.py - the k-means algorithm -- with pixels...
#

# import everything we need...
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import utils
import cv2
import math
from scipy.spatial import distance

# choose an image...
IMAGE_NAME = "./jp.png"  # Jurassic Park
IMAGE_NAME = "./batman.png"
IMAGE_NAME = "./hmc.png"
IMAGE_NAME = "./thematrix.png"
IMAGE_NAME = "./fox.jpg"
IMAGE_NAME = "./curry.jpg"
IMAGE_NAME = "./black hole.jpg"
image = cv2.imread(IMAGE_NAME, cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# reshape the image to be a list of pixels
image_pixels = image.reshape((image.shape[0] * image.shape[1], 3))

print(image_pixels)

# choose k (the number of means) in  NUM_MEANS
# and cluster the pixel intensities
NUM_MEANS = 9
clusters = KMeans(n_clusters = NUM_MEANS)
clusters.fit(image_pixels)

def posterized():
	""" The goal of this program is to posterize (get rid of gradual changes) a picture """
	new_image = image.copy()
	num_rows, num_cols, num_chans = new_image.shape
	for row in range(num_rows):
		for col in range(num_cols):
			r0,g0,b0 = image[row,col]
			min_dist = 1000000
			for center in clusters.cluster_centers_:
				r1,g1,b1 = center
				#find distance from pixel to each center
				dist = math.sqrt((r0-r1)**2 + (g0-g1)**2 + (b0-b1)**2)

				#set pixel equal to center color that is closest
				if min_dist > dist:
					min_dist = dist
					new_image[row,col] = center
			
	plt.figure()
	plt.axis("off")
	plt.imshow(new_image)
	return new_image


def center_to_coord(pixel):
	"""gets the x,y coordinate of the pixel"""
	x = 0
	y = 0
	pixel_r = pixel[0]
	pixel_g = pixel[1]
	pixel_b = pixel[2]
	print (pixel_r,pixel_g,pixel_b)
	num_rows, num_cols, num_chans = image.shape
	for row in range(num_rows):
		for col in range(num_cols):
			r,g,b = image[row,col]
			if r == pixel_r:
				print(r)
				if g == pixel_g:
					print(g)
					if b == pixel_b:
						print(r,g,b)
						x = col
						y = row
						print(x,y)
						break
	return [x,y]


# After the call to fit, the key information is contained
# in  clusters.cluster_centers_ :
count = 0
for center in clusters.cluster_centers_:
    print("Center #", count, " == ", center)
    # note that the center's values are floats, not ints!
    center_integers = [int(p) for p in center]
    print("   and as ints:", center_integers)
    count += 1

# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = utils.centroid_histogram(clusters)
bar = utils.plot_colors(hist, clusters.cluster_centers_)


# in the first figure window, show our image
#plt.figure()
#plt.axis("off")
#plt.imshow(image)

# in the second figure window, show the pixel histograms 
#   this starter code has a single value of k for each
#   your task is to vary k and show the resulting histograms
# this also illustrates one way to display multiple images
# in a 2d layout (fig == figure, ax == axes)
#
posterized()

fig, ax = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False)
title = str(NUM_MEANS)+" means"
ax[0,0].imshow(bar);    ax[0,0].set_title(title)
ax[0,1].imshow(bar);    ax[0,1].set_title(title)
ax[1,0].imshow(bar);    ax[1,0].set_title(title)
ax[1,1].imshow(bar);    ax[1,1].set_title(title)
for row in range(2):
    for col in range(2):
        ax[row,col].axis('off')
plt.show(fig)





#
# comments and reflections on hw8pr1, k-means and pixels
"""
 + Which of the paths did you take:  
    + posterizing or 
    + algorithm-implementation

 + How did it go?  Which file(s) should we look at?
 + Which function(s) should we try...


 1) I did the posterization one.
 2 It went well, if you just run this hw, it will posterize the latest IMAGE_NAME. This is the image I want you to
 look at. Orginially, we were stuck on taking the 2D distance when really we needed to take the 3D distance. Once
 we figured that out, everything went very smoothly.
"""
#
#