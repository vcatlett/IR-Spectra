#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import os

pathname = '/Your/Path/Name/'  # change to the path where your data is

K_names = []
H_names = []

for file in os.listdir(pathname):
    if file.endswith('K.fits') or file.startswith('SDCK'):
        K_names.append(file)
    elif file.endswith('H.fits') or file.startswith('SDCH'):
        H_names.append(file)

K_path = pathname + 'K_star_names.npy'
H_path = pathname + 'H_star_names.npy'
        
np.save(K_path, K_names)
np.save(H_path, H_names)
