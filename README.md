# Algorithm Performance Analysis

This scripts is designed to analyze the performance graph algorithms. The following tasks are implemented:
 - Task 1: Create a graph of the network with latencies between nodes and plot the graph.
 - Task 2: Generate an HTML report that provides a detailed analysis of algorithm performance for different configurations.
 - Task 3: Calculate the shortest path between two nodes with Dijkstra algorithm and print the shortest path between nodes.

## Requirements

- Python 3.x
- Pandas
- networkx
- matplotlib
- jinja2
- seaborn

## Usage

1. Clone the repository:

    ```bash
    git clone git@github.com:Swingyboy/goit-algo-hw-06.git
   ```

2. Navigate to the directory:

    ```bash
    cd homework_06
    ```
3. Install the required packages:

    ```bash
    pip install -r requirements.txt
   ```

4. Run the script with optional arguments:

```bash
  python task_1.py
  ```
```bash
  python task_2.py --runs 3 
  ```
Optional arguments: - **--runs**: Number of runs for each configuration (default: 3)

```bash
  python task_3.py
```

## Output

The script `task_2.py` generates an HTML report (`report.html`) which provides a detailed analysis of algorithm performance for different configurations.
The script `task_1.py` generates a graph of the network with latencies between nodes and plot the graph.
The script `task_3.py` takes graph from `task_1.py` and calculates the shortest path between two nodes with dijkstra algorithm and print the shortest path between nodes.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

