def process_data(raw_data):
    result = {"valid": [], "invalid": []}

    lines = [ln.strip() for ln in raw_data.strip().splitlines() if ln.strip()]
    rows = lines[1:]  # skip header

    for line in rows:
        parts = [p.strip() for p in line.split(",")]

        if len(parts) != 3:
            result["invalid"].append({"row": line, "reason": "wrong number of columns"})
            continue

        name, age, score = parts

        if not name:
            result["invalid"].append({"row": line, "reason": "missing name"})
            continue

        try:
            age = int(age) if age else None
        except ValueError:
            age = None

        try:
            score = float(score)  # float handles "91" and "91.5"
        except ValueError:
            result["invalid"].append({"row": line, "reason": "score not a valid number"})
            continue

        if not (0 <= score <= 100):
            result["invalid"].append({"row": line, "reason": "score out of range"})
            continue

        result["valid"].append({
            "name": name.title(),
            "age": age,
            "score": score
        })

    return result


def print_report(result, total_rows):
    print(f"Processed {total_rows} rows.")
    print(f"Valid: {len(result['valid'])} | Invalid: {len(result['invalid'])}")

    print("\nValid students:")
    for s in result["valid"]:
        print(f"  {s['name']} (age {s['age']}): {s['score']}")

    print("\nInvalid rows:")
    for bad in result["invalid"]:
        print(f'  "{bad["row"]}" -> {bad["reason"]}')


if __name__ == "__main__":
    raw_data = """
    name, age, score
    Alice, 28, 91
    Bob, , 85
    carol, 34, 72
      Dave  , 29, 150
    Eve, 22, 88
    Frank, 41, notanumber
    , 30, 77
    """

    processed = process_data(raw_data)
    print("\nReturned dictionary:")
    print(processed)
    print("\n")
    print_report(processed, raw_data)