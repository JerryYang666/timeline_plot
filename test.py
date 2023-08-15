import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
sub_categories = ['Subcategory 1', 'Subcategory 2', 'Subcategory 3']
sub_sub_categories = ['Sub-Subcategory A', 'Sub-Subcategory B']
values = [
    [[10, 5], [5, 5], [3, 2]],
    [[20, 10], [5, 5], [3, 2]],
    [[8, 2], [2, 1], [3, 2]],
    [[15, 5], [5, 5], [3, 2]]
]

# Specify colors for sub-categories
sub_category_colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Create a horizontal bar chart using broken_barh
plt.figure(figsize=(10, 8))
sns.set(style="whitegrid")  # Set the style of the plot

# Adjust spacing parameters
bar_height = 0.4  # Height of each sub-sub-bar
sub_category_spacing = 0.2  # Spacing between sub-categories
sub_sub_category_spacing = 0.05  # Spacing between sub-sub-categories
category_spacing = 1.0  # Spacing between categories

# Create a subplot
ax = plt.subplot()

# Plot the broken horizontal bars within each sub-category
for i, category in enumerate(categories):
    category_position = i * (len(sub_categories) * (bar_height + sub_category_spacing) + category_spacing)
    for j, sub_category in enumerate(sub_categories):
        sub_values = values[i][j]
        sub_cat_sub_positions = [category_position + j * (bar_height + sub_sub_category_spacing)]
        sub_bar_lengths = [value for value in sub_values]
        ax.broken_barh([(0, sub_bar_lengths[0]), (1, sub_bar_lengths[1])],
                       sub_cat_sub_positions,
                       height=bar_height,
                       label=sub_sub_categories[j],
                       color=sub_category_colors[j])
        category_position += bar_height + sub_sub_category_spacing

# Adjust y-axis ticks and labels
ax.set_yticks([(i * (len(sub_categories) * (bar_height + sub_category_spacing)) +
                (len(sub_categories) - 1) * sub_category_spacing) / 2
               for i in range(len(categories))])
ax.set_yticklabels(categories)

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart with Broken Horizontal Bars')

# Move the legend to the outside of the plot
ax.legend(title='Sub-Subcategories', loc='upper left', bbox_to_anchor=(1.0, 1.0))

# Invert y-axis to align with the category names
plt.gca().invert_yaxis()

# Show the plot
plt.show()
