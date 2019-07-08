from __future__ import print_function
import argparse
import os
import subprocess
import hypertune
import gcp_runner

def test(args, epoch):
    fitness_score = 0
    for trial in range(1, args.trialsPerTest + 1):
        trial_score = gcp_runner.run_trial(args)
        fitness_score += trial_score
    fitness_score /= args.trialsPerTest
    print(fitness_score)
    print('Fitness Score -> {}\n'.format(fitness_score))
    hpt = hypertune.HyperTune()
    hpt.report_hyperparameter_tuning_metric(
        hyperparameter_metric_tag='fitness_score',
        metric_value=fitness_score,
        global_step=epoch)

def get_args():
    parser = argparse.ArgumentParser(description='ARGoS CPFA Simulator')
    parser.add_argument(
        '--ProbabilityOfSwitchingToSearching',
        type=float,
        default=0.504)
    parser.add_argument(
        '--ProbabilityOfReturningToNest',
        type=float,
        default=0.001)
    parser.add_argument(
        '--UninformedSearchVariation',
        type=float,
        default=7.0)
    parser.add_argument(
        '--RateOfInformedSearchDecay',
        type=float,
        default=0.28)
    parser.add_argument(
        '--RateOfSiteFidelity',
        type=float,
        default=4.27)
    parser.add_argument(
        '--RateOfLayingPheromone',
        type=float,
        default=3.75)
    parser.add_argument(
        '--RateOfPheromoneDecay',
        type=float,
        default=0.03)
    parser.add_argument(
        '--FoodDistribution',
        type=int,
        default=1)
    parser.add_argument(
        '--PrintFinalScore',
        type=int,
        default=1)
    parser.add_argument(
        '--epochs',
        type=int,
        default=5)
    parser.add_argument(
        '--randomFoodDist',
        type=int,
        default=1)
    parser.add_argument(
        '--trialsPerTest',
        type=int,
        default=10)

    args = parser.parse_args()
    return args


def main():
    args = get_args()
    for epoch in range(1, args.epochs + 1):
        test(args, epoch)


if __name__ == '__main__':
    main()
