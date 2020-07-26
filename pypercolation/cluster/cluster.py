

class Cluster:
    """
    Cluster instance.

    Params:
        - nodes: nodes (i.e. sites) that belong to cluster
    """
    def __init__(self, nodes):
        self.nodes = nodes

    def size(self):
        """
        Returns cluster size, i.e. number of nodes in cluster
        """
        return len(self.nodes)
