# posterize
Transform images using pixel clusters


I used an algorithim called k-means that uses a given paramter k, to estimate the given dataset. For instance, if k was 2, then the alorigthm figures out how to best represent the dataset with 2 datapoints. The higher k is, the closer the representative dataset is to the original. You can use the algorithim to manipulate picutres, to strip down the number of colors.

Using k-means on pictures, popular pixel colors are used for clustering. For instance, using a k of 2, the picture would be transformed to use only 2 colors that most represent the picture, or the array of pixels provided. 

I have attached some cool transformations below.



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
