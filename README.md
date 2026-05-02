# E-Commerce Delivery Route Optimization Using Shortest Path

## 1. Real-World Problem Context

In e-commerce logistics, delivering products efficiently from warehouses to customers is a critical operational challenge. Companies must determine the most efficient routes to minimize transportation costs and delivery times.

This project models a simplified e-commerce delivery network and aims to identify the shortest delivery route from a warehouse to a customer zone.

---

## 2. Problem Definition

The objective of this project is to determine the shortest path between a warehouse and a customer zone in a logistics network.

- Nodes represent logistics facilities such as warehouses, distribution centers, hubs, and customer zones.
- Edges represent transportation routes between these facilities.
- Each edge has:
  - Distance (in kilometers)
  - Delivery time (in minutes)

The goal is to minimize the total travel distance.

---

## 3. Network Model

The system is represented as an undirected graph.

- Nodes represent logistics components:
  - Warehouse
  - Distribution Centers
  - Hubs
  - Customer Zone

- Edges represent delivery routes between these components.

- Each edge includes a distance value (used for optimization) and a delivery time.

### Data Assumptions

The dataset used in this project is a simplified but realistic representation of an e-commerce logistics network.

- Distance values are based on realistic transportation distances.
- Delivery times are proportional to distance and operational delays.
- The network structure reflects typical hub-and-spoke logistics design.

---

## 4. Nodes and Edges

Nodes used in the network:

- Warehouse  
- DistributionCenter_A  
- DistributionCenter_B  
- DistributionCenter_C  
- Hub_D  
- Hub_E  
- Hub_F  
- CustomerZone  

Each edge contains:

- distance_km  
- delivery_time_min  

Dataset location:

data/path_data.csv

---

## 5. Selected Algorithm

The problem is solved using the Shortest Path Problem.

Algorithm used:

- Dijkstra Algorithm
- Implemented using the NetworkX library

Why this method?

- Efficient for weighted graphs  
- Guarantees optimal shortest path  
- Widely used in logistics and routing systems  

---

## 6. Python Implementation

The solution is implemented using the following libraries:

- pandas → data processing  
- networkx → graph modeling and optimization  
- matplotlib → visualization  

Workflow:

1. Load dataset from CSV  
2. Build the graph  
3. Apply Dijkstra algorithm  
4. Compute shortest path  
5. Calculate total distance and time  
6. Visualize the network  

Main script:

src/shortestpath_solution.py

---

## 7. Results

The model produces:

- Shortest delivery path  
- Total distance (km)  
- Estimated delivery time (minutes)  

Outputs are stored in:

results/output.txt  
results/shortestpath_visualization.png  

---

## 8. Managerial Interpretation

The results show the most efficient delivery route from the warehouse to the customer zone.

From a managerial perspective:

- The company can reduce transportation costs  
- Delivery speed can be improved  
- Inefficient routes can be identified  
- Supports data-driven logistics decision-making  

---

## 9. How to Run the Code

Install dependencies:

pip install -r requirements.txt

Run the solution:

python src/shortestpath_solution.py

---

## 10. References

- NetworkX Documentation: https://networkx.org  
- Python Documentation: https://docs.python.org  
