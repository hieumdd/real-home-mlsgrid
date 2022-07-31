from mlsgrid.pipeline import property

pipelines = {
    i.name: i
    for i in [
        j.pipeline  # type: ignore
        for j in [
            property,
        ]
    ]
}
