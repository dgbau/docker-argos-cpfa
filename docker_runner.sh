#!/bin/bash
docker run --rm -v $PWD/scripts:/scripts -it dbitz/argos-cpfa:v1 bash \
-c "python3 /scripts/runner.py \
-ProbabilityOfSwitchingToSearching 0.40 \
-ProbabilityOfReturningToNest 0.02 \
-UninformedSearchVariation 6.0 \
-RateOfInformedSearchDecay 0.58 \
-RateOfSiteFidelity 4.0 \
-RateOfLayingPheromone 3.5 \
-RateOfPheromoneDecay 0.08 \
-FoodDistribution 0 \
-PrintFinalScore 1"