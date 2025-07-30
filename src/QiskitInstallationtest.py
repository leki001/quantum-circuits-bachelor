from qiskit import QuantumCircuit
from matplotlib import pyplot as plt
qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()
qc.draw('mpl')
plt.show()