#copyright Kenta Oshima 2022
import sys

neuron1=int(sys.argv[1])-int(sys.argv[2])
neuron2=int(sys.argv[3])-int(sys.argv[4])
neuron3=-int(sys.argv[5])-int(sys.argv[6])

print(neuron1)
print(neuron2)
print(neuron3)
total=neuron1-neuron2-neuron3

if total>3:#therefore there are 3 answers
	total=3
print(f'Score: {total}')
