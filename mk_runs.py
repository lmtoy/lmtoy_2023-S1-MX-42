#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2023-S1-MX-42"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["IK_Tau"] = [ 120373, 120375, 120377, 120472, 120474, 120476, 120478, 120480, 120482,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["IK_Tau"] = "pix_list=-15 dv=100 dw=100"

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["IK_Tau"] = "bank=0 pix_list=-13"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3["IK_Tau"] = "bank=1 pix_list=-13,15"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
