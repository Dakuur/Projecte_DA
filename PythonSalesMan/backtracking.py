import graph_lib as gl
import graph
import math
import sys
import queue
import dijkstra
import copy

# ============================= BACKTRACKING PUR =============================


def next(
    current_v: gl.Vertex,
    current_e: gl.Edge,
    visits: list,
    g: gl.Graph,
    final: gl.Vertex,
):

    global path, best_path

    previs = current_e.Destination.Prev

    if (
        current_v not in previs
        and len(previs) < 2
        and path[0] + current_e.Length < best_path[0]
        and (current_e.Destination in visits or len(current_e.Destination.Edges) > 1)
    ):

        previs.append(current_v)
        path[0] += current_e.Length
        path[1].append(current_e)

        fet = False
        try:
            visits.remove(current_e.Destination)
            fet = True
        except ValueError:
            pass

        backtrack_rec(g, visits, current_e.Destination, final)

        if fet:
            visits.append(current_e.Destination)
        path[0] -= current_e.Length
        path[1].pop()
        previs.pop()


def backtrack_rec(g: gl.Graph, visits: list, current_v: gl.Vertex, final: gl.Vertex):

    global path, best_path

    if current_v == final and not visits and path[0] < best_path[0]:
        best_path[0] = path[0]
        best_path[1] = path[1].copy()
    else:
        [
            next(current_v, current_e, visits, g, final)
            for current_e in sorted(current_v.Edges, key=lambda x: x.Length)
        ]


def SalesmanTrackBacktracking(g: gl.Graph, visits: list):

    global path, best_path
    best_path = [math.inf, []]
    path = [0, []]

    for vertex in g.Vertices:
        vertex.Prev = []

    restants = visits.Vertices[1:]
    primer = visits.Vertices[0]
    ultim = visits.Vertices[-1]

    backtrack_rec(g, restants, primer, ultim)

    result = graph.Track(g)
    result.Edges = best_path[1]
    return result


# ============================ BACKTRACKING GREEDY ============================


def floyd(g: gl.Graph, visits: gl.Visits):
    distances = {}
    paths = {}
    for vertex in visits.Vertices:
        dists_v, paths_v = dijkstra.Dijkstra(g, vertex)
        distances[vertex.Name] = dists_v
        paths[vertex.Name] = paths_v
    return distances, paths


def build_track(g: gl.Graph, path: list, best_paths: dict):
    track = graph.Track(g)

    for i in range(0, len(path) - 1):  # tots menys ultim
        start = path[i].Name
        end = path[i + 1].Name
        for e in best_paths[start][end]:
            track.AddLast(e)

    return track


def SalesmanTrackBacktrackingGreedy(g: gl.Graph, visits: gl.Visits):
    best_distances, best_paths_dict = floyd(g, visits)
    best_path = []
    best_distance = math.inf

    def visit(path, total_distance):
        nonlocal best_path, best_distance
        if len(path) == len(visits.Vertices):
            if path[-1] == visits.Vertices[-1] and total_distance < best_distance:
                best_distance = total_distance
                best_path = path
        else:
            for vertex in visits.Vertices:
                if vertex not in path:
                    new_distance = (
                        total_distance + best_distances[path[-1].Name][vertex.Name]
                    )
                    visit(path + [vertex], new_distance)

    start = visits.Vertices[0]
    end = visits.Vertices[-1]
    visit([start], 0)

    track = build_track(g, best_path, best_paths_dict)
    return track
