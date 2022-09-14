import math

# Approximating circle's area with rectangulars

def circle_area(radius, sections):
    b = radius/(sections + 2) # Base width of each rectangular
    area_quarter = 0 
    x = 0
    for i in range(0, sections - 1): 
        x += b 
        height = math.sqrt(radius**2 - x**2)
        area_quarter += b * height
    return 4 * area_quarter # Multiply by 4 to calculate the area of the whole circle