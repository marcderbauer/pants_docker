FROM python:3.10 AS base

# Copy the server.pex file into the /app directory in the Docker image
COPY web/server.pex server.pex

# Command to run the PEX file using gunicorn
CMD ["./server.pex", "-b", "0.0.0.0:8000"]