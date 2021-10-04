FROM ubuntu:18.04

WORKDIR /giunners-app

RUN apt-get update
RUN apt-get install sudo

RUN sudo apt-get install -y software-properties-common
RUN sudo apt-get update

RUN sudo add-apt-repository ppa:openkim/latest
RUN sudo add-apt-repository ppa:gladky-anton/lammps
RUN sudo apt-get update

# Install LAMMPS
#CMD echo grep ^ /etc/apt/sources.list /etc/apt/sources.list.d/*
RUN sudo apt-cache search lammps
RUN sudo apt-get install -y lammps

RUN sudo add-apt-repository ppa:deadsnakes/ppa
RUN sudo apt update
RUN sudo apt install -y python3.8

# Copy app folder into image
COPY ./app ./app

# Change permissions
RUN cd app; chmod +x main.py
RUN cd app/gui; chmod +x gui.py
RUN cd app/gui; chmod +x run_am.py

RUN apt-get install -y python3.8-tk
# Install X Virtual Frame Buffer
RUN apt-get install -y xvfb
RUN apt install -y ghostscript python3-tk
#CMD dpkg-query -L python3-tk; dpkg-query -L python3.8 

#CMD cd app; ls -l; cd gui; ls -l 
#CMD ["python3.8", "./app/main.py"]
ENTRYPOINT [ "python3.8", "./app/main.py"]