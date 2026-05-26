import pandas as pd
import random

data = []

for i in range(3000):
    area = random.randint(600, 4000)
    bedrooms = random.randint(1, 6)
    bathrooms = random.randint(1, 5)
    age = random.randint(0, 25)
    parking = random.randint(0, 3)
    location_score = round(random.uniform(5.0, 10.0), 1)

    price = (
        area * 3500 +
        bedrooms * 500000 +
        bathrooms * 300000 +
        parking * 200000 +
        location_score * 400000 -
        age * 50000
    )

    data.append([
        area,
        bedrooms,
        bathrooms,
        age,
        parking,
        location_score,
        int(price)
    ])

df = pd.DataFrame(data, columns=[
    "Area_sqft",
    "Bedrooms",
    "Bathrooms",
    "Age_years",
    "Parking",
    "Location_Score",
    "Price"
])

df.to_csv("house_price_dataset.csv", index=False)

print("3000 records dataset generated successfully!")