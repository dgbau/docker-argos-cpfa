#!/bin/bash


docker run --rm -v $PWD/scripts:/scripts -it argos-cpfa:v1 bash \
-c "python3 /scripts/runner.py \
-ProbabilityOfSwitchingToSearching 1.0 \
-ProbabilityOfReturningToNest 0.0 \
-UninformedSearchVariation 0.0395 \
-RateOfInformedSearchDecay 0.06925 \
-RateOfSiteFidelity 12.6571 \
-RateOfLayingPheromone 16.3573 \
-RateOfPheromoneDecay 0.30182 \
-FoodDistribution 0 \
-PrintFinalScore 1" >> output.txt