from pylab import *

def showft(sig_xt, ff_lim):

    N = len(sig_xt)
    Fs = sig_xt.get_Fs()
    tt = sig_xt.timeAxis()
    ixp = where(tt >= 0)[0]
    ixn = where(tt < 0)[0]
    xt = sig_xt.signal()
    xt = hstack((xt[ixp], xt[ixn]))

    # Shifted fft
    Xf = fftshift(fft(xt)) / Fs

    # Corrected freq range
    ff = Fs * array(arange(-N/2+1, N/2+1), int64) / N

    # Lower & Upper indexs of range
    lower = int(ff_lim[0] * N / Fs + (N/2 + 1))
    upper = int(ff_lim[1] * N / Fs + (N/2 + 1))

    absXf = abs(Xf)
    argXf = angle(Xf)

    ff_lim_from_dB = (10 ** (ff_lim[2] / 20)) * max(absXf)

    if (ff_lim[2] < 0):
        max_abx_Xf = max(absXf)
        f1 = figure()
        af11 = f1.add_subplot(211)
        absXf = (absXf <= ff_lim_from_dB) * ff_lim_from_dB + (absXf > ff_lim_from_dB) * absXf
        af11.plot(ff[lower:upper+1], 20*log10(absXf[lower:upper+1]/max_abx_Xf))
        af11.grid()
        af11.set_ylabel('20*log_10(|X(f)|) [dB]')
        strgt = 'FT Approximation, $F_s=$' + str(Fs) + ' Hz'
        strgt = strgt + ', N=' + str(N)
        strgt = strgt + ', $\Delta_f$={0:3.2f}'.format(Fs/N) + ' Hz'
        af11.set_title(strgt)
        # Phase plot
        af12 = f1.add_subplot(212)
        argXf = (absXf <= ff_lim_from_dB) * 0 + (absXf > ff_lim_from_dB) * argXf
        af12.plot(ff[lower:upper+1], 180/pi * argXf[lower:upper+1])
        af12.grid()
        af12.set_ylabel('arg[X(f)] [deg]')
        af12.set_xlabel('f [Hz]')
        show()
    else:
        f1 = figure()
        af11 = f1.add_subplot(211)
        absXf = (absXf <= ff_lim[2]) * ff_lim[2] + (absXf > ff_lim[2]) * absXf
        af11.plot(ff[lower:upper+1], absXf[lower:upper+1])
        af11.grid()
        af11.set_ylabel('|X(f)|')
        strgt = 'FT Approximation, $F_s=$' + str(Fs) + ' Hz'
        strgt = strgt + ', N=' + str(N)
        strgt = strgt + ', $\Delta_f$={0:3.2f}'.format(Fs/N) + ' Hz'
        af11.set_title(strgt)
        # Phase plot
        af12 = f1.add_subplot(212)
        argXf = (absXf <= ff_lim[2]) * 0 + (absXf > ff_lim[2]) * argXf
        af12.plot(ff[lower:upper+1], 180/pi * argXf[lower:upper+1])
        af12.grid()
        af12.set_ylabel('arg[X(f)] [deg]')
        af12.set_xlabel('f [Hz]')
        show()

def showeye(sig_rt, FB, NTd=50, dispparams=[]):
    rt = sig_rt.signal()
    Fs = sig_rt.get_Fs()
    t0 = dispparams[0] / FB
    tw = dispparams[1] / FB
    dws = int(floor(Fs*tw))
    tteye = arange(dws) / Fs
    trix = around(Fs*(t0+arange(NTd)/FB))
    ix = where(logical_and(trix>=0, trix<=len(rt)-dws))[0]
    trix = trix[ix]
    TM = rt[int(trix[0]):int(trix[0]+dws)]
    for x in range(1, NTd):
        TM = vstack((TM, rt[int(trix[x]):int(trix[x]+dws)]))
    plot(FB*tteye, TM.T, '-b')
    xlabel('t/FB')
    ylabel('r(t)')
    grid()
    show()

def showpsd(sig_xt, ff_lim, N):

    xt = sig_xt.signal()
    Fs = sig_xt.get_Fs()
    N = int(min(N, len(xt)))
    NN = int(floor(len(xt)/float(N)))

    xt = xt[0:N*NN]
    xNN = reshape(xt,(NN,N))

    Sxf = np.power(abs(fft(xNN)),2.0)
    if NN > 1:
        Sxf = sum(Sxf, axis=0)/float(NN)
    Sxf = Sxf/float(N*Fs)
    Sxf = reshape(Sxf,size(Sxf))
    ff = Fs*array(arange(N),int64)/float(N)
    if ff_lim[0] < 0:
        ixp = where(ff<0.5*Fs)[0]
        ixn = where(ff>=0.5*Fs)[0]
        ff = hstack((ff[ixn]-Fs,ff[ixp]))
        Sxf = hstack((Sxf[ixn],Sxf[ixp]))
    df = Fs/float(N)

    power_total = sum(Sxf)

    maxSxf = max(Sxf)
    ixf = where(logical_and(ff>=ff_lim[0], ff<ff_lim[1]))[0]
    ff = ff[ixf]
    Sxf = Sxf[ixf]

    power_range = sum(Sxf)

    strgt = '$P_x$ = {:.3g}'.format(power_total)
    strgt = strgt + ', $P_x(f_x, f_2) = ${:.3g}'.format(power_range)

    max_dB = 10*log10(maxSxf)
    strgy = 'PSD: $S_x(f)$'
    if (ff_lim[2] < 0):
        Sxf = 10*log10(Sxf) - max_dB
        Sxf = (Sxf <= ff_lim[2]) * ff_lim[2] + (Sxf > ff_lim[2]) * Sxf
        strgt = '$P_x$ = {:.3g}'.format(power_total)
        strgt = strgt + ', $P_x(f_x, f_2) = ${:.3g}%'.format(power_range/power_total*100)
        strgy = 'PSD: $10*log_{10}(S_x(f))$'

    strgt = strgt + ', $F_s=${:d} Hz'.format(Fs)
    strgt = strgt + ', $\\Delta_f=${:.3g} Hz'.format(df)
    strgt = strgt + ', $NN=${:d}, $N=${:d}'.format(NN, N)
    f1 = figure()
    af1 = f1.add_subplot(111)
    af1.plot(ff, Sxf, '-b')
    af1.grid()
    af1.set_xlabel('f [Hz]')
    af1.set_ylabel(strgy)
    af1.set_title(strgt)
    show()
