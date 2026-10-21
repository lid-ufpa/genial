import numpy as np
import matplotlib.pyplot as plt

def plot_quadratic(a, b, c, x_range=(-10, 10), num_points=400, show_vertex=True):
    """
    Plots a quadratic function y = ax^2 + bx + c using matplotlib.

    Parameters
    ----------
    a, b, c : float
        Coefficients of the quadratic equation.
    x_range : tuple, optional
        Range of x values (min_x, max_x). Default is (-10, 10).
    num_points : int, optional
        Number of points to plot. Default is 400.
    show_vertex : bool, optional
        If True, shows the vertex of the parabola. Default is True.
    """

    # Generate x values
    x = np.linspace(x_range[0], x_range[1], num_points)
    # Compute corresponding y values
    y = a * x**2 + b * x + c

    # Plot the curve
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"$y = {a}x^2 + {b}x + {c}$", linewidth=2)
    plt.axhline(0, color='gray', linestyle='--', linewidth=1)
    plt.axvline(0, color='gray', linestyle='--', linewidth=1)

    # Compute and show vertex
    if show_vertex and a != 0:
        xv = -b / (2 * a)
        yv = a * xv**2 + b * xv + c
        plt.scatter(xv, yv, color='red', zorder=5)
        plt.text(xv+(x_range[1]*0.1), yv, f"Zero em ({xv:.2f}, {yv:.2f})", color='darkred', fontsize=10)

    plt.title(f"Função quadrática: {a}x^2 + {b}x + {c}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
