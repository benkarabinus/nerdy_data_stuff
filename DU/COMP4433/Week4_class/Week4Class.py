from matplotlib import pyplot as plt, gridspec
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import seaborn as sns

mpg = sns.load_dataset("mpg")

fig, ax = plt.subplots(1, 2, figsize=(14, 6))
ax[0].hist(mpg['horsepower'])




plt.tight_layout()
plt.show()






"""
gs = gridspec.Gridspec(4, 4)
ax0 = plt.subplots(gs[:2, :3])
ax1 = plt.subplots(gs[-2:, :3])
"""
