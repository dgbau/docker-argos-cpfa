FROM ubuntu:latest
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install  tzdata -y && apt-get install sudo git g++ cmake \
libfreeimage-dev libfreeimageplus-dev qt5-default freeglut3-dev libxi-dev \
libxmu-dev liblua5.2-dev lua5.2 python3 vim -y
RUN apt install python3-pip -y
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
ADD *.deb /sim/
WORKDIR /sim/
RUN dpkg -i argos3_simulator-*.deb
RUN git clone https://github.com/BCLab-UNM/CPFA-ARGoS.git
RUN ls
RUN chmod +x ./CPFA-ARGoS/build.sh
WORKDIR /sim/CPFA-ARGoS
RUN ./build.sh
ADD *.py /sim/
RUN chmod +x /sim/*.py
RUN python3 /sim/buildtest.py
