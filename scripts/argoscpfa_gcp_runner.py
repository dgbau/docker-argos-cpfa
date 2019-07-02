from __future__ import print_function

import argparse
import os
import subprocess
import hypertune

def test(args, epoch):
    fitness_score = 0
    correct = 0
    print('\nTest Score: {:.4f}'.format(fitness_score))
    # Uses hypertune to report metrics for hyperparameter tuning.
    hpt = hypertune.HyperTune()
    hpt.report_hyperparameter_tuning_metric(
        hyperparameter_metric_tag='fitness_score',
        metric_value=fitness_score,
        global_step=epoch)

def get_args():
    parser = argparse.ArgumentParser(description='ARGoS CPFA Simulator')
    parser.add_argument(
        '-ProbabilityOfSwitchingToSearching',
        type=float,
        default=64)
    parser.add_argument(
        '-ProbabilityOfReturningToNest',
        type=float,
        default=1000)
    parser.add_argument(
        '-UninformedSearchVariation',
        type=float,
        default=10)
    parser.add_argument(
        '-RateOfInformedSearchDecay',
        type=float,
        default=0.01)
    parser.add_argument(
        '-RateOfSiteFidelity',
        type=float,
        default=0.5)
    parser.add_argument(
        '-RateOfLayingPheromone',
        type=float,
        default=0.01)
    parser.add_argument(
        '-RateOfPheromoneDecay',
        type=float,
        default=0.01)
    parser.add_argument(
        '-FoodDistribution',
        type=int,
        default=0.01)
    parser.add_argument(
        '-PrintFinalScore',
        type=int,
        default=1)

    args = parser.parse_args()
    return args


def main():
    # Training settings
    args = get_args()
    for epoch in range(1, args.epochs + 1):
        test(args, epoch)


if __name__ == '__main__':
    main()
