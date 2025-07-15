from qiskit import *
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram

# Create the circuit
qc = QuantumCircuit(1, 1)       # 1 Qubit, 1 classical Bit

qc.h(0)             # apply Hadamard gate

qc.measure(0, 0)        # measure qubit to classical bit 

qc.draw('mpl')

# Simulate the circuit
simulator = AerSimulator()      # select the simulator

compiled_circuit = transpile(qc, simulator)     # transpile the quantum circuit in elementary gates

result = simulator.run(compiled_circuit, shots=1000).result()       # run the circuit

# Show results
counts = result.get_counts()
print("Results:", counts)
plot_histogram(counts, title="Result of Single Coin Flip")