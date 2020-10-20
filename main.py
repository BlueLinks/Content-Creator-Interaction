import networkx as nx
import csv
import matplotlib.pyplot as plt


def main():
    # Read interactions from file
    with open("interactions.csv", "r") as f:
        csvreader = csv.reader(f, delimiter=",")
        g = nx.Graph()
        
        for row in csvreader:
            # Row in format: Creator 1,Creator2,The Interaction
            g.add_edge(row[0],row[1],how = row[2])

    # Create the plot
    plt.figure(figsize=(24, 16))
    
    labels = nx.get_edge_attributes(g,'how')
    pos = nx.kamada_kawai_layout(g)
    nx.draw_networkx_edge_labels(g,pos = pos,edge_labels = labels,font_size=8)
    nx.draw(g, pos=pos, with_labels=True)
    
    plt.savefig("Graph.png", dpi = 200)

if __name__ == __name__ == "__main__":
    main()

