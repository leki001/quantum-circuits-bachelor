from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt

qc = QuantumCircuit(6, 2)
# q0 = Input A
# q1 = Input B
# q2 = Input C_in
# q3 = Intermediate value (auxiliary qubit)
# q4 = Output Sum
# q5 = Output C_out

qc.x(0)     # comment line to set q0 = |0> 
qc.x(1)     # comment line to set q1 = |0>
qc.x(2)     # comment line to set q2 = |0>

qc.barrier()
# Auxiliary qubit
# q3 = A ⊕ B
qc.cx(0, 3)
qc.cx(1, 3)  

qc.barrier()
# Output sum
# q4 = (A ⊕ B) ⊕ Carry-in
qc.cx(2, 4)
qc.cx(3, 4)

qc.barrier()
# Output C_out
# A ∧ B → in q5
qc.ccx(0, 1, 5)
# (A⊕B) ∧ C_in
qc.ccx(3, 2, 5)

qc.barrier()
qc.measure(4, 0)
qc.measure(5, 1)

qc.draw('mpl', initial_state=True)
plt.show()

simulator = AerSimulator()
transpile_circuit = transpile(qc, simulator)
result = simulator.run(transpile_circuit, shots=1000).result()

counts = result.get_counts()
print("Results:", counts)
plot_histogram(counts, title="Full Adder Output Distribution")
plt.show()