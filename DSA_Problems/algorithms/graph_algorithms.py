"""
Graph Algorithms Implementation
"""

from collections import deque, defaultdict
import heapq


class Graph:
    """Graph representation using adjacency list"""
    
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight=1):
        """Add edge to graph"""
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def bfs(self, start):
        """
        Breadth-First Search
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start):
        """
        Depth-First Search (Iterative)
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Add neighbors in reverse order for left-to-right traversal
                for neighbor, _ in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def dfs_recursive(self, start, visited=None, result=None):
        """
        Depth-First Search (Recursive)
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        if visited is None:
            visited = set()
        if result is None:
            result = []
        
        visited.add(start)
        result.append(start)
        
        for neighbor, _ in self.graph[start]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited, result)
        
        return result
    
    def dijkstra(self, start):
        """
        Dijkstra's Algorithm - Shortest path from start to all vertices
        Time Complexity: O((V + E) log V) with min heap
        Space Complexity: O(V)
        Works on: Non-negative weighted graphs
        """
        # Get all vertices by collecting keys and all neighbors
        all_vertices = set(self.graph.keys())
        for vertex in self.graph:
            for neighbor, _ in self.graph[vertex]:
                all_vertices.add(neighbor)
        
        distances = {vertex: float('inf') for vertex in all_vertices}
        distances[start] = 0
        
        pq = [(0, start)]  # (distance, vertex)
        visited = set()
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            
            for neighbor, weight in self.graph[current]:
                distance = current_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances
    
    def bellman_ford(self, start):
        """
        Bellman-Ford Algorithm - Shortest path with negative weights
        Time Complexity: O(V * E)
        Space Complexity: O(V)
        Can detect negative cycles
        """
        # Initialize distances
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        
        # Get all edges
        edges = []
        for u in self.graph:
            for v, weight in self.graph[u]:
                edges.append((u, v, weight))
        
        # Relax edges V-1 times
        vertices = list(self.graph.keys())
        for _ in range(len(vertices) - 1):
            for u, v, weight in edges:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
        
        # Check for negative cycles
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                return None  # Negative cycle detected
        
        return distances
    
    def has_cycle(self):
        """
        Detect cycle in graph using DFS
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = set()
        rec_stack = set()
        
        def dfs_cycle(vertex):
            visited.add(vertex)
            rec_stack.add(vertex)
            
            if vertex in self.graph:
                for neighbor, _ in self.graph[vertex]:
                    if neighbor not in visited:
                        if dfs_cycle(neighbor):
                            return True
                    elif neighbor in rec_stack:
                        return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in list(self.graph.keys()):
            if vertex not in visited:
                if dfs_cycle(vertex):
                    return True
        
        return False
    
    def topological_sort(self):
        """
        Topological Sort using DFS (for DAG)
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        Returns None if cycle detected
        """
        if self.has_cycle():
            return None
        
        visited = set()
        stack = []
        
        def dfs_topological(vertex):
            visited.add(vertex)
            
            if vertex in self.graph:
                for neighbor, _ in self.graph[vertex]:
                    if neighbor not in visited:
                        dfs_topological(neighbor)
            
            stack.append(vertex)
        
        for vertex in list(self.graph.keys()):
            if vertex not in visited:
                dfs_topological(vertex)
        
        return stack[::-1]


def floyd_warshall(vertices, edges):
    """
    Floyd-Warshall Algorithm - All pairs shortest path
    Time Complexity: O(V³)
    Space Complexity: O(V²)
    
    Args:
        vertices: List of vertices
        edges: List of tuples (u, v, weight)
    """
    # Initialize distance matrix
    dist = {i: {j: float('inf') for j in vertices} for i in vertices}
    
    # Distance from vertex to itself is 0
    for v in vertices:
        dist[v][v] = 0
    
    # Add edge weights
    for u, v, weight in edges:
        dist[u][v] = weight
    
    # Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist


# Example usage
if __name__ == "__main__":
    # Create graph
    print("=== Graph Traversal ===")
    g = Graph(directed=False)
    
    # Add edges
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    for u, v in edges:
        g.add_edge(u, v)
    
    print("BFS from vertex 0:", g.bfs(0))
    print("DFS from vertex 0:", g.dfs(0))
    print("DFS Recursive from vertex 0:", g.dfs_recursive(0))
    
    # Dijkstra's algorithm
    print("\n=== Dijkstra's Algorithm ===")
    g_weighted = Graph(directed=True)
    weighted_edges = [
        (0, 1, 4), (0, 2, 1),
        (2, 1, 2), (1, 3, 1),
        (2, 3, 5), (3, 4, 3)
    ]
    
    for u, v, w in weighted_edges:
        g_weighted.add_edge(u, v, w)
    
    distances = g_weighted.dijkstra(0)
    print("Shortest distances from vertex 0:")
    for vertex, dist in sorted(distances.items()):
        print(f"  To vertex {vertex}: {dist}")
    
    # Cycle detection
    print("\n=== Cycle Detection ===")
    g_cycle = Graph(directed=True)
    g_cycle.add_edge(0, 1)
    g_cycle.add_edge(1, 2)
    g_cycle.add_edge(2, 0)  # Creates cycle
    
    print("Has cycle:", g_cycle.has_cycle())
    
    # Topological sort
    print("\n=== Topological Sort ===")
    g_dag = Graph(directed=True)
    g_dag.add_edge(5, 2)
    g_dag.add_edge(5, 0)
    g_dag.add_edge(4, 0)
    g_dag.add_edge(4, 1)
    g_dag.add_edge(2, 3)
    g_dag.add_edge(3, 1)
    
    print("Topological order:", g_dag.topological_sort())
    
    # Floyd-Warshall
    print("\n=== Floyd-Warshall Algorithm ===")
    vertices = [0, 1, 2, 3]
    fw_edges = [(0, 1, 3), (0, 3, 7), (1, 0, 8), (1, 2, 2), 
                (2, 0, 5), (2, 3, 1), (3, 0, 2)]
    
    all_pairs = floyd_warshall(vertices, fw_edges)
    print("All pairs shortest paths:")
    for i in vertices:
        for j in vertices:
            print(f"  {i} -> {j}: {all_pairs[i][j]}")
