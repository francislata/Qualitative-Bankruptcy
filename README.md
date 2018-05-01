# Qualitative Bankruptcy

## Description
This project is about determining whether a company's set of qualities (e.g., financial flexibility, credibility, etc.) can determine whether or not they will be most likely become bankrupt or not. This kind of study is helpful for determing whether financial institutions are more or less likely to approve a company's request for a loan. Also, this is helpful for investors when deciding whether to put in their investments to a certain company.

## How to run
Set working directory to the root of this project and run the following command:
```python run.py```.

## Details

### Data
Based from the dataset, the following qualitative features are used to determine whether an individual will be bankrupt or not:
- Industrial Risk
- Management Risk
- Financial Flexibility
- Credibility
- Competitiveness
- Operating Risk

The descriptions for these variables are described in this [paper](https://pdfs.semanticscholar.org/e9f9/1b103539087b2df1edf40d13de455417e270.pdf) in section 2 titled **Data mining techniques for extracting experts’ decision rules**.

### Models
There are two models in this project: **support vector machine** and **logistic regression** models.

**1) Logistic regression**

This model has been chosen due to the binary classification capabilities. This is a go-to model for binary classification problems, as it is the case for this project.

**2) Support vector machine**

This model has also been chosen due to its capability to separate out binary classes by a decision boundary line. Since it maximizes the margin between the data points relative to the decision boundary line, it became an ideal model to try out for this project.

### Results
**Phase 1**
Initially, all features have been used to see whether they can predict bankruptcy. As a result, I have found that *SVM is better than logistic regression*. Clearly, the SVM has separated positive and negative examples perfectly. In particular, SVM got an accuracy of 1.0 while logistic regression got 0.76.

**Phase 2**
After reading the original paper where this dataset is based from, I have found that using the **competitiveness** (i.e., the company's competitive advantage) and **financial flexibility** (i.e., the ability of a company to receive financial support from third parties) are the key features in bankruptcy prediction.

After using these features, I have found that *SVM is still better than logistic regression*. A new improvement came in to light when the logistic regression's accuracy increased from 0.76 to 0.96. This is an increase of 0.20 in accuracy.

## Conclusion
The original article claimed that genetic algorithms are far superior in bankruptcy prediction than neural networks. Due to the time (2003) when this article was written and with the advanced improvements in shallow and deep algorithms, SVM has attained a better accuracy than genetic algorithms.

## Credits
The dataset used to train and test the model created in this project has been provided by:

Dua, D. and Karra Taniskidou, E. (2017). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

In particular, the qualitative bankruptcy dataset can be found [here](https://archive.ics.uci.edu/ml/datasets/Qualitative_Bankruptcy).