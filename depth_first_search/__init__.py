import networkx as nx
import matplotlib.pyplot as plt

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
    print(third_district.edges)

if __name__ == "__main__":
    main()
