from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt

qc = QuantumCircuit(4, 2)
# q0 = Input A
# q1 = Input B
# q2 = Output Sum
# q3 = Output Carry

qc.x(0)     # comment line to set q0 = |0> 
qc.x(1)     # comment line to set q1 = |0>

qc.barrier()

# Sum= A ⊕ B
qc.cx(0,2)      # A → Sum
qc.cx(1, 2)     # B → Sum

qc.barrier()

# Carry = A ∧ B
qc.ccx(0,1,3)   # Toffoli: (A,B) -> Carry

qc.barrier()

qc.measure(2, 0)    # Sum
qc.measure(3, 1)    # Carry

qc.draw('mpl', initial_state=True)
plt.show()

simulator = AerSimulator()
transpile_circuit = transpile(qc, simulator)
result = simulator.run(transpile_circuit, shots=1000).result()

counts = result.get_counts()
print("Results:", counts)       # LittleEndian -> c1, c0