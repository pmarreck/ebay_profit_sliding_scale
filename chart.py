import numpy as np
import matplotlib.pyplot as plt

# Configuration variables
# Minimum percentage the seller gets (floor), even for very expensive items
MIN_SELLER_PERCENTAGE = 0.30  # 30%

# Additional percentage on top of minimum that can be earned (for cheaper items)
ADDITIONAL_PERCENTAGE = 0.35  # 35%

# Price point (in dollars) where the curve starts to significantly decline
PRICE_INFLECTION = 974.0  # This affects where the curve starts to drop more steeply

# Steepness of the curve (higher values make the transition more abrupt)
CURVE_STEEPNESS = 1.1  # Values > 1 make curve steeper, < 1 make it more gradual

# Range of values to plot
MIN_VALUE = 10  # Minimum item value to show on chart
MAX_VALUE = 10000  # Maximum item value to show on chart
NUM_POINTS = 500  # Number of points to plot (more = smoother curve)

def p(x):
    """
    Calculate the seller's percentage based on item value.
    Uses a logistic-like curve that starts high for low-value items
    and asymptotically approaches MIN_SELLER_PERCENTAGE for high-value items.
    """
    return MIN_SELLER_PERCENTAGE + ADDITIONAL_PERCENTAGE / (1 + (x/PRICE_INFLECTION)**CURVE_STEEPNESS)

# Generate a range of item values
x_values = np.linspace(MIN_VALUE, MAX_VALUE, NUM_POINTS)
percentages = p(x_values)
profits = x_values * percentages

def create_plots(show_plots=True):
    """Create the visualization plots. Returns the figure objects."""
    # Plot Percentage vs Value
    fig1 = plt.figure(figsize=(12,6))
    plt.plot(x_values, percentages * 100, label="eBay Seller's Percentage")
    plt.title("Seller's Percentage vs. Item Value")
    plt.xlabel("Item Value ($)")
    plt.ylabel("Seller's Cut (%)")
    plt.grid(True)
    plt.legend()

    # Plot Profit vs Value
    fig2 = plt.figure(figsize=(12,6))
    plt.plot(x_values, profits, label="Seller's Profit")
    plt.title("Seller's Profit vs. Item Value")
    plt.xlabel("Item Value ($)")
    plt.ylabel("Seller's Profit ($)")
    plt.grid(True)
    plt.legend()

    if show_plots:
        plt.show()
    else:
        plt.close(fig1)
        plt.close(fig2)
    
    return fig1, fig2

if __name__ == '__main__':
    create_plots(show_plots=True)
