import pytest


from cph.graph import dijkstra_dists


@pytest.fixture
def graph_tests():
    return [
    ({
        0:[(1,5),(3,9),(4,1)],
        1:[(2,2),(0,5)],
        2:[(1,2),(3,6)],
        3:[(2,6),(0,9),(4,2)],
        4:[(3,2),(0,1)]
    }, [0, 5, 7, 3, 1]),
    ({
        0:[(1,5)],
        1:[(3,6),(2,7)],
        2:[(3,5)],
        3:[(0,2)],
    }, [0, 5, 12, 11]),
    ]


def test_dijkstra_dists(graph_tests):
    for graph, answer in graph_tests:
        assert dijkstra_dists(graph, 0) == answer

