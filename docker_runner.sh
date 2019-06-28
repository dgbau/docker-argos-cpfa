#!/bin/bash
echo hello
docker run -v \
/Users/everyday/UNM/CS_Moses/argos_docker/scripts:/sim/scripts \
-it argos-cpfa:v0 bash \
-c  " \
cd /sim && \
./buildtest.py && \
python3 /sim/scripts/runner.py \
-ProbabilityOfSwitchingToSearching 1 \
-ProbabilityOfReturningToNest 0.002 \
-UninformedSearchVariation 6.0 \
-RateOfInformedSearchDecay 0.58 \
-RateOfSiteFidelity 4.0 \
-RateOfLayingPheromone 3.5 \
-RateOfPheromoneDecay 0.08 \
-PrintFinalScore 1"
