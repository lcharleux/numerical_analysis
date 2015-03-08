from PIL import Image 
import numpy as np   
from matplotlib import pyplot as plt 
from matplotlib import cm
im = Image.open('../data/grenouille.jpg') 
rouge, vert, bleu = im.split()
z = np.array(rouge)



