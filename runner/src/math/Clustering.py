import numpy as np

"""
This module contains the functions to cluster the pedestrians.
"""

MIN_X_DISTANCE = 50
MIN_Y_DISTANCE = 0.5

class Clustering:
    """
    This class contains the functions to cluster the pedestrians.
    """
    def __init__(self, df, particles, min_x_distance=MIN_X_DISTANCE, min_y_distance=MIN_Y_DISTANCE):
        self.df = df
        self.particles = particles
        self.min_x_distance = min_x_distance
        self.min_y_distance = min_y_distance
    
    def distance(self, tup1, tup2):
        return abs(tup1[1] - tup2[1]) < self.min_x_distance and abs(tup1[2] - tup2[2]) < self.min_y_distance

    def unify_groups(self, particles_groups):
        # Remove duplicates
        unique_groups = {}
        for group in particles_groups:
            sorted_group = tuple(sorted(group))
            hash_id = str(hash(sorted_group))
            unique_groups[hash_id] = set(sorted_group)

        return list(unique_groups.values())

    def join_groups(self, particles_groups):
        for group in particles_groups:
            for other_group in particles_groups:
                if len(set(group) & set(other_group)) > 0:
                    group.update(other_group)

        return particles_groups

    def direct_group(self, particle, particles_list):
        particle_group = set([particle[0]])
        for other_particle in particles_list:
            if self.distance(particle, other_particle) and particle[3] == other_particle[3]:
                particle_group.add(other_particle[0])

        return particle_group

    def calculate_groups(self, from_y=0, to_y=50):
        groups = []
        for index, row in self.df.iterrows():
            # initializing list
            particles_list = [(i, row[f'PX[{i}]'], row[f'PY[{i}]'], row[f'PS[{i}]']) for i in range(1, self.particles) if row[f'PY[{i}]'] >= from_y and row[f'PY[{i}]'] <= to_y]

            particles_groups = []
            for particle in particles_list:
                particle_group = self.direct_group(particle, particles_list)
                particles_groups.append(particle_group)


            previous_group_quantity = 0
            while len(particles_groups) != previous_group_quantity:
                previous_group_quantity = len(particles_groups)
                particles_groups = self.join_groups(particles_groups)
                particles_groups = self.unify_groups(particles_groups)

            groups.append(len([group for group in particles_groups if len(group) > 3]))

        return np.mean(groups)

    def calculate_groups_by_time(self, row, from_y=0, to_y=50):
        particles_list = [(i, row[f'PX[{i}]'], row[f'PY[{i}]'], row[f'PS[{i}]']) for i in range(1, self.particles) if row[f'PY[{i}]'] >= from_y and row[f'PY[{i}]'] <= to_y]

        particles_groups = []
        for particle in particles_list:
            particle_group = self.direct_group(particle, particles_list)
            particles_groups.append(particle_group)


        previous_group_quantity = 0
        while len(particles_groups) != previous_group_quantity:
            previous_group_quantity = len(particles_groups)
            particles_groups = self.join_groups(particles_groups)
            particles_groups = self.unify_groups(particles_groups)

        return [group for group in particles_groups if len(group) > 3]