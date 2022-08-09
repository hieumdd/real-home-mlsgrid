from mlsgrid.pipeline import property, property_close

pipelines = {
    i.name: i
    for i in [
        j.pipeline  # type: ignore
        for j in [
            property,
            property_close,
        ]
    ]
}
