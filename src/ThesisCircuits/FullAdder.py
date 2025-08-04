from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile
from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt

qc = QuantumCircuit(8, 2)
# q0 = A
# q1 = B
# q2 = C_in
# q3 = AND1(A,B)
# q4 = XOR1(A,B)
# q5 = XOR2(C,q4) = XOR2(C,XOR1) = SUM
# q6 = AND2(C,q4) = AND2(C,XOR1)
# q7 = OR(q3,q6)  = OR(AND1,AND2) = C_out

qc.x(0)     # comment line to set q0 = |0> 
qc.x(1)     # comment line to set q1 = |0>
qc.x(2)     # comment line to set q2 = |0>

qc.barrier()
# AND1(A,B)
qc.ccx(0,1,3)   

qc.barrier()
# XOR1(A,B)
qc.cx(0,4)
qc.cx(1,4)

qc.barrier()
# XOR2(C,q4) = XOR2(C,XOR1) = SUM
qc.cx(2,5)
qc.cx(4,5)

qc.barrier()
# AND2(C,q4) = AND2(C,XOR1)
qc.ccx(2,4,6)

qc.barrier()
# OR(q3,q6)  = OR(AND1,AND2) = C_out
qc.x(3)
qc.x(6)
qc.ccx(3,6,7)
qc.x(7)

qc.barrier()
qc.measure(5, 0)
qc.measure(7, 1)

qc.draw('mpl', initial_state=True)
plt.show()

simulator = AerSimulator()
transpile_circuit = transpile(qc, simulator)
result = simulator.run(transpile_circuit, shots=1000).result()

counts = result.get_counts()
print("Results:", counts)
plot_histogram(counts, title="Distribution")
plt.show()