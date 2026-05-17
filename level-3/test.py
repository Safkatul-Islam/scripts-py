# A dataset of transactions comes in as a list of strings:
raw = [
    "Alice,250.5,2024-01-15",
    "Bob,abc,2024-01-16",       # corrupted amount
    "Carol,410.0,2024-01-17",
    "Dan,,2024-01-18",           # missing amount
    "Eve,188.75,2024-01-19"
]

# Write a function parse_transactions(data) that:
# (a) Parses each line into a dict: {"name": ..., "amount": ..., "date": ...}
# (b) Skips any row where amount can't be converted to a float — using try/except
# (c) Returns a list of only the valid transaction dicts
# Bonus: Also return the count of skipped rows alongside the valid list (as a tuple)

def parse_transactions(data: list[str]) -> tuple[list[dict], int]:
    valid = []
    skipped = 0

    for row in data:
        try:
            name, amount, date = row.split(",")
            amount = float(amount)
            valid.append({
                "name": name,
                "amount": amount,
                "date": date
            })
        except (ValueError, TypeError):
            skipped += 1

    return valid, skipped

print(parse_transactions(raw))