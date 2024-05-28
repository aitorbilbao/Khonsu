from stl import mesh
from DiscretizeMeshFunction import import_map_mesh
import pickle
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

#Change file path (mesh is ~297x297 km)
M = mesh.Mesh.from_file(current_dir + '/map.stl')
pickle_file = os.path.join(current_dir, 'discretized_data.pkl')
input_1 = input("New Discretisation? [Y/N]: ") # Y for new discretization, N for loading from pickle file
    
# Check if the pickle file exists
if os.path.exists(pickle_file) and input_1 == 'N':
    # Load the discretized data from the pickle file
    with open(pickle_file, 'rb') as f:
        X, Y, elevation, test_grid,grid_size = pickle.load(f)
elif input_1 == 'Y':
    # Discretize the mesh and save the result to the pickle file
    grid_size = int(input("Enter grid size: "))
    print("Importing mesh...")

    X, Y, elevation, test_grid = import_map_mesh(M, grid_size)
    with open(pickle_file, 'wb') as f:
        pickle.dump((X, Y, elevation, test_grid,grid_size), f)
else: 
    raise ValueError("Invalid input. Please enter Y or N.")
