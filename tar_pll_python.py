# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:01:38 2017

@author: gerrychou
"""
import tarfile
from shutil import copy2
from datetime import datetime

f_list_bak=['Linsys',
        'pll_analyze_noise.py',
        'pll7428_analyze.py',
        'tar_pll_python.py',
        'pll_summary.html']
 
f_list_ftp=f_list_bak + ['vco_pn.printsnpn0',
        'pfd_cp_lpf_pn.printsnpn0']

##--- tar source code + noise file, send to d:\ftp ---
f_list = f_list_ftp
fn_tar = 'Python_PLL.tar'
copy_to = 'D:/ftp'

tar=tarfile.open(fn_tar, "w")
for fn in f_list:
    tar.add(fn)
tar.close()
copy2(fn_tar, copy_to)

print("\nSend '" + fn_tar + "' to '" + copy_to + "'" )

##--- tar source code only, send to .\bak ---
f_list = f_list_bak
fn_tar = 'Python_PLL_'+datetime.now().strftime("%Y%m%d_%H%M")+'.tar'
copy_to = './bak'

tar=tarfile.open(fn_tar, "w")
for fn in f_list:
    tar.add(fn)
tar.close()
copy2(fn_tar, copy_to)

print("Send '" + fn_tar + "' to '" + copy_to + "'" )



