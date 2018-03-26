# Justin Casali, ECEN 4652, LAB 03
# From Prof Mathys in ECEN 4242

# File: ptfun.py
# Python module for generating p(t) for PAM in the GRC

import numpy as np

def pampt(sps, ptype, pparms=[]):

    if ptype.lower() == 'rcf':

        nk = round(pparms[0]*sps)
        nn = np.arange(-nk,nk)
        pt = np.sinc(nn/float(sps))  # sinc pulse

        if len(pparms) > 1:
            p2t = 0.25*np.pi*np.ones(len(nn))
            ix = np.where(np.power(2*pparms[1]*nn/float(sps),2.0) != 1)[0]
            p2t[ix] = np.cos(np.pi*pparms[1]*nn[ix]/float(sps))
            p2t[ix] = p2t[ix]/(1-np.power(2*pparms[1]*nn[ix]/float(sps),2.0))
            pt = pt*p2t

    elif ptype.lower() == 'rect':
        nn = np.arange(0,sps)
        pt = np.ones(len(nn))

    elif ptype.lower() == 'sinc':
        nk = round(pparms[0]*sps)
        nn = np.arange(-nk,nk)
        pt = np.sinc(nn/float(sps))
        if len(pparms) > 1:
            pt = pt*np.kaiser(len(pt),pparms[1])

    elif ptype.lower() == 'tri':
        nn = np.arange(-sps, sps)
        pt = np.zeros(len(nn))
        ix = np.where(nn < 0)[0]
        pt[ix] = 1 + nn[ix]/float(sps)
        ix = np.where(nn >= 0)[0]
        pt[ix] = 1 - nn[ix]/float(sps)

    elif ptype.lower() == 'man':
        nn = np.arange(-sps, sps)
        pt = np.zeros(len(nn))
        n = len(pt)
        b1 = (n * 1) // 4
        b2 = (n * 2) // 4
        b3 = (n * 3) // 4
        pt[:b1] = np.zeros(np.size(nn[:b1]))
        pt[b1:b2] = -np.ones(np.size(nn[b1:b2]))
        pt[b2:b3] = +np.ones(np.size(nn[b2:b3]))
        pt[b3:] = np.zeros(np.size(nn[b3::]))

    elif ptype.lower() == 'rcf':
        nk = round(pparms[0]*sps)
        nn = np.arange(-nk,nk)
        pt = np.sinc(nn*FB) * np.cos(pi*pparms[1]*nn*FB) / (1 - (2*pparms[1]*nn*FB) ** 2)

    else:
        pt = np.ones(1)

    return pt
