"""This module showcases an implementation of depth-first search with networkx. """

import matplotlib.pyplot as plt
import networkx as nx


def main():
    third_district = nx.Graph()
    third_district.add_edges_from([
        ("Bingawan", "Calinog"),
        ("Calinog", "Lambunao"),
        ("Lambunao", "Janiuay"),
        ("Lambunao", "Badiangan"),
        ("Janiuay", "Maasin"),
        ("Janiuay", "Cabatuan"),
        ("Badiangan", "Mina"),
        ("Badiangan", "Pototan"),
        ("Cabatuan", "Mina"),
        ("Mina", "Pototan"),
    ])

    plt.figure("Third District Graph")
    nx.draw_networkx(third_district, node_color = "#ced495", node_shape = "s")
    plt.show()
    # Find a path using depth first search from Pototan to Calinog
    if third_district_subgraph := depth_first_search(third_district, "Pototan", "Calinog"):
        nx.draw_networkx(third_district_subgraph, node_color = "#ced495", node_shape = "s")
        plt.show()

def depth_first_search(graph: nx.Graph, start, target) -> nx.Graph | None:
    # Copied from https://github.com/TheAlgorithms/Python/blob/master/graphs/depth_first_search.py
    visited, stack = set(start), [start]
    step = 0
    
    while stack:
        current = stack.pop()
        step += 1
        print(f"Step: {step} @ Node: {current}")
        visited.add(current)
        if (current == target):
            def nodes_filter(x):
                return x in visited
            return nx.subgraph_view(graph, nodes_filter)
        for adjacent in (graph[current]):
            if adjacent not in visited:
                stack.append(adjacent)
        print(stack)
    
    return None

if __name__ == "__main__":
    main()
