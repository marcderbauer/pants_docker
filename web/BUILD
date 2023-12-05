python_sources()

docker_environment(
    name="python_linux",
    platform="linux_arm64", # Seems like the correct platform?
    image="python:3.10.13-bookworm"
)
# -> Can't find interpreter for constraints: CPython==3.10.*
# -> Version is correct
# -> Cpython?
# -> Path issues?

pex_binary(
    name="server",
    script="gunicorn",
    args=["web.server:app"],
    dependencies=["main_lib/component.py", "//:reqs#gunicorn", "web/server.py"],
    environment="linux"
)

docker_image(
    name="server_image",
)

# 
# (venv) ➜  pants_docker git:(main) ✗ pants package web:server_image
# 17:46:11.86 [ERROR] 1 Exception encountered:
# 
# Engine traceback:
#   in `package` goal
# 
# ProcessExecutionFailure: Process 'Find interpreter for constraints: CPython==3.10.*' failed with exit code 102.
# stdout:
# 
# stderr:
# Could not find a compatible interpreter.
# 
# No interpreters could be found on the system.
# 
# 
# 
# Use `--keep-sandboxes=on_failure` to preserve the process chroot for inspection.