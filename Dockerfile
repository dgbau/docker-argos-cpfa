FROM ubuntu:latest
# Prep image dependencies and permissions
RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get install  tzdata -y && apt-get install sudo git g++ cmake \
    libfreeimage-dev libfreeimageplus-dev qt5-default freeglut3-dev libxi-dev \
    libxmu-dev liblua5.2-dev lua5.2 python vim wget -y
RUN apt install python-pip -y
RUN pip install cloudml-hypertune

# Installs google cloud sdk, this is mostly for using gsutil to export model.
RUN wget -nv \
    https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz && \
    mkdir /root/tools && \
    tar xvzf google-cloud-sdk.tar.gz -C /root/tools && \
    rm google-cloud-sdk.tar.gz && \
    /root/tools/google-cloud-sdk/install.sh --usage-reporting=false \
    --path-update=false --bash-completion=false \
    --disable-installation-options && \
    rm -rf /root/.config/* && \
    ln -s /root/.config /config && \
    # Remove the backup directory that gcloud creates
    rm -rf /root/tools/google-cloud-sdk/.install/.backup

# Path configuration
ENV PATH $PATH:/root/tools/google-cloud-sdk/bin
# Make sure gsutil will use the default service account
RUN echo '[GoogleCompute]\nservice_account = default' > /etc/boto.cfg

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

# test argos install (comment out after image is verified)
# RUN echo 'testing argos --version'
# RUN argos3 --version
# Copies the trainer code 
RUN mkdir /root/trainer
RUN mkdir /root/scripts
COPY scripts/*.py /root/trainer/
COPY scripts/config.yaml /root/trainer
# Sets up the entry point to invoke the trainer.
ENTRYPOINT ["python", "/root/trainer/argoscpfa_gcp_runner.py"]
