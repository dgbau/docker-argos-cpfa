FROM ubuntu:latest
# Prep image dependencies and permissions
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install  tzdata -y && apt-get install sudo git g++ cmake \
libfreeimage-dev libfreeimageplus-dev qt5-default freeglut3-dev libxi-dev \
libxmu-dev liblua5.2-dev lua5.2 python3 vim -y
RUN apt install python3-pip -y
RUN pip install cloudml-hypertune

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
# Install ARGoS
ADD *.deb /
RUN dpkg -i argos3_simulator-*.deb
# Install CPFA-ARGoS
RUN git clone https://github.com/BCLab-UNM/CPFA-ARGoS.git
RUN chmod +x ./CPFA-ARGoS/build.sh
# Add experiment files and test installation
WORKDIR /CPFA-ARGoS
RUN /CPFA-ARGoS/build.sh
RUN echo 'testing argos --version'
RUN argos3 --version
