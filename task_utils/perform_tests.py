import networkx as nx
import pandas as pd
from threading import Thread
import timeit
from typing import Any, Callable, Dict, List, Tuple, Union

from task_utils.algorithms import *


def get_algo_time(search_func: Callable, **kwargs) -> Tuple[float, any]:
    graph = kwargs.get("graph")
    start = kwargs.get("start")
    target = kwargs.get("target")
    start_time = timeit.default_timer()
    result = search_func(graph, start, target)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return execution_time, result


def test_algo(search_func: Callable, graph: nx.Graph, start: str, target: str, n: int) -> Dict[str, Union[str, int, float]]:
    search_res = get_algo_time(search_func, graph=graph, start=start, target=target)
    results = {
        "Algorithm": search_func.__name__,
        "Time": search_res[0],
        "Degree Centrality": round(nx.degree_centrality(graph)[target], 3),
        "Run Number": n + 1,
        "Target": target
    }
    return results


def run_search_tests(res: list, graph: nx.Graph, start: str, target: str, runs_number: int = 1) -> list:
    for n in range(runs_number):
        for call in [depth_first_search, breadth_first_search]:
            t = Thread(target=res.append, args=(test_algo(call, graph, start, target, n),))
            t.start()
            t.join()
    return res


def run_tests(grp: nx.Graph,
              start: str,
              nodes: List[str],
              runs_number: int = 3,
              ) -> List[Dict[str, Union[str, int, float]]]:
    results = []
    for node in nodes:
        t = Thread(target=run_search_tests, args=(results, grp, start, node, runs_number))
        t.start()
        t.join()
    return results
