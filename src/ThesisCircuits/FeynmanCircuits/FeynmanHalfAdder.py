from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt

qc = QuantumCircuit(3, 2)
# q0 = Input A      | Output A
# q1 = Input B      | Output Sum
# q2 = Input 0      | Output Carry

qc.x(0)     # comment line to set q0 = A = |0> 
qc.x(1)     # comment line to set q1 = B = |0>

qc.barrier()

qc.ccx(0,1,2)
qc.cx(0,1)

qc.barrier()

qc.measure(1, 0)    # Sum
qc.measure(2, 1)    # Carry

qc.draw('mpl', initial_state=True)
plt.show()

simulator = AerSimulator()
transpile_circuit = transpile(qc, simulator)
result = simulator.run(transpile_circuit, shots=1000).result()

counts = result.get_counts()
print("Results:", counts)