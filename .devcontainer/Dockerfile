# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.134.0/containers/python-3/.devcontainer/base.Dockerfile
ARG VARIANT="3"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Optional] Allow the vscode user to pip install globally w/o sudo
#ENV PIP_TARGET=/usr/local/pip-global
#ENV PYTHONPATH=${PIP_TARGET}:${PYTHONPATH}
#ENV PATH=${PIP_TARGET}/bin:${PATH}
#RUN mkdir -p ${PIP_TARGET} \
#    && chown vscode:root ${PIP_TARGET} \
#    && echo "if [ \"\$(stat -c '%U' ${PIP_TARGET})\" != \"vscode\" ]; then chown -R vscode:root ${PIP_TARGET}; fi" \
#        | tee -a /root/.bashrc /home/vscode/.bashrc /root/.zshrc >> /home/vscode/.zshrc

# install chrome
#RUN  apt-get update \
#     && apt-get install -y wget --no-install-recommends \
#     && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
#     && apt-get update \
#     && apt-get install -y google-chrome-stable

# install aws cli version 2 with credential aws
#RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
#    && unzip awscliv2.zip \
#    && ./aws/install -i /usr/local/aws-cli -b /usr/local/bin \
#    && mkdir /home/vscode/.aws \
#    && echo '[default]\n\
#region = eu-west-3\n'\
#>> /home/vscode/.aws/config \
#    && echo '[default]\n\
#aws_access_key_id = localstack\n\
#aws_secret_access_key = localstack\n' \
#>> /home/vscode/.aws/credentials \
#    && chown -R vscode:vscode /home/vscode/.aws
