import pytest


from cph.graph import dijkstra_dists


@pytest.fixture
def graph_tests():
    return [
    ({
        1:[(2,5),(4,9),(5,1)],
        2:[(3,2),(1,5)],
        3:[(2,2),(4,6)],
        4:[(3,6),(1,9),(5,2)],
        5:[(4,2),(1,1)]
    }, [0, 5, 7, 3, 1]),
    ({
        1:[(2,5)],
        2:[(4,6),(3,7)],
        3:[(4,5)],
        4:[(1,2)],
    }, [0, 5, 12, 11]),
    ]


def test_dijkstra_dists(graph_tests):
    for graph, answer in graph_tests:
        assert dijkstra_dists(graph, 1) == answer

