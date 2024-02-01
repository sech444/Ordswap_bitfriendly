FROM python:3.10.13-alpine

# Install system dependencies
RUN apk update && \
    apk add --no-cache sqlite sqlite-dev build-base gmp-dev gcc musl-dev hdf5 hdf5-dev

# Use built-in pip to access poetry
RUN pip install --upgrade pip

# Install Poetry
RUN pip install --progress-bar off "poetry==1.7.0"

# Install additional Python packages
RUN pip install ecdsa[gmpy2] blockcypher --no-cache-dir

# Try to build h5py
RUN pip wheel --no-cache-dir --use-pep517 "h5py==3.9.0"

# Set working directory
WORKDIR /app

# Copy only the necessary files
COPY pyproject.toml poetry.lock* /app/

# Project initialization
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN if [ "$INSTALL_DEV" = "true" ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi

# For development, Jupyter remote kernel, Hydrogen
ARG INSTALL_JUPYTER=false
RUN if [ "$INSTALL_JUPYTER" = "true" ] ; then pip install jupyterlab ; fi

# Copy the rest of the application
COPY . /app

# Expose the necessary port
# EXPOSE 84/tcp

# Command to run the application
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "84"]
