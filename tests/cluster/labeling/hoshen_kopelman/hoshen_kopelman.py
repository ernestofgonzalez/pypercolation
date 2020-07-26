"""
Tests for pypercolation.cluster.HoshenKopelman
"""

import networkx as nx

# initialize graph
G = nx.read_edgelist("network-example.edgelist")

# Set site occupancy
G.add_node('1', occupied=True)
G.add_node('2', occupied=True)
G.add_node('3', occupied=True)
G.add_node('4', occupied=False)
G.add_node('5', occupied=True)
G.add_node('6', occupied=True)
G.add_node('7', occupied=True)
G.add_node('8', occupied=False)
G.add_node('9', occupied=False)
G.add_node('10', occupied=True)
G.add_node('11', occupied=True)
G.add_node('12', occupied=False)
G.add_node('13', occupied=False)
G.add_node('14', occupied=True)
G.add_node('15', occupied=False)
G.add_node('16', occupied=True)

import sys
sys.path.insert(1, '/home/ernestogonzalez/Documents/pypercolation')
from pypercolation.cluster.labeling import HoshenKopelman


hoshen_kopelman = HoshenKopelman(network=G)
M = hoshen_kopelman.cluster_size_histogram()

print(M)
