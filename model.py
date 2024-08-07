import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Ellipse
def random_color():
    return (random.random(), random.random(), random.random())

# Function to create a circle
def create_circle():
    fig, ax = plt.subplots()
    circle = plt.Circle((0.5, 0.5), 0.4, color='yellow', fill=True)
    ax.add_artist(circle)
    ax.set_aspect('equal', adjustable='box')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.title("Circle")
    # Original pat
    new_path = "circle.png"
    plt.savefig(new_path)
    plt.show()

# # Function to create a square
# def create_square():
#     fig, ax = plt.subplots()
#     square = plt.Rectangle((0.25, 0.25), 0.5, 0.5, color=random_color(), fill=True)
#     ax.add_artist(square)
#     ax.set_aspect('equal', adjustable='box')
#     plt.xlim(0, 1)
#     plt.ylim(0, 1)
#     plt.title("Square")
#     plt.savefig("square.png")
#     plt.show()

# # Function to create a rectangle
# def create_rectangle():
#     fig, ax = plt.subplots()
#     rectangle = plt.Rectangle((0.2, 0.3), 0.6, 0.4, color=random_color(), fill=True)
#     ax.add_artist(rectangle)
#     ax.set_aspect('equal', adjustable='box')
#     plt.xlim(0, 1)
#     plt.ylim(0, 1)
#     plt.title("Rectangle")
#     plt.savefig("rectangle.png")
#     plt.show()

# # Function to create a triangle
# def create_triangle():
#     fig, ax = plt.subplots()
#     triangle = plt.Polygon([[0.5, 0.8], [0.2, 0.2], [0.8, 0.2]], color=random_color(), fill=True)
#     ax.add_artist(triangle)
#     ax.set_aspect('equal', adjustable='box')
#     plt.xlim(0, 1)
#     plt.ylim(0, 1)
#     plt.title("Triangle")
#     plt.savefig("triangle.png")
#     plt.show()

# # Function to create a sphere
# def create_sphere():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     u = np.linspace(0, 2 * np.pi, 100)
#     v = np.linspace(0, np.pi, 100)
#     x = 0.5 * np.outer(np.cos(u), np.sin(v))
#     y = 0.5 * np.outer(np.sin(u), np.sin(v))
#     z = 0.5 * np.outer(np.ones(np.size(u)), np.cos(v))
#     ax.plot_surface(x, y, z, color=random_color())
#     ax.set_title("Sphere")
#     plt.savefig("sphere.png")
#     plt.show()

# # Function to create a cube
# def create_cube():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     r = [-0.5, 0.5]
#     X, Y = np.meshgrid(r, r)
    
#     # Top and bottom faces
#     Z = np.full_like(X, 0.5)
#     ax.plot_surface(X, Y, Z, color=random_color())
#     Z = np.full_like(X, -0.5)
#     ax.plot_surface(X, Y, Z, color=random_color())
    
#     # Front and back faces
#     Z = np.full_like(X, 0.5)
#     ax.plot_surface(X, -0.5, Y, color=random_color())
#     ax.plot_surface(X, 0.5, Y, color=random_color())
    
#     # Left and right faces
#     ax.plot_surface(0.5, X, Y, color=random_color())
#     ax.plot_surface(-0.5, X, Y, color=random_color())
    
#     ax.set_title("Cube")
#     plt.savefig("cube.png")
#     plt.show()

# # Function to create a tetrahedron
# def create_tetrahedron():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     vertices = np.array([[1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1]])
#     faces = [[vertices[j] for j in [0, 1, 2]],
#              [vertices[j] for j in [0, 1, 3]],
#              [vertices[j] for j in [0, 2, 3]],
#              [vertices[j] for j in [1, 2, 3]]]
#     poly3d = Poly3DCollection(faces, facecolors=random_color(), linewidths=1, edgecolors='r')
#     ax.add_collection3d(poly3d)
#     ax.set_title("Tetrahedron")
#     plt.savefig("tetrahedron.png")
#     plt.show()

# # Function to create an octahedron
# def create_octahedron():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     vertices = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
#     faces = [[vertices[j] for j in [0, 2, 4]],
#              [vertices[j] for j in [0, 3, 4]],
#              [vertices[j] for j in [0, 2, 5]],
#              [vertices[j] for j in [0, 3, 5]],
#              [vertices[j] for j in [1, 2, 4]],
#              [vertices[j] for j in [1, 3, 4]],
#              [vertices[j] for j in [1, 2, 5]],
#              [vertices[j] for j in [1, 3, 5]]]
#     poly3d = Poly3DCollection(faces, facecolors=random_color(), linewidths=1, edgecolors='r')
#     ax.add_collection3d(poly3d)
#     ax.set_title("Octahedron")
#     plt.savefig("octahedron.png")
#     plt.show()

# # Function to create a cuboid
# def create_cuboid():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     r = [-0.5, 0.5]
#     X, Y = np.meshgrid(r, r)
    
#     # Top and bottom faces
#     Z = np.full_like(X, 0.3)
#     ax.plot_surface(X, Y, Z, color=random_color())
#     Z = np.full_like(X, -0.3)
#     ax.plot_surface(X, Y, Z, color=random_color())
    
#     # Front and back faces
#     Z = np.full_like(X, 0.3)
#     ax.plot_surface(X, -0.5, Y, color=random_color())
#     ax.plot_surface(X, 0.5, Y, color=random_color())
    
#     # Left and right faces
#     ax.plot_surface(0.5, X, Y, color=random_color())
#     ax.plot_surface(-0.5, X, Y, color=random_color())
    
#     ax.set_title("Cuboid")
#     plt.savefig("cuboid.png")
#     plt.show()

# # Function to create a cone
# def create_cone():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     height = 1
#     radius = 1
#     z = np.linspace(0, height, 50)
#     theta = np.linspace(0, 2 * np.pi, 50)
#     theta, z = np.meshgrid(theta, z)
#     x = radius * (1 - z / height) * np.cos(theta)
#     y = radius * (1 - z / height) * np.sin(theta)
#     ax.plot_surface(x, y, z, color=random_color())
#     ax.set_title("Cone")
#     plt.savefig("cone.png")
#     plt.show()

# # Function to create a cylinder
# def create_cylinder():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     z = np.linspace(0, 1, 50)
#     theta = np.linspace(0, 2 * np.pi, 50)
#     theta_grid, z_grid = np.meshgrid(theta, z)
#     x_grid = np.cos(theta_grid)
#     y_grid = np.sin(theta_grid)
#     ax.plot_surface(x_grid, y_grid, z_grid, color=random_color())
#     ax.set_title("Cylinder")
#     plt.savefig("cylinder.png")
#     plt.show()

# # Function to create a pyramid
# def create_pyramid():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0.5, 0.5, 1]])
#     faces = [[vertices[j] for j in [0, 1, 4]],
#              [vertices[j] for j in [1, 2, 4]],
#              [vertices[j] for j in [2, 3, 4]],
#              [vertices[j] for j in [3, 0, 4]],
#              [vertices[j] for j in [0, 1, 2, 3]]]
#     poly3d = Poly3DCollection(faces, facecolors=random_color(), linewidths=1, edgecolors='r')
#     ax.add_collection3d(poly3d)
#     ax.set_title("Pyramid")
#     plt.savefig("pyramid.png")
#     plt.show()

# # Function to create a prism
# def create_prism():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     vertices = np.array([[0, 0, 0], [1, 0, 0], [0.5, np.sqrt(3)/2, 0], [0, 0, 1], [1, 0, 1], [0.5, np.sqrt(3)/2, 1]])
#     faces = [[vertices[j] for j in [0, 1, 2]],
#              [vertices[j] for j in [3, 4, 5]],
#              [vertices[j] for j in [0, 1, 4, 3]],
#              [vertices[j] for j in [1, 2, 5, 4]],
#              [vertices[j] for j in [2, 0, 3, 5]]]
#     poly3d = Poly3DCollection(faces, facecolors=random_color(), linewidths=1, edgecolors='r')
#     ax.add_collection3d(poly3d)
#     ax.set_title("Prism")
#     plt.savefig("prism.png")
#     plt.show()

# # Function to create a dodecahedron
# def create_dodecahedron():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     phi = (1 + np.sqrt(5)) / 2
#     vertices = np.array([
#         [-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
#         [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1],
#         [0, -1/phi, -phi], [0, -1/phi, phi], [0, 1/phi, -phi], [0, 1/phi, phi],
#         [-1/phi, -phi, 0], [-1/phi, phi, 0], [1/phi, -phi, 0], [1/phi, phi, 0],
#         [-phi, 0, -1/phi], [-phi, 0, 1/phi], [phi, 0, -1/phi], [phi, 0, 1/phi]
#     ])
#     faces = [
#         [0, 8, 4, 14, 12], [0, 12, 2, 10, 16], [0, 16, 1, 9, 8], [1, 9, 5, 19, 17], [1, 17, 3, 13, 12],
#         [2, 10, 6, 18, 16], [2, 13, 3, 11, 10], [3, 11, 7, 15, 13], [4, 8, 9, 5, 14], [4, 14, 6, 18, 15],
#         [5, 19, 7, 15, 14], [6, 18, 7, 19, 17], [8, 9, 5, 14, 12], [10, 11, 7, 15, 13], [16, 17, 3, 13, 12]
#     ]
#     poly3d = Poly3DCollection([vertices[face] for face in faces], facecolors=random_color(), linewidths=1, edgecolors='r')
#     ax.add_collection3d(poly3d)
#     ax.set_title("Dodecahedron")
#     plt.savefig("dodecahedron.png")
#     plt.show()

# # Function to create an icosahedron
# def create_icosahedron():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     phi = (1 + np.sqrt(5)) / 2
#     vertices = np.array([
#         [-1, phi, 0], [1, phi, 0], [-1, -phi, 0], [1, -phi, 0],
#         [0, -1, phi], [0, 1, phi], [0, -1, -phi], [0, 1, -phi],
#         [phi, 0, -1], [phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1]
#     ])
#     faces = [
#         [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
#         [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
#         [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
#         [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
#     ]
#     poly3d = Poly3DCollection([vertices[face] for face in faces], facecolors=random_color(), linewidths=1, edgecolors='r')
#     ax.add_collection3d(poly3d)
#     ax.set_title("Icosahedron")
#     plt.savefig("icosahedron.png")
#     plt.show()


# # Function to create a hedgehog (star)
# def create_hedgehog():
#     fig, ax = plt.subplots()
#     num_points = 10
#     angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
#     points = np.column_stack([np.cos(angles), np.sin(angles)])
#     for point in points:
#         ax.plot([0, point[0]], [0, point[1]], color=random_color())
#     ax.set_aspect('equal')
#     ax.set_title("Hedgehog (Star)")
#     plt.savefig("hedgehog.png")
#     plt.show()

# # Function to create a kite
# def create_kite():
#     fig, ax = plt.subplots()
#     points = np.array([[0, 0], [1, 2], [2, 0], [1, -1]])
#     polygon = Polygon(points, closed=True, color=random_color())
#     ax.add_patch(polygon)
#     ax.set_aspect('equal')
#     ax.set_title("Kite")
#     plt.savefig("kite.png")
#     plt.show()

# # Function to create a sector
# def create_sector():
#     fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
#     theta = np.linspace(0, np.pi / 2, 100)
#     r = 1
#     x = r * np.cos(theta)
#     y = r * np.sin(theta)
#     ax.plot(np.append(x, 0), np.append(y, 0), color=random_color())
#     ax.fill(np.append(x, 0), np.append(y, 0), color=random_color())
#     ax.set_title("Sector")
#     plt.savefig("sector.png")
#     plt.show()

# # Function to create a segment
# def create_segment():
#     fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
#     theta = np.linspace(0, np.pi / 2, 100)
#     r = 1
#     x = r * np.cos(theta)
#     y = r * np.sin(theta)
#     ax.plot(np.append(x, 0), np.append(y, 0), color=random_color())
#     ax.fill_between(x, y, color=random_color())
#     ax.set_title("Segment")
#     plt.savefig("segment.png")
#     plt.show()

# # Function to create an annulus
# def create_annulus():
#     fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
#     theta = np.linspace(0, 2 * np.pi, 100)
#     r1 = 1
#     r2 = 0.5
#     x1 = r1 * np.cos(theta)
#     y1 = r1 * np.sin(theta)
#     x2 = r2 * np.cos(theta)
#     y2 = r2 * np.sin(theta)
#     ax.fill(np.append(x1, x2[::-1]), np.append(y1, y2[::-1]), color=random_color())
#     ax.set_title("Annulus")
#     plt.savefig("annulus.png")
#     plt.show()

# # Function to create a torus
# def create_torus():
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     theta = np.linspace(0, 2 * np.pi, 100)
#     phi = np.linspace(0, 2 * np.pi, 100)
#     theta, phi = np.meshgrid(theta, phi)
#     r, R = 0.3, 1
#     x = (R + r * np.cos(theta)) * np.cos(phi)
#     y = (R + r * np.cos(theta)) * np.sin(phi)
#     z = r * np.sin(theta)
#     ax.plot_surface(x, y, z, color=random_color())
#     ax.set_title("Torus")
#     plt.savefig("torus.png")
#     plt.show()


# # Function to create an ellipse
# def create_ellipse():
#     fig, ax = plt.subplots()
#     ellipse = Ellipse((0.5, 0.5), width=1, height=0.5, angle=0, color=random_color())
#     ax.add_patch(ellipse)
#     ax.set_aspect('equal')
#     ax.set_title("Ellipse")
#     plt.savefig("ellipse.png")
#     plt.show()


# # Function to create a rhombus
# def create_rhombus():
#     fig, ax = plt.subplots()
#     points = np.array([[0, 0], [1, 2], [2, 0], [1, -2]])
#     polygon = Polygon(points, closed=True, color=random_color())
#     ax.add_patch(polygon)
#     ax.set_aspect('equal')
#     ax.set_title("Rhombus")
#     plt.savefig("rhombus.png")
#     plt.show()

# # Function to create a polygon with a given number of sides
# def create_polygon(num_sides, title, filename):
#     fig, ax = plt.subplots()
#     angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
#     points = np.column_stack([np.cos(angles), np.sin(angles)])
#     polygon = Polygon(points, closed=True, color=random_color())
#     ax.add_patch(polygon)
#     ax.set_aspect('equal')
#     ax.set_xlim(-1.5, 1.5)
#     ax.set_ylim(-1.5, 1.5)
#     ax.set_title(title)
#     plt.savefig(filename)
#     plt.show()

# # Function to create a parallelogram
# def create_parallelogram():
#     fig, ax = plt.subplots()
#     points = np.array([[0, 0], [2, 0], [3, 1], [1, 1]])
#     polygon = Polygon(points, closed=True, color=random_color())
#     ax.add_patch(polygon)
#     ax.set_aspect('equal')
#     ax.set_xlim(-1, 4)
#     ax.set_ylim(-1, 2)
#     ax.set_title("Parallelogram")
#     plt.savefig("parallelogram.png")
#     plt.show()

# # Function to create a rhombus
# def create_rhombus():
#     fig, ax = plt.subplots()
#     points = np.array([[0, 0], [1, 2], [2, 0], [1, -2]])
#     polygon = Polygon(points, closed=True, color=random_color())
#     ax.add_patch(polygon)
#     ax.set_aspect('equal')
#     ax.set_xlim(-1, 3)
#     ax.set_ylim(-3, 3)
#     ax.set_title("Rhombus")
#     plt.savefig("rhombus.png")
#     plt.show()

# # Function to create a trapezoid
# def create_trapezoid():
#     fig, ax = plt.subplots()
#     points = np.array([[0, 0], [3, 0], [2, 1], [1, 1]])
#     polygon = Polygon(points, closed=True, color=random_color())
#     ax.add_patch(polygon)
#     ax.set_aspect('equal')
#     ax.set_xlim(-1, 4)
#     ax.set_ylim(-1, 2)
#     ax.set_title("Trapezoid")
#     plt.savefig("trapezoid.png")
#     plt.show()

# # Function to create a kite
# def create_kite():
#     fig, ax = plt.subplots()
#     points = np.array([[0, 0], [1, 2], [2, 0], [1, -1]])
#     polygon = Polygon(points, closed=True, color=random_color())
#     ax.add_patch(polygon)
#     ax.set_aspect('equal')
#     ax.set_xlim(-1, 3)
#     ax.set_ylim(-2, 3)
#     ax.set_title("Kite")
#     plt.savefig("kite.png")
#     plt.show()

# # Function to create an arrow
# def create_arrow():
#     fig, ax = plt.subplots()
#     points = np.array([[0, 0], [2, 1], [1, 1], [1, 3], [-1, 3], [-1, 1], [-2, 1]])
#     polygon = Polygon(points, closed=True, color=random_color())
#     ax.add_patch(polygon)
#     ax.set_aspect('equal')
#     ax.set_xlim(-3, 3)
#     ax.set_ylim(-1, 4)
#     ax.set_title("Arrow")
#     plt.savefig("arrow.png")
#     plt.show()

# # Example usage
# #create Pentagon
# create_polygon(5, "Pentagon", "pentagon.png")
# #create Hexagon
# create_polygon(6, "Hexagon", "hexagon.png")
# #create Heptagon
# create_polygon(7, "Heptagon", "heptagon.png")
# #create Octagon
# create_polygon(8, "Octagon", "octagon.png")
# #create Nonagon
# create_polygon(9, "Nonagon", "nonagon.png")
# #create Decagon
# create_polygon(10, "Decagon", "decagon.png")
# create_ellipse()
# create_parallelogram()
# create_rhombus()
# create_trapezoid()
# create_hedgehog()
# create_kite()
# create_arrow()
# create_sector()
# create_segment()
# create_annulus()
# create_torus()
# create_cone()
# create_cylinder()
# create_sphere()
# create_pyramid()
# create_prism()
# create_dodecahedron()
# create_icosahedron()
# create_tetrahedron()
# create_octahedron()
# create_cube()
# create_cuboid()
# create_circle()
# create_square()
# create_rectangle()
# create_triangle()
create_circle()

