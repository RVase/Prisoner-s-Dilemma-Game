import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load your CSV data into a Pandas DataFrame
data = pd.read_csv('data_0.7_all_runs_top_nodes.csv')

# Filter the data for the first 5 runs
runs_to_plot = range(5)
filtered_data = data[data['Run'].isin(runs_to_plot)]

# Create a single matrix visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Define a custom color palette for aesthetics
cmap = sns.color_palette("coolwarm", as_cmap=True)

# Iterate over each run
for i, run in enumerate(runs_to_plot):
    run_data = filtered_data[filtered_data['Run'] == run]
    
    # Sort the data by degree in descending order
    run_data = run_data.sort_values(by='in_degree', ascending=False)
    
    # Calculate positions and sizes for the circles
    positions = np.full(5, i)  # Use integer run values for x-axis positions
    vertical_positions = np.arange(5)  # Vertically distribute nodes
    sizes = run_data['in_degree'] * 10
    colors = run_data['payoff']
    
    # Create scatter plot for each run
    scatter = ax.scatter(
        positions,            # x-axis positions (one column per run)
        vertical_positions,   # y-axis positions (vertically distributed)
        s=sizes,              # Circle size based on degree
        c=colors,             # Circle color based on payoff
        cmap=cmap,
        vmin=filtered_data['payoff'].min(),
        vmax=filtered_data['payoff'].max(),
        edgecolor='k',        # Add black edges for better visibility
        linewidths=1,
        alpha=0.8,            # Adjust transparency for smoother appearance
    )
    
    # # Identify nodes with in-degree 99
    # nodes_with_in_degree_99 = run_data[run_data['in_degree'] == 99]
    
    # # Create a black dot at the center of nodes with in-degree 99
    # for index, row in nodes_with_in_degree_99.iterrows():
    #     ax.scatter(
    #         positions[i],  # x-axis position (current run)
    #         vertical_positions[row.name],  # y-axis position
    #         c='k',         # Black color for the dot
    #         s=100,         # Size of the dot
    #         marker='o',    # Circular marker
    #         edgecolor='k', # Black edge for the dot
    #         zorder=3,      # Place the dot above other markers
    #     )

# Set axis labels and limits with improved styling
ax.set_xlabel('Runs', fontsize=14)
ax.set_ylabel('Nodes', fontsize=14)
ax.set_xlim(-0.5, len(runs_to_plot) - 0.5)  # Set x-axis limits to show integer values
ax.set_xticks(range(len(runs_to_plot)))  # Set x-axis ticks to integer run values
ax.set_xticklabels([f'Run {run}' for run in runs_to_plot], fontsize=12)
ax.set_yticks(range(5))
ax.set_yticklabels([])  # Hide y-axis labels for nodes

# Add a colorbar with improved styling
cbar = plt.colorbar(scatter, label='Payoff', ax=ax, pad=0.02)
cbar.set_ticks([])  # Hide colorbar ticks

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add a title
plt.title('Matrix Visualization of Node Degree and Payoff', fontsize=16)

plt.tight_layout()
plt.show()
