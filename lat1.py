import matplotlib.pyplot as plt
    
from skimage import data
from skimage.transform import swirl

image = data.checkerboard()
swirled = swirl(image, rotation=0, strength=10,
radius=120)
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2,
figsize=(8, 3),
 sharex=True,
sharey=True)
ax0.imshow(image, cmap=plt.cm.gray)
ax0.axis('off')
ax1.imshow(swirled, cmap=plt.cm.gray)
ax1.axis('off')
plt.show()