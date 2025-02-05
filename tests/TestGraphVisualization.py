import sys

sys.path.append("")

import unittest
import numpy as np
import io

from causallearn.graph.Dag import Dag
from causallearn.graph.GraphNode import GraphNode
from causallearn.utils.GraphUtils import GraphUtils
from causallearn.utils.DAG2PAG import dag2pag
from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.cit import fisherz
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class testGraphVisualization(unittest.TestCase):

    def test_draw_CPDAG(self):
        data_path = "data_linear_10.txt"
        data = np.loadtxt(data_path, skiprows=1)  # Import the file at data_path as data
        cg = pc(data, 0.05, fisherz, True, 0,
                -1)  # Run PC and obtain the estimated graph (CausalGraph object)
        pyd = GraphUtils.to_pydot(cg.G)
        tmp_png = pyd.create_png(f="png")
        fp = io.BytesIO(tmp_png)
        img = mpimg.imread(fp, format='png')
        plt.axis('off')
        plt.imshow(img)
        plt.show()
        print('finish')

    def test_draw_DAG(self):
        nodes = []
        for i in range(3):
            nodes.append(GraphNode(f"X{i + 1}"))
        dag1 = Dag(nodes)

        dag1.add_directed_edge(nodes[0], nodes[1])
        dag1.add_directed_edge(nodes[0], nodes[2])
        dag1.add_directed_edge(nodes[1], nodes[2])

        pyd = GraphUtils.to_pydot(dag1)
        pyd.write_png('dag.png')

    def test_draw_PAG(self):
        nodes = []
        for i in range(5):
            nodes.append(GraphNode(str(i)))
        dag = Dag(nodes)
        dag.add_directed_edge(nodes[0], nodes[1])
        dag.add_directed_edge(nodes[0], nodes[2])
        dag.add_directed_edge(nodes[1], nodes[3])
        dag.add_directed_edge(nodes[2], nodes[4])
        dag.add_directed_edge(nodes[3], nodes[4])
        pag = dag2pag(dag, [nodes[0], nodes[2]])

        pyd = GraphUtils.to_pydot(pag)
        pyd.write_png('pag.png')

