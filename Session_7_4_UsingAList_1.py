week_1_sales = [532.15, 775.43, 613.26, 439.76, 541.78]
week_2_sales = [621.50, 893.75, 458.92, 772.29, 386.47]
week_3_sales = [928.61, 513.78, 674.22, 785.95, 492.13]
week_4_sales = [559.82, 726.47, 386.77, 921.63, 647.94]

# Find the largest sale
total_sales = [week_1_sales, week_2_sales, week_3_sales, week_4_sales]
largest_sale = 0
for week_sales in total_sales:
        if (largest_sale < max(week_sales)):
            largest_sale = max(week_sales)

print(f"The largest sale was ${largest_sale}.")
