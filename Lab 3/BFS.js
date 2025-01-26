function bfs(graph, start) {
    const visited = new Set(); 
    const queue = [];         

    queue.push(start);         
    visited.add(start);        

    console.log("BFS Traversal:");
    while (queue.length > 0) {
        const current = queue.shift(); 
        console.log(current);

        for (let i = 0; i < graph[current].length; i++) {
            let neighbor = graph[current][i];
            if (!visited.has(neighbor)) {
                queue.push(neighbor);   
                visited.add(neighbor); 
            }
        }
        
    }
}

const graph = {
    A: ['B', 'C'],
    B: ['A', 'D', 'E'],
    C: ['A'],
    D: ['B'],
    E: ['B']
};

const startNode = 'A';
bfs(graph, startNode);
