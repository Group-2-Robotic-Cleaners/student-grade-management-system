import matplotlib.pyplot as plt
import seaborn as sns

def plot_grade_distribution(grades):
    sns.countplot(x=grades)
    plt.title("Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Count")
    plt.show()
