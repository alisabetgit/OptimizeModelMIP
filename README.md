<h1 align="center">Optimize Model MIP</h1>
<p align="center">
  <a href="https://medium.com/@alisabetio"><img alt="Medium" src="https://skydoves.github.io/badges/Story-Medium.svg"/></a>
</p>
<p align="center">  
OptimizeModelMIP is a code that solves the graph optimization model using the Python MIP library.
</p>
</br>
<p align="center">
<img src="/Images/Output.png"/>
</p>

## About
Suppose a directional graph G=(N,A) in which each arc (i,j) in A, represents a positive number c(i,j) and represents the length of that arc.</br>Also, vertices O and D represent the vertices of origin and destination.</br>To find the shortest path from vertex O to vertex D, we define the following binary variable:</br>“δ(i,j) : The binary variable whose arc (i,j)is on the shortest path is one, otherwise it is zero.”
</br>Thus the shortest path problem is formulated as follows, in which the first condition guarantees that the selected route leaves the origin, the second condition guarantees that the selected route enters the destination, and the third condition guarantees that if the selected route reaches a vertex (Except for the origin and destination) entered, exits and thus, the continuity of the path is maintained.
</br>
<p align="center">
<img src="/Images/Formula.png"/>
</p>

## Example
- implement the above model in Python.
- give the following graph information to Python and solve the model of Part A for the following data with the MIP library.
- draw a graph with Python and specify the shortest path on it.
</br>
<p align="center">
<img src="/Images/Graph.png"/>
</p>

## Tech stack
- Python
- [Python-MIP](https://www.python-mip.com) is a modelling tool developed to provide : Ease of use, High performance, Extensibility
  
## Installation
- clone it.
- pip install mip==1.6.5
- pip install matplotlib
