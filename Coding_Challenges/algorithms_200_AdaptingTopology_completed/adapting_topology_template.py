#! /usr/bin/python3

import sys
from pennylane import numpy as np
import pennylane as qml

graph = {
    0: [1],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1],
    4: [1, 5, 7, 8],
    5: [4, 6],
    6: [5, 7],
    7: [4, 6],
    8: [4],
}


def n_swaps(cnot):
    """Count the minimum number of swaps needed to create the equivalent CNOT.

    Args:
        - cnot (qml.Operation): A CNOT gate that needs to be implemented on the hardware
        You can find out the wires on which an operator works by asking for the 'wires' attribute: 'cnot.wires'

    Returns:
        - (int): minimum number of swaps
    """

    # QHACK #

    start = cnot.wires[0]
    end = cnot.wires[1]

    # Dijkstra's algorithm
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    while len(visited) < len(graph):
        current_node = min(
            [(node, distance) for node, distance in distances.items() if node not in visited],
            key=lambda x: x[1]
        )[0]
        if current_node == end:
            break
        for neighbor in graph[current_node]:
            distance = distances[current_node] + 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        visited.add(current_node)
    

    print(distances)

    return (distances[end] -1)*2
    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    inputs = sys.stdin.read().split(",")
    output = n_swaps(qml.CNOT(wires=[int(i) for i in inputs]))
    print(f"{output}")