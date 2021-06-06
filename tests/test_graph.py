from app.graph import Graph


def test_graph():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(2, 0)
    g.add_edge(2, 1)
    g.add_edge(1, 3)
    paths = g.print_all_paths(2, 3)
    assert paths == [[2, 0, 1, 3], [2, 0, 3], [2, 1, 3]]
