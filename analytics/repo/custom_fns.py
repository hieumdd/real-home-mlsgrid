from pypika import CustomFunction
from pypika.terms import AnalyticFunction


class PERCENTILE_CONT(AnalyticFunction):
    def __init__(self, *args, **kwargs):
        super(PERCENTILE_CONT, self).__init__("PERCENTILE_CONT", *args, **kwargs)


DATE_TRUNC = CustomFunction("DATE_TRUNC", ["date_expression", "date_part"])

MEDIAN = lambda column: PERCENTILE_CONT(column, 0.5)

DATE_DIFF = CustomFunction(
    "DATE_DIFF",
    ["date_expression", "date_expression", "date_part"],
)
