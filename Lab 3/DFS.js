function dfs(graph, start) {
    const visited = new Set(); 
    const stack = [];          

    stack.push(start);         
    visited.add(start);        

    console.log("DFS Traversal:");
    while (stack.length > 0) {
        const current = stack.pop(); 
        console.log(current);

        for (let i = 0; i < graph[current].length; i++) {
            let neighbor = graph[current][i];
            if (!visited.has(neighbor)) {
                stack.push(neighbor);   
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
dfs(graph, startNode);
