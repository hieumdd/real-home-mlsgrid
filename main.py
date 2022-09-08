from flask import Flask, Request, request

from mlsgrid.service import pipeline_service
from analytics.service import analytics_service
from analytics.template import routes as analytics_routes

app = Flask(__name__)


@app.post("/sync")
def pipeline_controller():
    data = request.get_json()

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

    internal_ctx = app.test_request_context(
        path=request.full_path,
        method=request.method,
    )
    internal_ctx.request = request
    internal_ctx.push()
    response = app.full_dispatch_request()
    internal_ctx.pop()

    print(response)
    return response
