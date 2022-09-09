from flask import Flask, Request, request

from mlsgrid.service import pipeline_service
from analytics.service import analytics_service
from analytics.template import routes as analytics_routes

app = Flask(__name__)


@app.route("/sync", methods=["POST"])
def pipeline_controller():
    request_json = request.get_json(silent=True)

    data = request_json if request_json else {}

    output_rows = pipeline_service(
        data.get("start"),
        data.get("end"),
    )
    return {"result": output_rows}


@app.route("/analytics/<page>/<route>")
def analytics_controller(page, route):
    return analytics_service(request.args, analytics_routes[page][route])


def main(request: Request):
    print(request)

    request_json = request.get_json(silent=True)

    internal_ctx = app.test_request_context(
        path=request.full_path,
        method=request.method,
        json=request_json if request_json else {},
    )
    internal_ctx.request = request
    internal_ctx.push()
    response = app.full_dispatch_request()
    internal_ctx.pop()

    print(response)
    return response
