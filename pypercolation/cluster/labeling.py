"""
Cluster labeling algorithms.
"""
import numpy as np


class HoshenKopelman():
    """
    Hoshen Kopelman cluster labeling algorithm for non-lattice graphs.
    """
    def __init__(self, network):
        self.G = network

    def raster_scan(self):
        """
        Raster scan and labeling on the network
        """
        node_l = dict((node, 0) for node in self.G.nodes) # stores nodes cluster labels
        node_lp = [] # n-th position stores cluster label for n-th label (for n non-zero integer)
                     # e.g. [1, 2, 1] means cluster 3 is equivalent to cluster 1
        k = 0

        for node in self.G.nodes:
            if self.G.nodes[node]['occupied']:
                isolated = True # node is isolated if node is occupied but none of its neighbors is occupied
                neighbors = [n for n in self.G.neighbors(node)]
                for neighbor in neighbors:
                    if self.G.nodes[neighbor]['occupied']:
                        isolated = False
                if isolated:
                    # (b) node is occupied but none of neighbors is occupied
                    k += 1 # start new cluster
                    node_l[node] = k # record new cluster in node_l
                    node_lp.append(k) # update node_lp
                else:
                    neighbors_l = dict((node, node_l[node]) for node in neighbors) # stores neighbors labels
                    if all(label == 0 for label in neighbors_l.values()): # none of the neighboring nodes is labeled
                        # (c)(i) - none of the neighboring nodes is labeled
                        k += 1 # start new cluster
                        node_l[node] = k # record new cluster in node_l
                        node_lp.append(k) # update node_lp
                    else:
                        # (c)(ii)
                        N = list(filter((0).__ne__, neighbors_l.values())) # non-null labels from neighbors_l
                        for k in range(len(N)):
                            M = node_lp[N[k]-1]
                            while M < N[k]:
                                N[k] = M
                                M = node_lp[N[k]-1]
                        node_lp_min = min(N)
                        node_l[node] = node_lp_min
                        for i in N:
                            node_lp[i-1] = node_lp_min
            else:
                # (a)
                pass

        return node_l


    def union(self, x, y):
        """
        Specifies that items x and y are members of the same cluster.
        Makes two cluster labels equivalent by linking their respective chains of aliases.
        """
        pass

    def find(self, x):
        """
        Returns a representative member of the cluster to which x belongs (i.e.
        returns cluster label).
        """
        pass

    def cluster_size_histogram(self, bins=False):
        """
        Returns cluster size histogram.
        """
        node_l = self.raster_scan()
        if bins:
            M = np.histogram(np.array(list(node_l.values())), bins=bins)
        else:
            M = np.histogram(np.array(list(node_l.values())))
        return M
