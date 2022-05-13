# Breast Cancer Data Analysis

<p align='justify'>Breast Cancer is a disease commonly found in women, an abnormally grown cells in the breast tissue are referred to as a tumor. These tumors are not always cancer cells, these are sometimes benign, pre-malignant, or malignant. To identify and diagnose this various tests such as MRI, ultrasound, biopsy, and mammograms are used. The data set we considered has details regarding the breast cancer results from the breast fine-needle aspiration test, which involves collecting some fluid or cells from a breast cyst and results are classified and reported as ‘1’ and ‘0’ which refers to Malignant(presence of cancer cells) and Benign(absence of cancer cells). This is considered a classification problem in machine learning. The goal or the objective of this project is to classify whether the breast cancer is malignant or benign and also predict the recurrence and non-recurrence of the cases using Logistic Regression.


<p align='justify'>I have submitted two different codes, one includes Exploratory Data Analysis and the other one includes the Machine Learning model. The data set considered has 32 columns and 569 rows (a pretty small dataset though).

[Kaggle Dataset Link](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)

<br />
<br />
<br />

**Exploratory Data Analysis:**

I have done a few plotting to understand the data set and relation between the different columns available. I will be attaching the links that I referred to understand and implement for my dataset.

1. [Violin Plot](https://www.geeksforgeeks.org/violin-plot-for-data-analysis/)
<p align='justify'>The violin plot usually explains whether the considered variables are good for classification or not. If the median of m and b looks like they are separated then it is assumed that they are good for classification. For example, in this plot, we can see texture_mean has a median that looks separate whereas factional dimension mean doesn’t look separated.

<br />
<br />

2. [Kde Plot](https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/)
<p align='justify'>KDE plot is useful in understanding the probability distribution if there are multiple samples in a single plot. We can see the probability distribution of malignant and benign with the help of this plotting.

<br />
<br />

3. [Heatmap](https://towardsdatascience.com/annotated-heatmaps-in-5-simple-steps-cc2a0660a27d)
<p align='justify'>The correlation matrix is plotted to understand the correlation between the various columns available in our data set, we can see radius perimeter and area have a strong positive correlation and can be used in our analysis Other ones like compactness mean, concavity means and concave point mean are also positively correlated which can be useful for our analysis.

<br />
<br />

4. [Scattermatrix](https://www.geeksforgeeks.org/scatter-plot-matrix/)
<p align='justify'>The scatter plots help us in identifying how the variables are related to each other. The output displays the mean values of the distributions and relationships in the dataset. The mean values of cell radius, perimeter, area, compactness, concavity, and concave points can be used in the classification of breast cancer and a large value of these parameters tends to show a correlation between malignant tumors. I have also included scatter plots for positively correlated, negatively correlated, and un-correlated variables.

<br />
<br />

**Machine Learning-Using PySaprk:**

1. [PCA](https://towardsdatascience.com/dive-into-pca-principal-component-analysis-with-python-43ded13ead21)

<p align='justify'>Principal Component Analysis considers the correlation among variables. If the correlation is very high, PCA attempts to combine highly correlated variables and finds the directions of maximum variance in higher-dimensional data. The original data has 30 features, however, I tried to run PCA with lesser components. Now we transformed the original data set to build our regression models. I have used seaborn implots for representing PCA, logistic regression, and tree classifiers.

<br />
<p align='justify'>I used this method by referring to multiple open sources and tried to implement it on smaller data for better learning and to understand the difficulties that need to be faced using this method.

<br />
<br />

2. [Logistic Regression](https://towardsdatascience.com/logistic-regression-for-malignancy-prediction-in-cancer-27b1a1960184)

<p align='justify'>I have implemented the Logistic regression method of machine learning to understand the possibilities and predict the data. Post analysis, I could see there are no false positives or false negatives and I plotted the same using seaborn implot. Not sure if this is an effective approach to processing this data but did try a few more regression models without using pyspark for better analysis.

<p align='justify'>I did try test and error codes which helped in deriving accuracy of 98% and 96% for Logistic Regression and Decision Tree Analysis. I have not attached those test and error files as they do not add much to my learning.

<br />
<br />

**Takeaways**

1. These Machine learning models help in analyzing larger sets of data and help in identifying diseases and promoting diagnosis. This identifies potential therapeutic targets to propose new therapies and minimize potential side effects.
 <br />

2. a Better understanding of cleaning and processing data is the major personal takeaway for me from this project.
<br />

