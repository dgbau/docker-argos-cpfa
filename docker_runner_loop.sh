#!/bin/bash

for i in {1..30}
do
   docker run --rm -v $PWD/scripts:/scripts -it argos-cpfa:v1 bash \
    -c "python3 /scripts/runner.py \
    -ProbabilityOfSwitchingToSearching 0.695 \
    -ProbabilityOfReturningToNest 0.00029 \
    -UninformedSearchVariation 1.9 \
    -RateOfInformedSearchDecay 1.0 \
    -RateOfSiteFidelity 2.9 \
    -RateOfLayingPheromone 3.9 \
    -RateOfPheromoneDecay 10500 \
    -FoodDistribution 2 \
    -PrintFinalScore 1"
done