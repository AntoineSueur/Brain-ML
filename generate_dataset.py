# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import cv2
import itertools
import numpy as np
import random


colors = [x for x in itertools.product((0,255), (0,255), (0,255))] 
positions = ['top left','middle left','bottom left', 'top center', 'middle center', 'bottom center', 'top right','middle right', 'bottom right']
color_names = ['black','blue','green','cyan','red','magenta','yellow','white']

def generate_random_image(w, h, n_points_row):

    coords = [i*w//(n_points_row + 1 ) for i in range(1,n_points_row + 1)]
    anchors = [x for x in itertools.product(coords, coords)]
    radius = w//(4*n_points_row)
    image = np.ones((w,h,3))*125
    anchor, caption = random.sample(list(zip(anchors, positions)), 1)[0]
    noisy_anchor = (int(anchor[0] + radius*(random.random()-0.5)*2), int(anchor[1] + radius*(random.random()-0.5)*2))
    color, color_name = random.sample(list(zip(colors, color_names)), 1)[0]
    cv2.circle(image, noisy_anchor, radius, color, -1)
    #cv2.circle(image, anchor, int(radius/4), colors[0], -1)
    caption = 'The circle is at the ' + caption + ' of the picture.'
    return image, caption

def generate_anchor_position(w, h, n_points_row):

    coords = [i*w//(n_points_row + 1 ) for i in range(1,n_points_row + 1)]
    anchors = [x for x in itertools.product(coords, coords)]
    radius = w//(4*n_points_row)
    image = np.ones((w,h,3))*125
    for i, x in enumerate(list(zip(anchors, positions))):
        anchor, caption = x
        cv2.circle(image, anchor, radius, colors[i%8], -1)
    cv2.imwrite('tmp_image.jpg', image)
    
def generate_examples(n_samples):
    w,h = 224, 224    
    n_points_per_row = 3
    with open('Data/Circle_text/circle_annotations_train.txt', 'w') as f:
        for i in range(n_samples):
            image, caption = generate_random_image(w, h, n_points_per_row)
            cv2.imwrite('Data/Circle_Dataset/train/images/image_train_{}.jpg'.format(i), image)
            f.write('image_train_{}.jpg#0 '.format(i) + '\t' + caption + '\n')
    f.close()

#generate_examples(2000)
generate_anchor_position(224,224,3)
