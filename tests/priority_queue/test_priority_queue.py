from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    mock = [
        {"qtd_linhas": 7},
        {"qtd_linhas": 3},
        {"qtd_linhas": 8},
        {"qtd_linhas": 1},
    ]

    result = PriorityQueue()
    result.enqueue(mock[0])
    result.enqueue(mock[1])
    result.enqueue(mock[2])
    result.enqueue(mock[3])

    assert len(result) == 4
    assert result.search(0) == mock[1]
    assert result.search(1) == mock[3]
    assert result.search(2) == mock[0]
    assert result.search(3) == mock[2]

    result.dequeue()
    assert len(result) == 3
    assert result.search(0) == mock[3]

    result.dequeue()
    assert len(result) == 2
    assert result.search(0) == mock[0]

    result.dequeue()
    assert len(result) == 1
    assert result.search(0) == mock[2]

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        result.search(10)
