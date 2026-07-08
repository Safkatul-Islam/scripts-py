# You have a CSV-like text block representing sales data:
sales_data = """region,product,revenue
North,Widget,1200
South,Gadget,850
North,Gadget,950
East,Widget,1100
South,Widget,700
East,Gadget,1300
North,Widget,800
"""

# Without using any libraries, write code that:
# (a) Parses the data into a list of dicts (first row = headers)
# (b) Calculates total revenue per region and stores it in a dict
# (c) Prints the region with the highest total revenue
# (d) Bonus: Calculate total revenue per product as well, in a second dict

# ------Normal Manual version--------
def parse_sales_data(data:str):
    # (a) Parses the data into a list of dicts
    lines = data.splitlines()
    headers = lines[0].split(",")

    records = []
    for line in lines[1::]:
        values = line.split(",")
        record = dict(zip(headers,values))
        records.append(record)

    # (b) Calculates total revenue per region and stores it in a dict
    total_revenue_region = {}
    for record in records:
        region = record['region']
        revenue = int(record['revenue'])

        total_revenue_region[region] = total_revenue_region.get(region, 0) + revenue

    # (c) Prints the region with the highest total revenue
    # highest_revenue = 0
    # for region, revenue in total_revenue_region.items():
    #     if revenue > highest_revenue:
    #         highest_revenue = revenue

    max_region = max(total_revenue_region, key=total_revenue_region.get)
    print(f"Highest total revenue region: {max_region}")

    # for key in total_revenue_region:
    #     if total_revenue_region.get(key) == highest_revenue:
    #         print(f"Highest total revenue region: {key}")

    # (d) Bonus: Calculate total revenue per product as well, in a second dict
    total_revenue_product = {}
    for record in records:
        product = record['product']
        revenue = int(record['revenue'])

        total_revenue_product[product] = total_revenue_product.get(product, 0) + revenue

    return records, total_revenue_region, total_revenue_product


# ------Robust version--------
def parse_data(data:str):
    # (a) Parses the data into a list of dicts
    lines = data.strip().splitlines()
    if not lines:
        return [], {}, {}

    headers = [h.strip() for h in lines[0].split(",")]

    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        if len(values) != len(headers):
            continue
        record = dict(zip(headers, values))
        records.append(record)

    # (b) total revenue per region
    total_revenue_region = {}
    for record in records:
        region = record['region']
        try:
            revenue = float(record['revenue'])
        except ValueError:
            continue

        total_revenue_region[region] = total_revenue_region.get(region, 0) + revenue

    # (c) print region with highest revenue
    if total_revenue_region:
        max_region = max(total_revenue_region, key=total_revenue_region.get)
        print(f"Highest total revenue region: {max_region}")

    # (d) total revenue per product
    total_revenue_product = {}
    for record in records:
        product = record['product']
        try:
            revenue = float(record['revenue'])
        except ValueError:
            continue

        total_revenue_product[product] = total_revenue_product.get(product, 0) + revenue

    return records, total_revenue_region, total_revenue_product


if __name__ == "__main__":
    records, region_total, product_total = parse_data(sales_data)
    print(f"Region totals: {region_total}")
    print(f"Product totals: {product_total}")





