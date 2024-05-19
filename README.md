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
2. Data cleaning or genuine critical feature identification
3. Detection of noise in critical features
4. Decomposing complex feature information into multiple features, each containing specific details.

Method:
1. Examine target variation using EDA methods and identify sources of variation based on domain knowledge. If the variation sources cause interference in the prediction, reorganize the data to ensure suitability for accurate predictions.
2. Identify a feature utility metric that effectively demonstrates consistency in the relationship between the target and features as observed in the data analysis outcomes, aligning with domain knowledge. Furthermore, ensure that the relationship characterized by the index remains consistent across various resampled data subsets.
3. Mutual information serves as a valuable metric for quantifying the dependency between variables, making it particularly useful for selecting relevant features and reduces dimensionality in datasets.

Implementation:
* Data: Smartphones Price Dataset from Kaggle
* Examine target variation of Final Price using a violin plot. The violin plot indicates that the distribution of Final Price is unimodal.<img width="1116" alt="image" src="https://github.com/Tiffany-TW/BigData_AI_Analysis_Methods/assets/157606696/f9c31013-1391-4924-85dd-5af7b6a24605">
* Explore the dependency between the target and each feature using mutual information
   

#### What is Mutual Information?
