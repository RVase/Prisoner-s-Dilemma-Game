import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load your CSV data into a Pandas DataFrame
data = pd.read_csv('data_0.1_all_runs_top_nodes.csv')

# Filter the data for the first 50 runs
runs_to_plot = range(50)
filtered_data = data[data['Run'].isin(runs_to_plot)]

# Create a single matrix visualization
fig, ax = plt.subplots(figsize=(20, 6))  # Increased figure width for more column spacing

# Define a custom color palette for aesthetics
cmap = sns.color_palette("coolwarm", as_cmap=True)

# Iterate over each run
for i, run in enumerate(runs_to_plot):
    run_data = filtered_data[filtered_data['Run'] == run]
    
    # Sort the data by degree in descending order
    run_data = run_data.sort_values(by='in_degree', ascending=True)
    
    # Calculate positions and sizes for the circles
    positions = np.full(5, i)
    vertical_positions = np.arange(5)
    
    # Adjust circle sizes
    sizes = (run_data['in_degree'] * 10) / 2
    colors = run_data['payoff']
    
    # Adjust edge colors and widths for nodes with in_degree of 99
    edge_colors = ['forestgreen' if degree == 99 else 'k' for degree in run_data['in_degree']]
    edge_widths = [2 if degree == 99 else 1 for degree in run_data['in_degree']]
    
    # Create scatter plot for each run
    scatter = ax.scatter(
        positions,
        vertical_positions,
        s=sizes,
        c=colors,
        cmap=cmap,
        vmin=filtered_data['payoff'].min(),
        vmax=filtered_data['payoff'].max(),
        edgecolor=edge_colors,
        linewidths=edge_widths,
        alpha=0.8,
    )

# Set axis labels and limits with improved styling
ax.set_xlabel('Runs', fontsize=14)
ax.set_ylabel('Nodes', fontsize=14)
ax.set_xlim(-0.5, len(runs_to_plot) - 0.5)
ax.set_xticks(range(0, len(runs_to_plot), 10))  # Set ticks every 10 runs
ax.set_xticklabels([f'Run {run}' for run in range(0, len(runs_to_plot), 10)], fontsize=12)
ax.set_yticks(range(5))
ax.set_yticklabels([])

# Add a colorbar with improved styling
cbar = plt.colorbar(scatter, label='Payoff', ax=ax, pad=0.02)
cbar.set_ticks([])

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add a title

# plt.title('Matrix Visualization of Node Degree and Payoff for 50 Runs', fontsize=16)

plt.tight_layout()

# Save the figure as a PNG
plt.savefig('matrix_visualization.png', dpi=600, bbox_inches='tight')

plt.show()
plt.show()
