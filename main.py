import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mayavi import mlab
import ollama
import re
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import Polygon, Ellipse


shapes = [
    "Circle",
    "Square",
    "Rectangle",
    "Triangle",
    "Ellipse",
    "Parallelogram",
    "Rhombus",
    "Trapezoid",
    "Pentagon",
    "Hexagon",
    "Heptagon",
    "Octagon",
    "Nonagon",
    "Decagon",
    "Hedgehog (Star)",
    "Kite",
    "Arrow",
    "Sector",
    "Segment",
    "Annulus",
    "Torus",
    "Cone",
    "Cylinder",
    "Sphere",
    "Pyramid",
    "Prism",
    "Dodecahedron",
    "Icosahedron",
    "Tetrahedron",
    "Octahedron",
    "Cube",
    "Cuboid"
]
colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
]
# Generate Python code for drawing the selected shape
def generate_code(shape, color):
    print("Generating code..")
    print(f"Color: {color}")
    print(f"Shape: {shape}")
    response = ollama.chat(
    model="llama3",
   messages=[{ 
        "content":f'''
        ##Prompt:generate a python code which can create and save image of {shape} fill the image with {color} using matplotlib and strictly give only python code between this pattern "$$ code write here.. $$" without fucntion
        and call the function to show and save the image do not write plt.show() in code
    ''' ,"role": "system"}]
     )
    code = response["message"]["content"]
    print(code)
    return code

# Main function to run the process
def is_syntax_correct(code):
    try:
        compile(code, '<string>', 'exec')
        return True
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
        return False

# Function to execute the code
def execute_code(code):
    try:
        exec(code)
        return True
    except Exception as e:
        print(f"Runtime Error: {e}")
        return False

# Loop to generate and check code until it is correct

def main():
    code=''
    
    for shape in shapes:
        while True:
            code = generate_code(shape, random.choice(colors))
            match = re.search(r'\$\$(.*?)\$\$', code, re.DOTALL)
            code= match.group(1)
            # print("Generated Code:\n", code)
            if match.group(1):
                print("Generated code.")
            if is_syntax_correct(code):
                print("Syntax is correct.")
                if execute_code(code):
                    print("Code executed successfully.")
                    break
                else:
                    print("Execution failed. Regenerating code.")
            else:
                print("Syntax is incorrect. Regenerating code.")

if __name__ == "__main__":
    main()
