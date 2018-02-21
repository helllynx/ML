from numpy.fft import fft, ifft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

# f0 = float(input('Введите частоту сигнала в герцах: '))
# A = float(input('Введите амплитуду сигнала в условных единицах: '))
# phi = float(input('Введите фазу сигнала, рад: '))
# NT = float(input('Введите количество периодов наблюдения, ед.: '))
# mvis = float(input('Введите коэффициент уменьшения интервала дискретизации: '))


f0 = 2000
A = 1
phi = 5
NT = 10
mvis = 2

w = 2 * np.pi * f0
T = 1 / f0
dtn = np.pi / w
dtv = dtn / mvis

Tnab = NT * T

Nn = Tnab / dtn
Nv = Tnab / dtn

tn = dtn * np.arange(0, Nn - 1)
tv = dtv * np.arange(0, Nv - 1)

y1n = A * np.cos(2 * np.pi * f0 * tn + phi)
y2n = A * np.sin(2 * np.pi * f0 * tn + phi)

y1v = A * np.cos(2 * np.pi * f0 * tv + phi)
y2v = A * np.sin(2 * np.pi * f0 * tv + phi)

plt.plot(tn, y1n, 'r-*')
plt.title('Discrete by Nikevist')
# xlabel('Time, sec')
# ylabel('Signal')

plt.plot(tv, y1v, 'b')
plt.title('Discrete in ' + str(mvis) + ' times more precisely')
# xlabel('Time, sec')
# ylabel('Signal')

plt.plot(tn, y2n, 'r-*')
# xlabel('Time, sec')
# ylabel('Signal')

plt.plot(tv, y2v, 'b')
# xlabel('Time, sec')
# ylabel('Signal')


plt.show()