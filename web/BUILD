python_sources()

docker_environment(
    name="python_linux",
    platform="linux_arm64", # Seems like the correct platform?
    image="python:3.10.13-bookworm",
    python_bootstrap_search_path=["<PATH>"]
)

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