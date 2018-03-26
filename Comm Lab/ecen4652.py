# Justin Casali, ECEN 4652, LAB 02

import numpy as np
import copy

class sigWave:

    type = 'waveform'

    def __init__(self, sig, Fs=800, t0=0):
        self.sig = np.asanyarray(sig)
        self.Fs = Fs
        self.t0 = t0
        self.Nsamp = len(self.sig)
        self.tlen = self.Nsamp / self.Fs
        self.tend = self.t0 + (self.Nsamp - 1) / Fs

    def __len__(self):
        return self.Nsamp

    def get_Fs(self):
        return self.Fs

    def get_t0(self):
        return self.t0

    def set_t0(self, t0):
        self.t0 = t0
        self.tend = self.t0 + (self.Nsamp - 1) / self.Fs

    def timeAxis(self):
        return self.t0 + np.arange(self.Nsamp) / self.Fs

    def signal(self):
        return self.sig

    def copy(self):
        return copy.deepcopy(self)

    def scale(self, factor):
        return sigWave(factor * self.sig, self.Fs, self.t0)

class sigSequ:

    type = 'sequence'

    def __init__(self, sig, FB = 100, n0 = 0):
        self.sig = np.asanyarray(sig)
        self.FB = FB
        self.n0 = n0

    def __len__(self):
        return len(self.sig)
    def get_FB(self):
        return self.FB
    def get_n0(self):
        return self.n0

    def indexAxis(self):
        return self.n0 + np.arange(len(self.sig))
    def signal(self):
        return self.sig
    def copy(self):
        return copy.deepcopy(self)
    def scale_offset(self, a, b = 0):
        return sigSequ(a*self.sig+b, self.FB, self.n0)
