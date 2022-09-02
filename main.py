from flask import Flask, Request, request

from mlsgrid.service import pipeline_service

app = Flask("internal")


@app.route("/sync")
def pipeline_controller():
    data = request.get_json()

    return pipeline_service(
        data.get("start"),
        data.get("end"),
    )


@app.route("/analytics")
def analytics_controller():
    return 200


def main(request: Request):
    print(request)

    ctx = app.test_request_context(path=request.path, data=request.data)
    ctx.push()

    response = app.full_dispatch_request()

    ctx.pop()

    print(response)

    return {"response": response}
