from qiskit import *
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt

# Create the circuit
qc = QuantumCircuit(3, 3)       # three Qubits and three classical Bits

# apply Hadamard gate to all three qubits (superposition)
qc.h(0)
qc.h(1)
qc.h(2)

# Measure each qubit and write to corresponding classic bit
qc.measure(0, 0)
qc.measure(1, 1)
qc.measure(2, 2)

qc.draw('mpl')
plt.show()

# Simulate the circuit
simulator = AerSimulator()      # select the simulator

compiled_circuit = transpile(qc, simulator)     # transpile the quantum circuit in elementary gates

result = simulator.run(compiled_circuit, shots=1000).result()       # run the circuit

# Show results
counts = result.get_counts()
print("Results:", counts)
plot_histogram(counts, title="Result of Tripple Coin Flip")
plt.show()