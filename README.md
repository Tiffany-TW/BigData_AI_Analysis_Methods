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
* Data: Automobile Dataset from Kaggle
* Examine target variation of price using a violin plot. The violin plot indicates that the distribution of price is unimodal for most car brands.<img width="1506" alt="image" src="https://github.com/Tiffany-TW/BigData_AI_Analysis_Methods/assets/157606696/f9c86f44-c0ba-48d9-9d16-c3a51609128b">
* Explore the dependency between the target and each feature using mutual information <img width="1566" alt="image" src="https://github.com/Tiffany-TW/BigData_AI_Analysis_Methods/assets/157606696/c56ff047-5e64-4571-8d7e-671189f5e489"> The bar plot indicates that the dependency between curb-weight and price is the strongest of all.
* Note01: sklearn.feature_selection provides two functions mutual_information_regression and mutual_information_classif for numerical and categorical target variables respectively. Ensure discrete features in the dataset are transformed into integer type before calculating mutual information.
* Note02: It's good to investigate possible interaction effects before determining the features most relevant to the target based on mutual information. Example:



#### What is Mutual Information?
* One feature utility metric that quantifies the stength of (linear or non-linear) of correlation between two variables, say the target and features. The value of MI lies within 0 and infinity.
* In information theory terms, MI measures the amount of information that two variables provide about each other (symmetric).
* In terms of entropy, mutual information is clearly explained.
  * Entropy, denoted by H(X), is a measure of the average level of uncertainty of a random variable. Mathematically, H(X) is defined as $-\sum_{x \in X} {p(x)\log p(x)}$. It is clear
  * Information content ![information_content_illus](https://github.com/Tiffany-TW/BigData_AI_Analysis_Methods/assets/157606696/936735b6-ac1f-4b9b-9bec-f9d0daebd668)



#### Properties of Mutual Information
* Explicit relation between the feature item and the target ![mi_of_functions](https://github.com/Tiffany-TW/BigData_AI_Analysis_Methods/assets/157606696/df39def6-8146-4e73-8615-870d9fc3bb32)


* Add some gaussian noise to the function ![mi_of_function_add_noise](https://github.com/Tiffany-TW/BigData_AI_Analysis_Methods/assets/157606696/c34b7a94-0cac-4537-a063-9a1d02e6cc93)

#### Reference
1. https://www.kaggle.com/code/ryanholbrook/mutual-information 

