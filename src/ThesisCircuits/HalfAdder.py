from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt

qc = QuantumCircuit(3, 2)
# q0 = A
# q1 = B
# q2 = C_in

qc.x(0)     # comment line to set q0 = |0> 
qc.x(1)     # comment line to set q1 = |0>

qc.barrier()

qc.ccx(0,1,2)

qc.barrier()

qc.cx(0,1)

qc.barrier()

qc.measure(1, 0)
qc.measure(2, 1)

qc.draw('mpl', initial_state=True)
plt.show()

simulator = AerSimulator()
transpile_circuit = transpile(qc, simulator)
result = simulator.run(transpile_circuit, shots=1000).result()

counts = result.get_counts()
print("Results:", counts)
plot_histogram(counts, title="Distribution")
plt.show()