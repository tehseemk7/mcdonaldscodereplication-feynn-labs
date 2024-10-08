visit_means = data.groupby('Like')['Age'].mean() 
like_means = data.groupby('Like')['Age'].mean() 
female_means = data.groupby('Like')['Age'].apply(lambda x: (x == 'Female').mean())
plt.scatter(visit_means, like_means, s=1000 * female_means, alpha=0.5, c='blue', edgecolors='w', linewidth=0.5)
for i in range(len(visit_means)):
    plt.text(visit_means[i], like_means[i], str(i+1))
plt.xlabel('Visit Frequency')
plt.ylabel('Like')
plt.title('Segment Evaluation Plot')
plt.show()