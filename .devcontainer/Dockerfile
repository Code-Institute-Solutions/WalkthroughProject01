FROM ubuntu:22.04

ENV PYTHON_VERSION 3.8.12
ENV DEBIAN_FRONTEND=noninteractive
#Set of all dependencies needed for pyenv to work on Ubuntu
RUN apt-get update \ 
    && apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget ca-certificates curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev mecab-ipadic-utf8 git postgresql-client telnet libpq-dev unzip

RUN curl https://cli-assets.heroku.com/install.sh | sh

ARG USERNAME=codeany
RUN useradd -ms /bin/bash $USERNAME
USER $USERNAME
WORKDIR /home/$USERNAME

# Set-up necessary Env vars for PyEnv
ENV PYENV_ROOT /home/$USERNAME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Install pyenv
RUN set -ex \
    && curl https://pyenv.run | bash \
    && pyenv update \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && pyenv rehash \
    && python3 -m pip install --no-cache-dir --upgrade pip \
    && python3 -m pip install --no-cache-dir --upgrade setuptools wheel virtualenv pipenv pylint rope flake8  mypy autopep8 pep8 pylama pydocstyle bandit notebook twine

ENV PATH=$PATH:"/home/codeany/.local/bin"

RUN echo 'alias python=python3' >> ~/.bashrc && \
    echo 'export PIP_USER=yes' >> ~/.bashrc && \
    echo 'alias pip=pip3' >> ~/.bashrc && \
    echo 'export PYENV_ROOT="/home/codeany/.pyenv"' >> ~/.bashrc && \
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc

CMD ["tail", "-f", "/dev/null"]