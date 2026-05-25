# CS1Graphics Library

## Overview
The **cs1graphics** library is a Python module developed for introductory programming courses, particularly at **KAIST (Korea Advanced Institute of Science and Technology)**. It provides a simple and intuitive way to create graphical applications, animations, and interactive programs using Python.

## Features
- **Easy-to-use API**: Designed for beginners, with functions to create shapes (e.g., rectangles, circles, polygons) and manipulate them on a canvas.
- **Canvas-based**: Supports a `Canvas` class for drawing and organizing graphical objects.
- **Double Buffering**: Includes support for smooth animations and graphics rendering.
- **Built on Tkinter**: Leverages the Tkinter library for its underlying graphics operations.

## Installation
To use `cs1graphics`, ensure you have Python installed. The library is typically provided as part of course materials for KAIST's CS101 or similar introductory programming classes.

## Usage Example
```python
from cs1graphics import *

# Create a canvas
canvas = Canvas(800, 600, "white", "My Graphics")

# Draw a rectangle
rect = Rectangle(100, 50)
rect.setFillColor("blue")
rect.moveTo(100, 100)
canvas.add(rect)
