from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_distribution
from matplotlib import pyplot as plt

qc = QuantumCircuit(2, 2)

qc.h(0)
qc.cx(0,1)

qc.measure(0, 0)
qc.measure(1, 1)

qc.draw('mpl', initial_state=True)
plt.show()

simulator = AerSimulator()
transpile_circuit = transpile(qc, simulator)
result = simulator.run(transpile_circuit, shots=1000).result()

counts = result.get_counts()
probabilities  = {state: (count / sum(counts.values())) * 100 for state, count in counts.items()}

print("Results:     ", counts)
print("Results in %:", probabilities)

plot_distribution(counts, title="Distribution")
plt.show()