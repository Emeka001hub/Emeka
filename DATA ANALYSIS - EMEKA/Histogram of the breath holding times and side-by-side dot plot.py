import matplotlib.pyplot as plt
import pandas as pd

data_sample = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male',
               'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female',
               'Female', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'Time for breath held': [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27,
                             9.09, 51.15, 58.32, 22.22, 30.57, 17.47, 22.39,
                             26.90, 36.85, 27.33, 29.55, 13.87, 34.66],
    'Height': [184, 182, 180, 191, 189, 181, 180, 170, 176, 185, 175, 158,
               166, 175, 160, 165, 166, 170, 170, 172]
}

df = pd.DataFrame(data_sample)

plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.hist(df['Time for breath held'], bins=10, color='yellow', edgecolor='black', alpha=0.7)
plt.title('Histogram of Time for Breath held')
plt.xlabel('Time for breath held')
plt.ylabel('Frequency')


plt.subplot(1, 2, 2)

plt.scatter(df[df['Gender'] == 'Male']['Time for breath held'],
            [0] * sum(df['Gender'] == 'Male'),
            color='purple', label='Male', alpha=0.6)

plt.scatter(df[df['Gender'] == 'Female']['Time for breath held'],
            [1] * sum(df['Gender'] == 'Female'),
            color='pink', label='Female', alpha=0.6)

plt.title('Side-by-Side Dot Plot of Time for breath held')
plt.yticks([0, 1], ['Male', 'Female'])
plt.xlabel('Time for breath held')
plt.legend()


plt.tight_layout()
plt.show()
