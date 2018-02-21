from numpy.fft import fft, ifft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
import timeit


def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def DFT_VS_FFT(func, frequency, sample_rate):
    sampling_interval = 1.0 / sample_rate
    t = np.arange(0, 1, sampling_interval)
    print('Input data size = ' + str(t.size))
    y = func(2 * np.pi * frequency * t)

    n = len(y)  # length of the signal
    k = np.arange(n)
    T = n / sample_rate
    frq = k / T  # two sides frequency range
    frq = frq[np.arange(int(n / 2))]  # one side frequency range

    # % timeit
    # np.fft.fft(y)

    Y = np.fft.fft(y) / n  # fft computing and normalization
    Y = Y[np.arange(int(n / 2))]
    #
    # % timeit
    # DFT_slow(y)

    Y_1 = DFT_slow(y) / n
    Y_1 = Y_1[np.arange(int(n / 2))]

    plt.plot(t, y)
    plt.title('Input Signal')
    plt.show()

    plt.plot(frq, abs(Y))
    plt.title('FFT')
    plt.show()

    plt.plot(frq, abs(Y_1))
    plt.title('slow DFT')
    plt.show()


ff = 2000  # frequency of the signal

rate = 5000

print('### SIN ###')
DFT_VS_FFT(np.sin, ff, rate)

print('### COS ###')
DFT_VS_FFT(np.cos, ff, rate)


