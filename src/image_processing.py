#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 17:33:04 2017

@author: al
"""
import cv2
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def add_noise(image, intensity):
    # add noise with a varying degree of intensity
    # intensity is the sigma in this example
    
    im_rand = np.random.randn(*image.shape)
    noise = intensity * image.std() * im_rand
    result = noise + image
    # make sure none of the values go outside the expected range
    result = np.matrix.clip(result, 0, 255).astype(int)
    return result

def add_artifacts(image, percent):
    # shrink down the image and expand it back up to its original size
    # thus introducing artifacts to the image (blurring)
    if percent > 0.9 or percent < 0.1:
        raise ValueError("percent cannot be outside of range [0.1,0.9]")
    percent = 1.-float(percent)
    # shrink first
    small = cv2.resize(image, (0,0), fx=percent, fy=percent)
    
    percent = 1./percent
    
    big = cv2.resize(small, (0,0), fx=percent, fy=percent)
    
    return big

def rotate_image(image, degrees):
    # rotate the image by a certain number of degrees and then fill in the
    # gaps by mirroring in order to create an image of the same size
    pass

def flip_image(image, horiz = True, vert = False):
    # flip the image vertically or horizonally
    pass

if __name__ == "__main__":
    image = cv2.imread("../imgs/Lenna.png")
    noisy_image = add_noise(image,0.1)
    shrunk = add_artifacts(image, 0.9)
    plt.imshow(image)
    plt.gray()
    plt.show()
    plt.imshow(shrunk)
    plt.gray()
    plt.show()
    