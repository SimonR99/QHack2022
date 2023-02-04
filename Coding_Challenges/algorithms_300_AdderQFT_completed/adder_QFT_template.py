#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml
from matplotlib import pyplot as plt

def qfunc_adder(m, wires):
    """Quantum function capable of adding m units to a basic state given as input.

    Args:
        - m (int): units to add.
        - wires (list(int)): list of wires in which the function will be executed on.
    """

    qml.QFT(wires=wires)

    # QHACK #

    # convert m to binary
    #m_bin = np.binary_repr(m, width=len(wires))

    print(m)
    print(len(wires))


    base_rotation = 2**(len(wires))

    print(base_rotation)
    

    base_theta = (2*np.pi)/base_rotation

    for i in range(len(wires)):
        qml.RZ((m * 2 * np.pi) / (2**(i+1)), wires=i)    
    

    # QHACK #

    qml.adjoint(qml.QFT)(wires=range(n_wires))


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    m = int(inputs[0])
    n_wires = int(inputs[1])
    wires = range(n_wires)

    dev = qml.device("default.qubit", wires=wires, shots=1)

    @qml.qnode(dev)
    def test_circuit():
        # Input:  |2^{N-1}>
        qml.PauliX(wires=0)

        qfunc_adder(m, wires)
        return qml.sample()


    output = test_circuit()
    #fig, ax = qml.draw_mpl(test_circuit)()
    #plt.show()

    print(*output, sep=",")
