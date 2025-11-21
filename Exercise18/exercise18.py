import matplotlib.pyplot as plt
import numpy as np

def plot_Ex18():
    
    x = np.arange(0.1 * np.pi, 2 * np.pi, 0.1)
    
    # Compute y = sin(x) for the function
    y = np.sin(x)
    
    # Default plot
    plt.figure()
    plt.plot(x, y)  
    plt.title('Default Plot')
    plt.legend(['sin(x)'])  
    plt.show()
    
    # Dotted line and color 
    plt.figure()
    plt.plot(x, y, ':', color='#1122FF')  
    plt.title('Dotted Plot')
    plt.legend(['sin(x)']) 
    plt.show()

    # Square markers and dashed green line with RGB color (0.1, 0.6, 0.1)
    plt.figure()
    plt.plot(x, y, '--', color=(0.1, 0.6, 0.1), marker='s')  
    plt.title('Square Plot')
    plt.legend(['sin(x)'])  
    plt.show()

    # Three functions in the same figure
    # Compute the functions
    f1 = np.cos(x)  # f1(x) = cos(x)
    f2 = np.log(x)  # f2(x) = log(x)
    f3 = f1 + f2  # f3(x) = f1(x) + f2(x)
    
    plt.figure()

    # Plot f1(x) with a dotted green line with line width 3.0
    plt.plot(x, f1, ':g', linewidth=3.0, label='cos(x)')
    
    # Plot f2(x) with a dashed red line with line width 4.0
    plt.plot(x, f2, '--r', linewidth=4.0, label='log(x)')
    
    # Plot f3(x) with a solid blue line without markers
    plt.plot(x, f3, '-b', linewidth=1.0, label='cos(x) + log(x)')

    # Add a legend for each function
    plt.legend()

    # Turn on the grid
    plt.grid(True)

    # Set the x and y limits
    plt.xlim([0.1 * np.pi, 2 * np.pi])  # x limits from 0.1*pi to 2*pi
    plt.ylim([-1, 2])  # y limits from -1 to 2

    # Set x and y labels
    plt.xlabel('Location (m)')
    plt.ylabel('Displacement (m)')

    # Set figure title
    plt.title('Comparison of cos(x) and log(x) with their sum')

    # Save the figure
    plt.savefig('comparison_cos_log.png')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_Ex18()
