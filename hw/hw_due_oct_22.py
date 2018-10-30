'''
Created on Oct 20, 2018

@author: cdleong
'''
import matplotlib.pyplot as plt
import numpy as np
import math

def calculate_image_distance(focal_length_cm, object_distance_cm):
    one_over_focal_distance = 1.0/focal_length_cm
    one_over_object_distance = 1.0/object_distance_cm    
    image_distance_cm = 1.0/((one_over_focal_distance) - (one_over_object_distance))
    return image_distance_cm
    

def calculate_image_distances(object_distances_cm, focal_length_cm, very_close=0.00001):
    image_distances_cm = []
    for object_distance_cm in object_distances_cm:
        image_distance_cm = 0
        try:

            
            image_distance_cm = calculate_image_distance(focal_length_cm, object_distance_cm)
        except ZeroDivisionError:
            print("Object distance equal to focal length. Undefined.")
            # this won't work, because if they're coming from the right side it goes to plus infinity, 
            # and from the left, minus infinity 
#             image_distance_cm = calculate_image_distance(focal_length_cm, object_distance_cm-very_small_value) 
            
        print("for object distance {0}, image distance is {1}".format(object_distance_cm, image_distance_cm))
        image_distances_cm.append(image_distance_cm)
    return image_distances_cm

def plot_image_distances(object_distances_cm, 
                         image_distances, 
                         title = "image_distance (cm)",
                         xlabel="obj dist (cm)", 
                         ylabel="image dist (cm)",
                         plot_type="plot",
                         markers=None):
    plt.figure()
    
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.plot(object_distances_cm, image_distances)
    if plot_type == "semilogy":
        plt.yscale('symlog')
    plt.title(title)
    
    if markers:
        for marker in markers:
            if marker > object_distances_cm[0] and marker < object_distances_cm[-1]:
                plt.axvline(x=marker, color='r', linestyle='--')
        
    


def calculate_and_graph(focal_length_cm, problem_object_distances_cm, min_od, max_od, step):
    object_distances_cm = np.arange(min_od, max_od, step)
    image_distances_cm = calculate_image_distances(object_distances_cm, focal_length_cm)
    title = f"image distance (cm), object distance {min_od} to {max_od} cm"
    plot_image_distances(object_distances_cm, image_distances_cm, title=title, markers=problem_object_distances_cm)
    plot_image_distances(object_distances_cm, image_distances_cm, title="semilog " + title, plot_type="semilogy", markers=problem_object_distances_cm)

def ix_2():
    focal_length_cm = 50
    object_distances_cm = np.arange(49.9, 50.1, 0.001)
    object_distances_cm = [25.0, 50.0, 100.0, 200.0, 500.0]
    problem_object_distances_cm = [25.0, 100.0, 200.0, 500.0]
    
    
    min_od = 0.0
    max_od = 49.9
    step = 0.001
    calculate_and_graph(focal_length_cm, problem_object_distances_cm, min_od, max_od, step)  
    
    
    
    min_od = 50.1
    max_od = 100.0
    
    calculate_and_graph(focal_length_cm, problem_object_distances_cm, min_od, max_od, step)  

    
    min_od = 50.1
    max_od = 500.1
    
    calculate_and_graph(focal_length_cm, problem_object_distances_cm, min_od, max_od, step)  
    
    
    min_od = 50.1
    max_od = 100000.0
    step = 100.0
    calculate_and_graph(focal_length_cm, problem_object_distances_cm, min_od, max_od, step)    
    
    
    

def viii_12():
    
    min, max = 0, 11
    x_values = np.arange(min, max, 1.0)    
    y_values = [math.e**x for x in x_values]
    
    plt.figure() 
    plt.title("semilogy plot of e**x")
    plt.semilogy(x_values, y_values)
    plt.yscale('log', basey=math.e)
    plt.grid(True)
    plt.xticks(x_values)
    plt.yticks(y_values)
    
    plt.figure() 
    plt.title("loglog plot of e**x")
    plt.plot(x_values, y_values)
    
    
    
    
    x_over_ten_x_ratios = []
    ten_x_over_x_ratios = []
    for x_val in x_values:
        exp = math.e**x_val
        exp_10 = math.e**(x_val*10)
        x_over_ten_x_ratios.append(exp/exp_10)
        
        ten_x_over_x_ratios.append(exp_10/exp)
    
    plt.figure() 
    plt.title("semilogy plot of e^x/e^10x ratios")
    plt.semilogy(x_values, x_over_ten_x_ratios)
    plt.yscale('log', basey=math.e)
    plt.grid(True)
    plt.xticks(x_values)
    plt.yticks(x_over_ten_x_ratios)
    
    
    plt.figure() 
    plt.title("plot of e^x/e^10x, base 10")
    plt.plot(x_values, x_over_ten_x_ratios)
    plt.yscale('log')
    plt.grid(True)
    plt.xticks(x_values)
#     plt.yticks(x_over_ten_x_ratios)
    
    
    plt.figure() 
    plt.title("semilogy plot of e^10x/e^x")
    plt.semilogy(x_values, ten_x_over_x_ratios)
    plt.yscale('log', basey=math.e)
    plt.grid(True)
    plt.xticks(x_values)
    plt.yticks(ten_x_over_x_ratios)
    print(f"math.e: {math.e}")
    for x, y, ratio, other_ratio in zip(x_values, y_values, x_over_ten_x_ratios, ten_x_over_x_ratios):
        print(f"{x}, {y}, e^x/e^10x: {ratio}, e^10x/e^x: {other_ratio}")
    
    
        
    

if __name__ == '__main__':
    viii_12()
#     ix_2()
    plt.show()