import matplotlib.pyplot as plt
from mip import Model, xsum, minimize, BINARY

# edges start & end vertices & length of edge
edgesMat = [[0, 1, 5],
            [0, 2, 1],
            [1, 4, 2],
            [2, 3, 1],
            [3, 0, 1],
            [3, 6, 2],
            [4, 5, 3],
            [5, 7, 1],
            [6, 5, 1],
            [7, 6, 1]]

# vertices Locations
locations = [[0, 1, 1, 1, 2, 3, 3, 4],
             [1, 2, 1, 0, 1, 2, 0, 1]]

# number of nodes and list of vertices
n, V = edgesMat[-1][0] + 1, set(range(edgesMat[-1][0] + 1))

# distance matrix
distVec = [0 for i in range(len(edgesMat))]
for k in range(len(edgesMat)):
    distVec[k] = edgesMat[k][2]

model = Model(solver_name='CBC')

# binary variables indicating if arc (i,j) is used on the route or not
x = [model.add_var(var_type=BINARY) for i in range(len(edgesMat))]

# objective function: minimize the distance
model.objective = minimize(xsum(distVec[i] * x[i] for i in range(len(edgesMat))))

# constraint : leaving start node one more time than entering it
model += xsum(x[i] if edgesMat[i][0] == 0 else 0 for i in range(len(edgesMat))) - xsum(
    x[i] if edgesMat[i][1] == 0 else 0 for i in range(len(edgesMat))) == 1

# constraint : entering destination node one more time than leaving it
model += xsum(x[i] if edgesMat[i][1] == n - 1 else 0 for i in range(len(edgesMat))) - xsum(
    x[i] if edgesMat[i][0] == n - 1 else 0 for i in range(len(edgesMat))) == 1

# constraint : entering each middle node as many as leaving it
for j in (V - {0, len(V) - 1}):
    model += xsum(x[i] if edgesMat[i][0] == j else 0 for i in range(len(edgesMat))) - xsum(
        x[i] if edgesMat[i][1] == j else 0 for i in range(len(edgesMat))) == 0

# optimizing
model.optimize()

# ------- Plot Graph --------------------------------
# plotting the Edges
edgesX = [[locations[0][vec[0]], locations[0][vec[1]]] for vec in edgesMat]
edgesY = [[locations[1][vec[0]], locations[1][vec[1]]] for vec in edgesMat]
for i in range(len(edgesX)):
    plt.arrow(edgesX[i][0], edgesY[i][0], edgesX[i][1] - edgesX[i][0], edgesY[i][1] - edgesY[i][0],
              length_includes_head=True, head_width=0.1, head_length=0.3, fc='b', ec='b')
    plt.text((edgesX[i][1] + edgesX[i][0]) / 2 + .05, (edgesY[i][1] + edgesY[i][0]) / 2 + .1, str(edgesMat[i][2]),
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=15, color='black')

if model.num_solutions:
    print(' ----------------------------------------------------------------------- ')
    print('\tOptimum route with total distance {0} found:'.format(model.objective_value))
    nc = 0
    print(' ----------------------------------------------------------------------- ')
    print('\tO', end='')
    while True:
        pointX = locations[0][nc] + .05
        pointY = locations[1][nc] + .05
        nc = [edgesMat[i][1] for i in range(len(edgesMat)) if ((x[i].x >= 0.99) and (edgesMat[i][0] == nc))][0]
        plt.arrow(pointX, pointY, locations[0][nc] - pointX + .05, locations[1][nc] - pointY + .05,
                  length_includes_head=True, head_width=.1, head_length=.2, fc='r', ec='r', width=.01)
        if not (nc == len(V) - 1):
            print(' -> {0}'.format(nc), end='')
        else:
            print(' -> D', end='')
            break
    print('\n ---------------------------------------------------------------------- \n')

# plotting the Vertices
plt.plot(locations[0][:], locations[1][:], linestyle='None', marker='o', markerfacecolor='green', markersize=20)
for i in range(1, len(locations[0]) - 1):
    plt.text(locations[0][i], locations[1][i], str(i),
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=15, color='white')
plt.text(locations[0][0], locations[1][0], 'O',
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=15, color='white')
plt.text(locations[0][-1], locations[1][-1], 'D',
         horizontalalignment='center',
         verticalalignment='center',
         fontsize=15, color='white')
plt.gca().axis('off')

# giving a title to my graph
plt.title('Shortest Path Problem')

# function to show the plot
plt.show()