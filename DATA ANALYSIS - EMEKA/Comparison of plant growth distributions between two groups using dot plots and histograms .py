import pandas as pd
import matplotlib.pyplot as plt

sound_data_sample = {
    'With Music': [304, 317, 332, 299, 0,
                   257, 387, 308, 206, 0,
                   174,  47, 317, 278, 0,
                   214,  157, 286, 188, 0,
                   69, 0, 236, 43, 0],
    'Without Music': [292, 292, 282, 3, 94,
                      270, 364, 149, 324,164,
                      47, 316, 274, 2, 0,
                      288, 287, 319, 128, 0,
                      324, 75, 213, 219, 0,]
}

df = pd.DataFrame(sound_data_sample)


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.hist(df['With Music'], bins=10, color='yellow', alpha=0.5, edgecolor='black')
plt.title('Histogram of Plant Growth With Music')
plt.xlabel('Growth')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.7)

plt.subplot(1, 2, 2)
plt.hist(df['Without Music'], bins=10, color='yellow', alpha=0.5, edgecolor='black')
plt.title('Histogram of Plant Growth Without Music')
plt.xlabel('Growth')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.7)

plt.tight_layout()
plt.show()

plt.figure(figsize=(11, 5))


plt.subplot(1, 2, 1)
plt.scatter(df['With Music'], [0] * len(df['With Music']), color='yellow', alpha=0.5)
plt.title('Dot Plot of Plant Growth With Music')
plt.yticks([])
plt.xlabel('Growth')
plt.axhline(0, color='black', lw=0.5)


plt.subplot(1, 2, 2)
plt.scatter(df['Without Music'], [0] * len(df['Without Music']), color='blue', alpha=0.5)
plt.title('Dot Plot of Plant Growth Without Music')
plt.yticks([])
plt.xlabel('Growth')
plt.axhline(0, color='black', lw=0.5)

plt.tight_layout()
plt.show()
