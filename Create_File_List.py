#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os.path
import os

pathname = '/Users/victoriacatlett/Documents/REU/Data/'

K_names = []
H_names = []

for file in os.listdir(pathname):
    if file.endswith('K.fits'):
        K_names.append(file)
    elif file.endswith('H.fits'):
        H_names.append(file)

K_path = pathname + 'K_star_names.npy'
H_path = pathname + 'H_star_names.npy'
        
np.save(K_path, K_names)
np.save(H_path, H_names)
