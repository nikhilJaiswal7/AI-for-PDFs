import re

from query_data import query_rag


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def test_monopoly_rules():
    assert query_and_validate(
        question="How much total money does a player start with in Monopoly? (Answer with the number only)",
        expected_response="$1500",
    )


def test_ticket_to_ride_rules():
    assert query_and_validate(
        question="How many points does the longest continuous train get in Ticket to Ride? (Answer with the number only)",
        expected_response="10 points",
    )


def query_and_validate(question: str, expected_response: str):
    response_text = query_rag(question)
    actual = normalize_text(response_text)
    expected = normalize_text(expected_response)

    result = actual == expected
    print(f"Question: {question}")
    print(f"Expected: {expected}")
    print(f"Actual: {actual}")

    if result:
        print("\033[92mResponse: true\033[0m")
    else:
        print("\033[91mResponse: false\033[0m")

    return result
