import graph
import math
import sys
import queue
import dijkstra
import graph_lib as gl
from typing import List, Tuple, Dict
from copy import deepcopy, copy

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
    for vertex in visits.Vertices[
        :-1
    ]:  # skip the last vertex (no exiting paths from it)
        dists_v, paths_v = dijkstra.Dijkstra(g, vertex)
        distances[vertex.Name] = dists_v
        paths[vertex.Name] = paths_v
    return distances, paths


def min_max_levels(dist_dict: dict, path: list, visits: gl.Visits) -> float:
    """
    Returns the minimum level of the vertices in the path
    :param dist_dict: dict with the distances between all vertices
    :param path: list of vertices
    :param visits: Visits
    :return: minimum level
    """
    to_visit = [
        v.Name for v in visits.Vertices if (v not in path and v != visits.Vertices[-1])
    ]

    heuristics = dict()

    for i in to_visit:
        maximum_d = 0
        minimum_d = math.inf
        for k, v in dist_dict.items():
            if i == k:
                continue
            if v[i] > maximum_d:
                maximum_d = v[i]
            if v[i] < minimum_d:
                minimum_d = v[i]
        heuristics[i] = (minimum_d, maximum_d)

    return heuristics


def build_track(g: gl.Graph, path: list, best_paths: dict) -> gl.Track:
    """
    Builds the track (all vertices and edges) from the best paths between the vertices to be visited (ordered)
    :param g: Graph
    :param path: list of vertices to be visited
    :param best_paths: dict with the best paths between all vertices to be visited
    """
    track = graph.Track(g)
    [
        track.AddLast(e)
        for i in range(len(path) - 1)
        for e in best_paths[path[i].Name][path[i + 1].Name]
    ]
    return track


def SalesmanTrackBranchAndBound2(g: gl.Graph, visits: gl.Visits):
    dist_dict, paths_dict = distances_and_paths(g, visits)

    heuristics = min_max_levels(dist_dict, [], visits)

    # result = build_track(g, path, paths_dict)
    # return result

    raise Exception("Funció de l'apartat 2 no implementada")


# SalesmanTrackBranchAndBound3 ===================================================


def SalesmanTrackBranchAndBound3(g: gl.Graph, visits: gl.Visits):  # NO IMPLEMENTAR
    raise Exception("Funció de l'apartat 3 no implementada")
