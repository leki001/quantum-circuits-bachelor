from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_distribution
from matplotlib import pyplot as plt

# Create the circuit
qc = QuantumCircuit(1, 1)       # 1 Qubit, 1 classical Bit
qc.h(0)             # apply Hadamard gate
qc.measure(0, 0)        # measure qubit to classical bit 

qc.draw('mpl', initial_state=True)
plt.show()

# Simulate the circuit
simulator = AerSimulator()      # select the simulator
transpile_circuit = transpile(qc, simulator)     # transpile the quantum circuit in elementary gates
result = simulator.run(transpile_circuit, shots=1000).result()       # run the circuit

# Show results
counts = result.get_counts()
probabilities = {state: (count / sum(counts.values())) * 100 for state, count in counts.items()}

print("Results:     ", counts)
print("Results in %:", probabilities)

plot_distribution(counts, title="Coin Flip Distribution")
plt.show()