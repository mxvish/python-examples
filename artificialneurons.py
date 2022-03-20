#copyright Kenta Oshima 2022
import sys

neuron=2+int(sys.argv[1])-int(sys.argv[2])-int(sys.argv[3])+int(sys.argv[4])
if 2*neuron == 8:
	print("Neuron is fully activated")
elif 2*neuron == 0:
	print("Neuron is completely inactivated")
else:
    print(f'Score: {2*neuron}')
