from PIL import Image 
import numpy as np    
import matplotlib.pyplot as plt
im = Image.open(
  '../data/grenouille.jpg') 
fig = plt.figure(0) 
plt.clf()
plt.imshow(im, origin = "lower")
plt.xlabel("pixels")
plt.ylabel("pixels")
plt.show()

