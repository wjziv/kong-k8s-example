FROM kong:2.8
USER root

# Install system deps
RUN apk update
RUN apk add python3 py3-pip python3-dev musl-dev libffi-dev gcc g++ file make

# Upgrade internal deps
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

# Copy in Python Plugins + Major Kong Dep
COPY --chown=kong --chmod=555 ./py-plugins /usr/local/kong/python-plugins
COPY --chown=kong --chmod=555 ./pluginserver.py /usr/local/bin/kong-python-pluginserver

# Install Python Plugin dependency
RUN PYTHONWARNINGS=ignore pip3 install kong-pdk==0.31

# Initialize Kong
USER kong
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 8000 8443 8001 8444
STOPSIGNAL SIGQUIT
HEALTHCHECK --interval=10s --timeout=10s --retries=10 CMD kong health
CMD ["kong", "docker-start"]
