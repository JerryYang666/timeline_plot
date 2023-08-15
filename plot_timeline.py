# Copyright (c) 2023.
# -*-coding:utf-8 -*-
"""
@file: plot_timeline.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 8/11/23 16:11
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.legend_handler import HandlerLine2D



CASE_HEIGHT = 2


def main():
    descriptive = load_descriptive()  # Load descriptive data
    plt.figure(figsize=(20, 80))  # Set the size of the plot
    sns.set(style="white") # Set the style of the plot
    ax = plt.subplot()

    ax.broken_barh([(-1, 2), (3, 3)], (5, -0.1), facecolors='blue', label='Sub-Subcategory A')
    ax.broken_barh([(-1, 2), (3, 3)], (2, -0.1), facecolors='blue', label='Sub-Subcategory A')
    for i in range(0, len(descriptive)*CASE_HEIGHT+1, CASE_HEIGHT):
        ax.axhline(y=i, color='gray', linestyle='--', linewidth=1, zorder=0.8)
    ax.scatter([6], [4.96], color='black', zorder=1, marker='x', s=100, linewidth=3)
    ax.scatter([0], [0], color='green', zorder=1, marker='x', s=100, linewidth=3)
    ax.plot([1, 3], [4.96, 4.96], color='black', zorder=1, linestyle='dashed', linewidth=4, dashes=(0.5, 0.5), label='Sub-Subcategory B')
    ale, = ax.plot([1, 3], [4.96, 4.96], color='black', zorder=1, linewidth=2,
            label='Sub-Subcategory C', marker='D', mfc='white')
    ax.axvline(x=0, color='black', linestyle='-', linewidth=3, zorder=0.8, ymax=0.96, ymin=0.04)

    # Adjust y-axis ticks and labels
    ax.set_yticks([i * 2 + 1 for i in range(len(descriptive))])
    ax.set_yticklabels(descriptive, size=15)

    # Adjust x-axis ticks and labels
    ax.set_xticks(np.arange(-4, 20, 2))
    ax.set_xticklabels(np.arange(-4, 20, 2), size=15)
    # adjust the x-axis position
    ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # Adding labels and title
    plt.xlabel('Days', size=15)
    plt.title('Patient timeline', size=15)

    # Move the legend to the outside of the plot
    ax.legend(title='Legend', loc='upper left', bbox_to_anchor=(1.0, 1.0), handler_map={ale: HandlerLine2D(numpoints=2)})

    # Invert y-axis to align with the category names
    plt.gca().invert_yaxis()

    # Remove the outer spines (borders)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Show the plot
    plt.show()

def plot_reference_line(mpl_subplot):
    pass



def load_descriptive():
    # Load descriptive data
    descriptive_data = pd.read_csv('data/descriptive.csv')
    patient_descriptive_list = [f'{descriptive_data.iloc[i, 0]}\n{"M" if descriptive_data.iloc[i, 2] == 1 else "F"}\nAge:{descriptive_data.iloc[i, 4]}\nScore:{descriptive_data.iloc[i, 5]}\nBMI:{descriptive_data.iloc[i, 1]}' for i in range(len(descriptive_data))]
    return patient_descriptive_list

if __name__ == '__main__':
    main()
