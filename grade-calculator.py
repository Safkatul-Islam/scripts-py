
def get_grade(grades):
    if not grades:
        return "No grades provided!"

    average = sum(grades) / len(grades)

    if average > 100:
        return "Invalid grade!"
    elif average >= 90:
        return f"A (average: {average:.2f})"
    elif average >= 80:
        return f"B+ (average: {average:.2f})"
    elif average >= 70:
        return f"B (average: {average:.2f})"
    elif average >= 60:
        return f"C (average: {average:.2f})"
    else:
        return f"F (average: {average:.2f})"


print(get_grade([85, 92, 78, 95, 60]))   # B+ (average: 82.00)
print(get_grade([45, 52, 38]))            # F (average: 45.00)
print(get_grade([]))                      # No grades provided!
print(get_grade([110, 125, 130]))         # Invalid grade!