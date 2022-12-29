FROM ubuntu:focal

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install python3 python3-venv python-is-python3 git

# checkout guild from the last commit prior to the patch that fixes this
# install it as a standalone app
RUN git clone 'https://github.com/guildai/guildai'
RUN git -C guildai checkout ef8fe41339813a1150dd280b64f2f089b341c3a4

RUN python3 -m venv /opt/guild-app
RUN /opt/guild-app/bin/python -m pip install --upgrade pip
RUN /opt/guild-app/bin/python -m pip install -e /guildai

# simulate a user project with a project specific venv
# and a simple 'Hello World' user op defined in guild.yml
ADD user-project user-project
WORKDIR user-project
RUN python3 -m venv user-project-venv

## reproduce the error
# activate the user-project-venv (that doesn't have guild), and
# attempt a batch run of the simple op
RUN /bin/bash -c \
"source user-project-venv/bin/activate && \
  /opt/guild-app/bin/guild run -y user-op x=[2,3]"


## expected output:
# Step 13/13 : RUN /bin/bash -c "source user-project-venv/bin/activate &&   /opt/guild-app/bin/guild run -y user-op x=[2,3]"
#  ---> Running in bcecc2d3a894
# WARNING: Found more than 100 source code files but will only copy 100 as a safety measure. To control which files are copied, define 'sourcecode' for the operation in a Guild file.
# Traceback (most recent call last):
#   File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
#     return _run_code(code, main_globals, None,
#   File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
#     exec(code, run_globals)
#   File "/guildai/guild/batch_main.py", line 15, in <module>
#     from guild import batch_util
#   File "/guildai/guild/batch_util.py", line 26, in <module>
#     from guild import cli
#   File "/guildai/guild/cli.py", line 22, in <module>
#     import click
# ModuleNotFoundError: No module named 'click'
# The command '/bin/sh -c /bin/bash -c "source user-project-venv/bin/activate &&   /opt/guild-app/bin/guild run -y user-op x=[2,3]"' returned a non-zero code: 1
