# Dockerized Argos Sim
## Install docker on your system (not tested with Windows)
Follow these instructions to install Docker on your system
https://docs.docker.com/install/

## To pull from Docker Hub (Reccomended Method)
run the following command:
```docker pull dbitz/argos-cpfa:v1```

## To Build from Dockerfile (if you want to modify the container)
### Clone this repo
#### Download the .deb for ARGoS here:
https://drive.google.com/file/d/1VGDogC8tBipOv2kykJH4hsckXoBRKmFa/view
#### place the .deb in the repo root, and run
```docker build -t <choose-name>:<choose-tag> .```



## To Run the image:
This is an example for a container execution. the --rm flag will remove the container after execution is complete. 
* Note, if you built your own image you must supply that name instead of dbitz/argos-cpfa:v1
### Setting params
A listing of accepted parameter ranges coming soon..
### Running Container
```bash
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
```

