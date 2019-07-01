# Dockerized Argos Sim
## Install docker on your system (not tested with Windows)
Follow these instructions to install Docker on your system
https://docs.docker.com/install/

## To Build from Dockerfile (if you want to modify source)
### Clone this repo
#### Download the .deb for ARGoS here:
https://drive.google.com/file/d/1VGDogC8tBipOv2kykJH4hsckXoBRKmFa/view
#### place the .deb in the repo root, and run
```docker build -t <choose-name>:<choose-tag> .```

## To pull from Docker Hub
run the following command:
```docker pull dbitz/argos-cpfa:v1```

## To Run the image:

### Setting params