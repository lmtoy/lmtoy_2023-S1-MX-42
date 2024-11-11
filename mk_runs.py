#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2023-S1-MX-42"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["IK_Tau"] = [ 120373, 120375, 120377, 120472, 120474, 120476, 120478, 120480, 120482, \
                 120588, 120590, 120592, 120594, 120596, 120598, 120600, 120602, 120604, 120606, \
	         120854, 120856, 120858, 120860, 120862, \
                 120918, 120920, 120922, \
                 121021, 121023, 121025, 121027, 121029, 121094, 121096, 121098, 121100, \
                 121152, 121154, 121156, 121158, 121160, 121162, 121164, 121192, \
                 121299, 121301, 121303, 121305, 121307, 121309, 121311, 121313, 121317, \
                 121319, 121321, 121323,
                 122090, 122092, 122094, 122096, 122098, 122100, 122102, 122104,     # nov 8
                 122302, 122304, 122306, 122308, 122310, 122312, 122314, 122316,]    # nov 10


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["IK_Tau"] = "pix_list=-15 dv=50 dw=50 meta=0"

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["IK_Tau"] = "bank=0 pix_list=-13"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3["IK_Tau"] = "bank=1 pix_list=-13,15"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
