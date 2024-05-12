# BigData_AI_Analysis_Methods
This repository contains methods and strategies for effectively tackling challenges encountered during big data processing and AI model analysis.
## Tackling Overfitting Problems
### Case 1: Feature Selection Using Mutual Information 
Case description: 
* low correlation coefficient between target and domain knowledge-based critical features
* For features exhibiting high correlation with the target, the scatter plots reveal the presence of multiple clusters, yet the precise relationship between the features and the target warrants further elucidation.
* Due to constraints in data availability, certain portions of the collected data fail to fully elucidate the genuine circumstances surrounding the features.
* Even though the collected data is unsufficient to elucidate the genuine circumstances surrounding the features, we encountered overfitting problems. The following shows three possible reasons : (1) certain features are irrelevant with the target but they coincidently follow the pattern that increases the performance of the training model (2)  (3)

Analysis:
1. Inconsistency in the relationship between the target and features observed in the data analysis outcomes compared to domain knowledge
2. Feature selection using mutual information
3. Detection of noise in critical features
4.  

  Mutual information serves as a valuable metric for quantifying the dependency between variables, making it particularly useful for selecting relevant features and reduces dimensionality in datasets.
#### What is Mutual Information?
