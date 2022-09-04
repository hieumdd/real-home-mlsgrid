from flask import Flask, Request, request

from mlsgrid.service import pipeline_service
from analytics.service import analytics_service
from analytics.routes import routes as analytics_routes

app = Flask(__name__)


@app.route("/sync")
def pipeline_controller():
    data = request.get_json()

    output_rows = pipeline_service(
        data.get("start"),
        data.get("end"),
    )
    return {"result": output_rows}


@app.route("/analytics/<route>")
def analytics_controller(route):
    data = request.get_json()

    if not data or route not in analytics_routes:
        return ({"error": "Bad request"}, 400)

    return analytics_service(analytics_routes[route], request)


def main(request: Request):
    print(request)

    ctx = app.test_request_context(path=request.path, data=request.data)
    ctx.push()

    response = app.full_dispatch_request()

    ctx.pop()

    print(response)

    return response
