### Import
## main import
from qiskit import *

# subpackages need to be seperately imported

## Visualialisation of Bloch
from qiskit.quantum_info import Statevector  
from qiskit.visualization import plot_bloch_multivector

## Simulator
from qiskit.providers.basic_provider import BasicSimulator

## History
from qiskit.visualization import plot_histogram


### Circuit
## Generate Circuit
circuit = QuantumCircuit(1, 1)      # circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(2)              # Make a circuit with 2 qubits (no classical bits)
gc = QuantumCircuit(2,2)            # Initialising a circuit with 2 qubits and 2 classical bits
qc_ha = QuantumCircuit(4,2)         # Make a circuit with 4 qubits and 2 classical bits

## Visualise Circuit
print(circuit)
circuit.draw()
#circuit.draw(output="mpl")
circuit.draw(output='latex')

# initial_state=True shows the qubit values at the start
qc.draw(output='mpl', initial_state=True)  

## Circuit State
init_state = Statevector(circuit);   
print(init_state)  

plot_bloch_multivector(init_state)

## Circuit Gates
circuit.x(0);       # Apply a x-Pauli to the q0 of qc
circuit.y(0);       # Apply a y-Pauli to the q0 of qc
circuit.z(0);       # Apply a z-Pauli to the q0 of qc

circuit.h(0);       # Apply a Hadamard to the q0 of qc

qc.cx(0,1)          # Apply a CNOT gate with q0 as the control bit and q1 as the target bit

qc_ha.ccx(0,1,3)    # CCNOT with q0, q1 as controls and q3 as target

qc_ha.barrier()

## Measure Circuit
circuit.measure(0, 0); # Measure qubit 0 to the classical bit 0

qc_ha.measure(2,0)  # Measure qubit 2 into classical bit 0
qc_ha.measure(3,1)  # Measure qubit 3 into classical bit 1

## Simulate Circuit
backend = BasicSimulator()

# If you do not specify the number of shots, the default is 1024
result = backend.run(circuit, shots=2000).result()   

# Extract the counts of 0 and 1 measurements
counts = result.get_counts()                    
plot_histogram(counts)