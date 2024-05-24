import graph
import math
import sys
import queue
import dijkstra
import graph_lib as gl
from typing import List, Tuple, Dict

# SalesmanTrackBranchAndBound1 ===================================================


def SalesmanTrackBranchAndBound1(g: gl.Graph, visits: gl.Visits):  # NO IMPLEMENTAR
    raise Exception("Funció de l'apartat 1 no implementada")


# SalesmanTrackBranchAndBound2 ===================================================


def distances_and_paths(g: gl.Graph, visits: gl.Visits) -> Tuple[dict, dict]:
    """
    Returns the distances and paths between all vertices in the graph
    :param g: Graph
    :param visits: Visits
    :return: distances, paths
    """
    distances = {}
    paths = {}
    for vertex in visits.Vertices[:-1]:
        dists_v, paths_v = dijkstra.Dijkstra(g, vertex)
        distances[vertex.Name] = dists_v
        paths[vertex.Name] = paths_v
    return distances, paths


def build_track(g: gl.Graph, path: list, best_paths: dict):
    track = graph.Track(g)
    [
        track.AddLast(e)
        for i in range(len(path) - 1)
        for e in best_paths[path[i].Name][path[i + 1].Name]
    ]
    return track


def SalesmanTrackBranchAndBound2(g: gl.Graph, visits: gl.Visits):
    distances, best_paths = distances_and_paths(g, visits)

    result = build_track(g, visits.Vertices, best_paths)
    return result


# SalesmanTrackBranchAndBound3 ===================================================


def SalesmanTrackBranchAndBound3(g: gl.Graph, visits: gl.Visits):  # NO IMPLEMENTAR
    raise Exception("Funció de l'apartat 3 no implementada")
