import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import patches


def main():
    # Sample data
    categories = ['Case #30\nF\nAge:77\nScore:3\nBMI:27.1', 'Case #32\nF\nAge:77\nScore:3\nBMI:27.1', 'Case #33\nF\nAge:77\nScore:3\nBMI:27.1', 'Case #34\nF\nAge:77\nScore:3\nBMI:27.1']

    # Create a horizontal bar chart with spaced sub-subcategories using Seaborn and Matplotlib
    plt.figure(figsize=(20, 8))
    sns.set(style="white")  # Set the style of the plot

    # Adjust spacing parameters
    bar_width = 0.4  # Width of each sub-sub-bar
    sub_category_spacing = 0.2  # Spacing between sub-categories
    sub_sub_category_spacing = 0.1  # Spacing between sub-sub-categories
    category_spacing = 0.8  # Spacing between categories

    # Create a subplot
    ax = plt.subplot()

    # Plot the spaced sub-sub-bars within each sub-category

    ax.broken_barh([(-1, 2), (3, 3)], (5, -0.1), facecolors='blue', label='Sub-Subcategory A')
    for i in range(0, 10, 2):
        ax.axhline(y=i, color='gray', linestyle='--', linewidth=1, zorder=0.8)
    ax.scatter([6], [4.96], color='black', zorder=1, marker='x', s=100, linewidth=3)
    ax.plot([1, 3], [4.96, 4.96], color='black', zorder=1, linestyle='dashed', linewidth=4, dashes=(0.5, 0.5))
    ax.axvline(x=0, color='black', linestyle='-', linewidth=3, zorder=0.8)

    # Adjust y-axis ticks and labels
    ax.set_yticks([i * 2 + 1 for i in range(len(categories))])
    ax.set_yticklabels(categories, size=15)

    # Adjust x-axis ticks and labels
    ax.set_xticks(np.arange(-4, 20, 2))
    ax.set_xticklabels(np.arange(-4, 20, 2), size=15)

    # Adding labels and title
    plt.xlabel('Days', size=15)
    plt.title('Patient timeline')

    # Move the legend to the outside of the plot
    ax.legend(title='Sub-Subcategories', loc='upper left', bbox_to_anchor=(1.0, 1.0))

    # Invert y-axis to align with the category names
    plt.gca().invert_yaxis()

    # Remove the outer spines (borders)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Show the plot
    plt.show()


if __name__ == '__main__':
    main()
