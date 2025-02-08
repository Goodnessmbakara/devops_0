from flask import Blueprint, request, jsonify
from app.utils import (
    is_prime,
    is_perfect,
    get_digit_sum,
    get_number_properties,
    get_fun_fact,
)

main = Blueprint("main", __name__)


@main.route("/api/classify-number", methods=["GET"])
def classify_number():
    try:
        number = request.args.get("number")
        if not number:
            return (
                jsonify(
                    {
                        "number": None,
                        "error": True,
                        "message": "Number parameter is required",
                    }
                ),
                400,
            )

        number = int(number)

        return (
            jsonify(
                {
                    "number": number,
                    "is_prime": is_prime(number),
                    "is_perfect": is_perfect(number),
                    "properties": get_number_properties(number),
                    "digit_sum": get_digit_sum(number),
                    "fun_fact": get_fun_fact(number),
                }
            ),
            200,
        )

    except ValueError:
        return (
            jsonify(
                {
                    "number": request.args.get("number"),
                    "error": True,
                    "message": "Invalid number format",
                }
            ),
            400,
        )
