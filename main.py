def printHandshakes(peoples):
    # Number of total handhsakes
    handshakes = 0
    # First represent the first people involved in the handshake
    # Cycling all the list
    for first in range(0,len(peoples)):
        # Second represent the first people involved in the handshake
        # Cycling all the list without the elements already considered
        for second in range(first+1,len(peoples)):
            print(peoples[first] + " shakes hands with " + peoples[second])
            handshakes+=1
    return handshakes

assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
