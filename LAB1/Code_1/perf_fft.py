import time
from numpy import linspace, cos, sin, pi, absolute, arange, pi, asarray, exp, dot
from numpy.fft import fft, fftfreq, fftshift
import matplotlib.pyplot as plt

X_timer = []
Y_timer = []

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        Y_timer.append(time2 - time1)
        return ret
    return wrap


def plotMe(x, y, title='', xlabel='', ylabel=''):
    plt.plot(x, y, 'ro')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid()
    plt.show()


def DFT(y):
    y = asarray(y, dtype=float)
    N = y.shape[0]
    n = arange(N)
    k = n.reshape((N, 1))
    M = exp(-2j * pi * k * n / N)
    return dot(M, y)

@timing
def FFT(fft_func, signal_func, signal_freq, signal_duration=1.0, need_plot_sp=True):
    # Sampling rate
    fs = signal_freq*4  # Hz
    N = fs * signal_duration
    t = linspace(0, signal_duration, num=N, endpoint=False, dtype=float)

    # for timer
    X_timer.append(len(t))

    # Generate a sinusoid at frequency f
    f = signal_freq  # Hz
    a = signal_func(2 * pi * f * t)
    # print('Input signal size = ' + str(a.size))

    # Plot signal, showing how endpoints wrap from one chunk to the next
    if(need_plot_sp):
        plt.subplot(2, 1, 1)
        plt.plot(t, a, '.-')
        plt.margins(0.1, 0.1)
        plt.xlabel('Time [s]')

    # Use FFT to get the amplitude of the spectrum
    ampl = 1/N * absolute(fft_func(a))


    if(need_plot_sp):
        # FFT frequency bins
        freqs = fftfreq(int(N), 1 / fs)

        plt.subplot(2, 1, 2)
        plt.stem(fftshift(freqs), fftshift(ampl))
        plt.margins(0.1, 0.1)
        plt.xlabel('Frequency [Hz]')
        plt.tight_layout()
        plt.show()


time_ = arange(0.1, 1, 0.05)

for t in time_:
    FFT(fft, sin, 2000, t, False)

plotMe(X_timer, Y_timer, 'FFT')

X_timer.clear()
Y_timer.clear()

for t in time_:
    FFT(DFT, sin, 2000, t, False)

plotMe(X_timer, Y_timer, 'DFT')



