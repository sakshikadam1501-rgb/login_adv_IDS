import pandas as pd
import random

users = ["user1", "user2", "user3"]

data = []

for user in users:
    for _ in range(200):
        # Normal behavior
        base_hour = random.choice([9, 10, 11]) if user == "user1" else random.choice([18, 19, 20])
        
        data.append([
            user,
            base_hour,
            random.randint(0, 2),
            0,
            0,
            0
        ])

# Attack simulation
for _ in range(100):
    data.append([
        random.choice(users),
        random.randint(0, 5),
        random.randint(5, 10),
        1,
        1,
        1
    ])

df = pd.DataFrame(data, columns=[
    "username", "login_hour", "failed_attempts",
    "ip_change", "device_change", "label"
])

df.to_csv("data/realistic_logs.csv", index=False)
print("Dataset ready!")