python_sources()

pex_binary(
    name="server",
    script="gunicorn",
    args=["web.server:app"],
    dependencies=["main_lib/component.py", "//:reqs#gunicorn", "web/server.py"],
)

docker_image(
    name="server_image",
)