import argparse
import json
import os

from src.runner import run_experiment, compile_c_code, compile_model
from src.plotter import generate_gif, generate_grouped_directioned_graph
from src.utils import load_config, create_output_dir, copy_results_to_latest
from experiments.performance_n_pedestrians.performance_n_pedestrians import performance_n_pedestrians
from experiments.performance_n_volumes.performance_n_volumes import performance_n_volumes
from experiments.performance_n_peds_m_vols.performance_n_peds_m_vols import performance_n_peds_m_vols
from experiments.average_velocity.average_velocity import average_velocity
from experiments.lanes_by_volumes.lanes_by_volumes import lanes_by_volumes
from experiments.lanes_by_iterations.lanes_by_iterations import lanes_by_iterations
from experiments.lanes_by_width.lanes_by_width import lanes_by_width
from experiments.deltaq.deltaq import deltaq
def main():
    parser = argparse.ArgumentParser(description='Run experiments with JSON configuration')
    subparsers = parser.add_subparsers(dest='command', title='Tools', help='sub-command help')

    run_parser = subparsers.add_parser('run', description='Run experiments with JSON configuration')
    run_parser.add_argument('model', type=str, help='Name of the model to run (e.g., social_force_model)')
    run_parser.add_argument('--config', type=str, default='config.json', help='Path to JSON configuration file')
    run_parser.add_argument('--experiment-name', type=str, help='Name of the experiment (creates a subdirectory)')
    run_parser.add_argument('--compile', action='store_true', help='Compile the model before running')
    run_parser.add_argument('--compile-c', action='store_true', help='Compile the C++ code before running')
    run_parser.add_argument('--output-dir', type=str, default='results',
                            help='Base directory for experiment outputs (default: results)')
    run_parser.add_argument('--plot', action='store_true', help='Plot the results')
    
    plot_parser = subparsers.add_parser('plot', description='Plot results')
    plot_parser.add_argument('plot', type=str, help='plot type (gif, grouped_lanes)')
    plot_parser.add_argument('solution_file', type=str, help='Path to solution file')
    plot_parser.add_argument('--output-dir', type=str, default='results',
                             help='Base directory for experiment outputs (default: results)')
    plot_parser.add_argument('--config', type=str, default='config.json', help='Path to JSON configuration file')
    experiments_parser = subparsers.add_parser('experiments', description='Run experiments')
    experiments_parser.add_argument('experiment', type=str, help='Name of the experiment to run')

    args = parser.parse_args()

    if args.command == 'run':
        # Validate config file exists
        if not os.path.exists(args.config):
            raise FileNotFoundError(f"Configuration file not found: {args.config}")

        # Load configuration
        config = load_config(args.config)

        # Create output directory with experiment name if provided
        output_dir = create_output_dir(args.output_dir, args.experiment_name)
        print(f"Created output directory: {output_dir}")

        # Save config copy in experiment directory
        config_copy_path = os.path.join(output_dir, 'config.json')
        with open(config_copy_path, 'w') as f:
            json.dump(config, f, indent=2)

        # Compile the C++ code if requested
        if args.compile_c:
            compile_c_code()

        # Compile the model if requested
        if args.compile:
            compile_model(args.model)

        # Run experiment
        run_experiment(config, output_dir, args.model, plot=args.plot)

        # Copy results from output directory to latest directory
        copy_results_to_latest(output_dir)
        print(f"\nExperiment completed. Results saved in {output_dir}")
    elif args.command == 'plot':
        # Validate config file exists
        if not os.path.exists(args.config):
            raise FileNotFoundError(f"Configuration file not found: {args.config}")

        # Load configuration
        config = load_config(args.config)

        if args.plot == 'gif':
            generate_gif(args.solution_file, args.output_dir, config)
        elif args.plot == 'grouped_lanes':
            generate_grouped_directioned_graph([args.solution_file], args.output_dir)
    elif args.command == 'experiments':
        if args.experiment == 'performance_n_pedestrians':
            performance_n_pedestrians()
        elif args.experiment == 'performance_n_volumes':
            performance_n_volumes()
        elif args.experiment == 'performance_n_peds_m_vols':
            performance_n_peds_m_vols()
        elif args.experiment == 'average_velocity':
            average_velocity()
        elif args.experiment == 'lanes_by_volumes':
            lanes_by_volumes()
        elif args.experiment == 'lanes_by_iterations':
            lanes_by_iterations()
        elif args.experiment == 'lanes_by_width':
            lanes_by_width()
        elif args.experiment == 'deltaq':
            deltaq()
        else:
            print(f"Experiment {args.experiment} not found")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
