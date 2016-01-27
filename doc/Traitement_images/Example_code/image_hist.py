from PIL import Image 
import numpy as np    
from matplotlib import pyplot as plt 
im = Image.open('../Slides/figures/image.jpg')           
channels = im.split()
z = np.array(channels[0])              
N  = z.size                       
n_classes = int(N**.5)                         
fig = plt.figure()
plt.clf()
fig.add_subplot(2, 1, 1)
plt.imshow(z, origin = "upper")
plt.colorbar()
fig.add_subplot(2, 1, 2)
plt.title('Histogramme') 
plt.ylabel('Nombre de pixels')                   
plt.xlabel('Valeurs des pixels')       
plt.hist(z.flatten(), bins=n_classes, histtype = "stepfilled")            
plt.grid()
plt.show()                       

