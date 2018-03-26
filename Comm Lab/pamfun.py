# Justin Casali, ECEN 4652, LAB 02

from pylab import *
import ecen4652 as ecen

def pam11(sig_an, Fs, ptype, pparms=[]):

    N = len(sig_an)
    FB = sig_an.get_FB()
    n0 = sig_an.get_n0()
    ixL = int(ceil(-Fs*(n0+0.5)/float(FB)))
    ixR = int(ceil(+Fs*(n0+N-0.5)/float(FB)))
    tt = arange(ixL, ixR) / float(Fs)
    t0 = tt[0]

    an = sig_an.signal()
    ast = zeros(len(tt))
    ix = array(around(Fs*arange(0, N)/float(FB)), int)

    ast[ix-int(ixL)] = Fs*an

    ptype = ptype.lower()

    if (ptype == 'rect'):
        kL = -0.5
        kR = -kL
    elif (ptype == 'sinc'):
        k = pparms[0]
        beta = pparms[1]
        kL = -k
        kR = -kL
    elif (ptype == 'rcf'):
        k = pparms[0]
        alpha = pparms[1]
        kL = -k
        kR = -kL
    else:
        kL = -1.0
        kR = -kL

    ixpL = int(ceil(Fs*kL/float(FB)))
    ixpR = int(ceil(Fs*kR/float(FB)))
    ttp = arange(ixpL, ixpR)/float(Fs)
    pt = zeros(len(ttp))

    if (ptype == 'rect'):
        ix = where(logical_and(ttp>=kL/float(FB), ttp<kR/float(FB)))[0]
        pt[ix] = ones(len(ix))

    elif (ptype == 'tri'):
        # length of ttp, 0 to tpp / 2
        n = len(pt)
        right = arange(0, n//2) / (n//2)
        left = 1 - arange(0, n//2) / (n//2)
        pt = hstack((right, left))

    elif (ptype == 'sinc'):
        pt = sinc(ttp*FB) * kaiser(len(pt), beta)

    elif (ptype == 'rcf'):
        pt = sinc(ttp*FB) * cos(pi*alpha*ttp*FB) / (1 - (2*alpha*ttp*FB) ** 2)

    elif (ptype == 'man'):
        n = len(pt)
        b1 = (n * 1) // 4
        b2 = (n * 2) // 4
        b3 = (n * 3) // 4
        pt[:b1] = zeros(size(ttp[:b1]))
        pt[b1:b2] = -ones(size(ttp[b1:b2]))
        pt[b2:b3] = +ones(size(ttp[b2:b3]))
        pt[b3:] = zeros(size(ttp[b3::]))

    else:
        print("ptype '%s' is nto recognized" %ptype)

    st = convolve(ast, pt) / float(Fs)
    st = st[-ixpL:ixR-ixL-ixpL]
    return ecen.sigWave(st, Fs, t0)
