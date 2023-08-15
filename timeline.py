# Copyright (c) 2023.
# -*-coding:utf-8 -*-
"""
@file: timeline.py
@author: Jerry(Ruihuang)Yang
@email: rxy216@case.edu
@time: 8/13/23 15:26
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.legend_handler import HandlerLine2D


class Timeline:
    CASE_HEIGHT = 2
    NUM_OF_TRACKS = 2
    CLINICAL_SEPARATION = 4
    DESCRIPTIVE_CSV = 'data/descriptive.csv'
    TIMELINE_CSV = 'data/illness.csv'
    CLINICAL_CSV = 'data/clinical.csv'
    DAY_0_COL = 'DAY0'
    COLOR_MAP = ['crimson', 'mediumseagreen', 'purple', 'orange', 'pink', 'brown', 'gray', 'olive', 'cyan']
    SHAPE_MAP = ['x', 'v', '^', '<', '>', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']
    MIN_DATE = -62
    MAX_DATE = 31
    descriptive = None
    ax = None
    legend_handler = None
    timeline_data = None
    clinical_data = None

    def __init__(self):
        self.load_descriptive()  # Load descriptive data
        self.load_timeline()
        self.load_clinical()
        print(self.timeline_data)
        print(self.timeline_data.dtypes)
        self.timeline_data.to_csv('data/tl.csv', index=False)
        plt.figure(figsize=(22, 30))  # Set the size of the plot
        sns.set(style="white")  # Set the style of the plot
        self.ax = plt.subplot()
        self.plot_reference_line()
        self.plot()
        self.x_y_axis()
        self.title_label()
        self.post_production()
        plt.show()

    def plot(self):
        for col_name in self.timeline_data.columns:
            if col_name == self.DAY_0_COL:  # Skip the DAY0 column
                continue
            col_metadata = col_name.split('-')
            if col_metadata[0] == 'P':  # if this is a column for a point in time
                color = None
                shape = None
                if len(col_metadata) == 5:
                    color = col_metadata[3]
                    shape = col_metadata[4]
                self.plot_point(col_name, col_metadata[2], int(col_metadata[1]), color, shape)
            elif "LS" in col_metadata[0]:  # if this is a column for a line in time
                if len(col_metadata) == 5:
                    color = col_metadata[3]
                    shape = col_metadata[4]
                    end_col_name = col_metadata[0].replace('LS', 'LE') + '-' + col_metadata[1] + '-' + col_metadata[2]
                    self.plot_line(col_name, end_col_name, col_metadata[2], int(col_metadata[1]), color, shape)
                else:
                    raise Exception("Line in time must have specified color and shape")
        self.plot_clinical()
        return

        self.ax.broken_barh([(-1, 2), (3, 3)], (5, -0.1), facecolors='skyblue', label='Sub-Subcategory A')
        self.ax.broken_barh([(-1, 2), (3, 3)], (2, -0.1), facecolors='skyblue', label='Sub-Subcategory A')
        self.ax.scatter([6], [4.96], color='black', zorder=1, marker='x', s=100, linewidth=3)
        self.ax.scatter([0], [0], color='mediumseagreen', zorder=1, marker='x', s=100, linewidth=3)
        self.ax.plot([1, 3], [4.96, 4.96], color='black', zorder=1, linestyle='dashed', linewidth=4, dashes=(0.5, 0.5),
                     label='Sub-Subcategory B')
        self.legend_handler, = self.ax.plot([1, 3], [4.96, 4.96], color='black', zorder=1, linewidth=2,
                                            label='Sub-Subcategory C', marker='D', mfc='white')
        return

    def plot_clinical(self):
        for i in range(len(self.clinical_data)):
            for j in range(1, len(self.clinical_data.columns)):
                if self.clinical_data.iloc[i, j] == 1:
                    self.ax.scatter(self.MAX_DATE + j * self.CLINICAL_SEPARATION, i * self.CASE_HEIGHT + self.CASE_HEIGHT / 2, color='mediumseagreen',
                                    zorder=1, marker='o', s=300, linewidth=3)
                elif self.clinical_data.iloc[i, j] == 0:
                    self.ax.scatter(self.MAX_DATE + j * self.CLINICAL_SEPARATION, i * self.CASE_HEIGHT + self.CASE_HEIGHT / 2, color='crimson',
                                    zorder=1, marker='o', s=300, linewidth=3)
                else:
                    self.ax.scatter(self.MAX_DATE + j * self.CLINICAL_SEPARATION, i * self.CASE_HEIGHT + self.CASE_HEIGHT / 2, color='gray',
                                    zorder=1, marker='o', s=300, linewidth=3)
        for i, txt in enumerate(self.clinical_data.columns[1:]):
            self.ax.text(self.MAX_DATE + (i+0.9) * self.CLINICAL_SEPARATION, -1, txt, size=15, rotation=45)
        return

    def plot_line(self, start_col_name, end_col_name, legend_name, track, color, shape):
        for i in range(0, len(self.timeline_data[start_col_name])):
            if track == 0:
                self.plot_background_line(start_col_name, end_col_name, i, legend_name, track, color)
            elif shape == 'solid':
                self.plot_solid_line(start_col_name, end_col_name, i, legend_name, track, color)
            elif shape == 'dashed':
                self.plot_dashed_line(start_col_name, end_col_name, i, legend_name, track, color)

    def plot_solid_line(self, start_col_name, end_col_name, i, legend_name, track, color):
        if i != 0:
            legend_name = None
        line, = self.ax.plot([self.timeline_data[start_col_name][i], self.timeline_data[end_col_name][i]],
                             [self.timeline_data.index[i] * self.CASE_HEIGHT + track * self.CASE_HEIGHT / (
                                     self.NUM_OF_TRACKS + 1),
                              self.timeline_data.index[i] * self.CASE_HEIGHT + track * self.CASE_HEIGHT / (
                                      self.NUM_OF_TRACKS + 1)],
                             color=color, zorder=0.9, linestyle="solid", linewidth=8,
                             label=legend_name, solid_joinstyle='miter')
        line.set_solid_capstyle('butt')

    def plot_dashed_line(self, start_col_name, end_col_name, i, legend_name, track, color):
        if i != 0:
            legend_name = None
        self.ax.plot([self.timeline_data[start_col_name][i], self.timeline_data[end_col_name][i]],
                     [self.timeline_data.index[i] * self.CASE_HEIGHT + track * self.CASE_HEIGHT / (
                             self.NUM_OF_TRACKS + 1),
                      self.timeline_data.index[i] * self.CASE_HEIGHT + track * self.CASE_HEIGHT / (
                              self.NUM_OF_TRACKS + 1)],
                     color=color, zorder=0.9, linestyle="dashed", linewidth=8, dashes=(0.3, 0.3),
                     label=legend_name)

    def plot_background_line(self, start_col_name, end_col_name, i, legend_name, track, color):
        if i != 0:
            legend_name = None
        self.ax.broken_barh([(self.timeline_data[start_col_name][i],
                              self.timeline_data[end_col_name][i] - self.timeline_data[start_col_name][i])],
                            (self.timeline_data.index[i] * self.CASE_HEIGHT + self.CASE_HEIGHT - 0.1,
                             0.2 - self.CASE_HEIGHT),
                            facecolors=color, zorder=0.85, label=legend_name, alpha=0.35)

    def plot_point(self, col_name, legend_name, track, color=None, shape=None):
        if color is None:
            color = self.COLOR_MAP[0]
            self.COLOR_MAP.pop(0)
        if shape is None:
            shape = self.SHAPE_MAP[0]
            self.SHAPE_MAP.pop(0)
        self.ax.scatter(self.timeline_data[col_name],
                        self.timeline_data.index * self.CASE_HEIGHT + track * self.CASE_HEIGHT / (
                                self.NUM_OF_TRACKS + 1),
                        color=color, zorder=1, marker=shape, s=100, linewidth=3, label=legend_name)
        return

    def x_y_axis(self):
        # Adjust y-axis ticks and labels
        self.ax.set_yticks([i * self.CASE_HEIGHT + 1 for i in range(len(self.descriptive))])
        self.ax.set_yticklabels(self.descriptive, size=15)

        # Adjust x-axis ticks and labels
        self.ax.set_xticks(np.arange(self.MIN_DATE, self.MAX_DATE, 2))
        self.ax.set_xticklabels(np.arange(self.MIN_DATE, self.MAX_DATE, 2), size=15)
        # adjust the x-axis position
        #self.ax.xaxis.set_ticks_position('top')
        self.ax.xaxis.set_label_position('top')
        self.ax.tick_params(axis='x', which='both', labelbottom=False, labeltop=True, bottom=False, top=True, labelsize=15, pad=0)
        self.ax.tick_params(axis='y', which='both', labelleft=True, labelright=False, left=False, right=False, labelsize=15, pad=-50)

        return

    def title_label(self):
        # Adding labels and title
        plt.xlabel('Days', size=15)
        plt.title('Patient timeline', size=15)
        return

    def plot_reference_line(self):
        for i in range(0, len(self.descriptive) * self.CASE_HEIGHT + 1, self.CASE_HEIGHT):
            self.ax.axhline(y=i, color='gray', linestyle='--', linewidth=1, zorder=0.8, xmax=0.98, xmin=0.04)
        self.ax.axvline(x=0, color='black', linestyle='-', linewidth=3, zorder=0.8, ymax=0.96, ymin=0.04)
        for j in range(self.MIN_DATE, self.MAX_DATE):
            if j % 5 == 0 and j != 0:
                self.ax.axvline(x=j, color='gray', linestyle='--', linewidth=1, zorder=0.8, ymax=0.96, ymin=0.04)
        return

    def post_production(self):
        # Move the legend to the outside of the plot
        self.ax.legend(title='Legend', loc='upper right', bbox_to_anchor=(1.0, 0.0),
                       handler_map={self.legend_handler: HandlerLine2D(numpoints=2)})
        # Invert y-axis to align with the category names
        plt.gca().invert_yaxis()
        # Remove the outer spines (borders)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        return

    def load_descriptive(self):
        descriptive_data = pd.read_csv(self.DESCRIPTIVE_CSV)
        patient_descriptive_list = [
            f'{descriptive_data.iloc[i, 0]} {"M" if descriptive_data.iloc[i, 2] == 1 else "F"}\n{descriptive_data.iloc[i, 4]}y BMI:{descriptive_data.iloc[i, 1]} Score:{descriptive_data.iloc[i, 5]}'
            for i in range(len(descriptive_data))]
        self.descriptive = patient_descriptive_list
        return

    def load_timeline(self):
        self.timeline_data = pd.read_csv(self.TIMELINE_CSV)
        date_format = '%Y-%m-%d'  # The format of the date in the csv file
        # convert the date column to datetime data type
        self.timeline_data[self.timeline_data.columns[1:]] = self.timeline_data[self.timeline_data.columns[1:]].apply(
            lambda col: pd.to_datetime(col, format=date_format), axis=0)
        self.calculate_date_diff()
        return

    def load_clinical(self):
        self.clinical_data = pd.read_csv(self.CLINICAL_CSV)


    def calculate_date_diff(self):
        for col in self.timeline_data.columns[1:]:
            self.timeline_data[col] = (self.timeline_data[col] - self.timeline_data[self.DAY_0_COL]).dt.days
        return


if __name__ == '__main__':
    tl = Timeline()
