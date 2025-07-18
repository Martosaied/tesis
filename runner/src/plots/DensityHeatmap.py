import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from src.math.Density import Density

class DensityHeatmap: 
    """
    Plot a density heatmap of the simulation.

    The density heatmap is a heatmap that shows the density of the pedestrians in the simulation.
    """
    def __init__(self, solution_file, output_dir):
        self.solution_file = solution_file
        self.output_dir = output_dir


    def plot(self, title = 'Density Heatmap'):
        df = pd.read_csv(self.solution_file)
        particles = (len(df.columns) - 1) / 5
        right_pedestrian_counts, left_pedestrian_counts = Density(map_size=50, grid_size=200).calculate_pedestrian_counts(df, particles)

        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
        
        # Plot right-moving pedestrians heatmap
        im1 = ax1.imshow(right_pedestrian_counts, cmap='Reds', interpolation='nearest', vmin=0, vmax=0.1)
        ax1.set_title(f'{title} - Right-Moving Pedestrians', fontsize=16)
        ax1.set_xlabel('X Position', fontsize=14)
        ax1.set_ylabel('Y Position', fontsize=14)
        ax1.grid(True, which='both', color='white', linewidth=0.5)
        plt.colorbar(im1, ax=ax1, label='Number of pedestrians')
        
        # Plot left-moving pedestrians heatmap
        im2 = ax2.imshow(left_pedestrian_counts, cmap='Blues', interpolation='nearest', vmin=0, vmax=0.1)
        ax2.set_title(f'{title} - Left-Moving Pedestrians', fontsize=16)
        ax2.set_xlabel('X Position', fontsize=14)
        ax2.set_ylabel('Y Position', fontsize=14)
        ax2.grid(True, which='both', color='white', linewidth=0.5)
        plt.colorbar(im2, ax=ax2, label='Number of pedestrians')
        
        # Adjust layout and save
        plt.suptitle('Pedestrian Density Heatmaps by Direction', fontsize=20, y=1.05)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, f'{title}_pedestrian_heatmaps_by_direction.png'), dpi=300, bbox_inches='tight')
        plt.close()