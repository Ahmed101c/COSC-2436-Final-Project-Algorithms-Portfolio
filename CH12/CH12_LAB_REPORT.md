# Lab Report Template

## Student Information
**Name:** Ahmed Ajlal
**Date:** 04/30/2025
**Algorithm Analysis:** K-Nearest Neighbors (KNN) Regression for Bakery Loaf Prediction

---

## Algorithm Understanding

**What type of problem is this algorithm solving?**
This algorithm is solving a **regression problem**. It predicts a continuous numerical value (number of loaves) based on input features using supervised learning.

**How does KNN regression differ from KNN classification?**
KNN classification predicts a **discrete label** by taking a majority vote among the nearest neighbors, while KNN regression predicts a **continuous value** by averaging the neighbors’ values.


**What does the "K" in KNN represent, and why did we choose k=4 for this problem?**
**K** in KNN stands for the **number of nearest neighbors** used to make a prediction.

We choose **k = 4** to balance noise and generalization—small k can be too sensitive to outliers, while larger k smooths predictions; 4 likely gave the best performance (e.g., via validation) for this dataset.


**In your own words, explain how the model produces a prediction for a new day.**
The model looks at the new day’s features and finds the **k most similar historical days** (the closest neighbors). It then takes those days’ loaf counts and **averages them** to produce the prediction for the new day.


---

## Implementation Questions

**Why do we separate the DataFrame into features (X) and target (y) before training?**
We split the DataFrame into **features (X)** and **target (y)** so the model clearly knows what inputs to learn from and what output to predict. X contains the variables used to make predictions, while y is the correct answer the model tries to learn—keeping them separate prevents accidentally using the answer as an input and ensures proper training.

**Why must the input to `model.predict()` be a 2D array (e.g., `[[4, 1, 0]]`) instead of a 1D array (`[4, 1, 0]`)?**
Because the model expects input in the shape **(number of samples, number of features)**. A 2D array like `[[4, 1, 0]]` represents **one sample with three features**, while `[4, 1, 0]` is just a 1D list and doesn’t indicate how many samples there are, so the model can’t interpret it correctly.


**What does `.fit(X, y)` actually do for a KNN model? (Hint: it's different from most other ML algorithms.)**
[Your explanation — KNN is a "lazy learner" that mostly just stores the data]
For KNN, .fit(X, y) doesn’t learn a formula or model parameters—instead, it simply stores the training data (both X and y).
KNN is a lazy learner, so the real work happens during prediction, when it compares new data points to the stored dataset to find the nearest neighbors.

**Why do we use `.values` when extracting columns from the DataFrame?**
We use `.values` to convert a pandas DataFrame or Series into a **NumPy array**, which is the format most machine learning models (like KNN) expect for training and prediction.


---

## Extension: Choosing K

**What would happen if we set k=1? What are the risks?**

If **k = 1**, the model predicts based on the **single closest data point**. This makes it very sensitive to noise or outliers—any unusual or mislabeled point can directly cause incorrect predictions, leading to **overfitting** and poor generalization to new data.

**What would happen if we set k=20 (the size of the entire dataset)? What does the model become?**

If **k = 20** (i.e., using the entire dataset), the model no longer relies on “nearest neighbors” in any meaningful way. Instead, it effectively **ignores distance entirely** and just predicts the **overall average (for regression)** or **majority class (for classification)** of the whole dataset.

So the model becomes a **simple baseline predictor** with no sensitivity to individual input differences.


**How would you decide what value of k is best for a given dataset?**
You choose the best **k** by trying multiple values and evaluating performance on validation data (or using cross-validation). The optimal k is the one that gives the lowest prediction error while balancing **overfitting (small k)** and **underfitting (large k)**.


---

## Extension: Distance and Feature Scaling

**KNN uses distance to find "nearest" neighbors. Our features have very different ranges: weather is 1–5, but weekend_holiday and game_on are 0/1. Why could this be a problem?**

This is a problem because KNN relies on **distance calculations**, and features with larger numeric ranges can dominate that distance. Even though weather (1–5) and binary features (0/1) all matter, the model may give too much influence to features with bigger scales, making the “nearest neighbors” misleading. This can lead to poor predictions unless the data is **properly scaled or normalized**.


**Give an example of two days where the weather feature would unfairly dominate the distance calculation.**

Example:
Day A = [weather = 5, weekend_holiday = 0, game_on = 0]
Day B = [weather = 1, weekend_holiday = 1, game_on = 1]
Because weather ranges from 1–5 while the others are only 0–1, the large difference in weather (5 vs 1) can dominate the distance calculation, making the model consider these days very “far apart” even though the binary features might actually be more important.

**How would you modify the data preparation step to fix this? (Hint: look up "feature scaling" or "StandardScaler".)**
To fix the problem, you would apply **feature scaling** so all features are on a similar range before running KNN. A common approach is using **StandardScaler**, which transforms each feature to have mean 0 and standard deviation 1.

This prevents large-scale features (like weather) from dominating the distance calculation and ensures all features contribute fairly to finding nearest neighbors.


---

## Reflection Questions

**What is a limitation of KNN regression? Provide a scenario where it would make a poor prediction.**
[Your explanation — e.g., predicting a day with conditions far outside any historical data]

**Our dataset only has 20 days of data. How might the predictions change if we had 2,000 days of data instead?**
A key limitation of KNN regression is that it can only make predictions based on **existing nearby examples**, so it struggles when a new input is **unlike anything in the training data** (it has no real extrapolation ability).

**Example scenario:**
If all historical days have mild or moderate weather patterns, but a new day has extreme conditions (e.g., unusually high temperature combined with a major event that never occurred before), KNN will still average the “closest” normal days and produce a prediction that is likely **inaccurate or overly conservative**, since it has no truly similar cases to rely on.

**What other features (beyond weather, weekend/holiday, and game day) could the bakery collect to improve predictions?**

The bakery could improve predictions by adding features like **temperature, season, day of the week, local events, social media buzz or promotions, school holidays, and historical sales trends (e.g., last week’s demand)**. These extra signals can help the model better capture patterns that affect loaf demand.

**KNN is sometimes called a "lazy learning" algorithm because it does almost no work during training. What is the tradeoff at prediction time?**

The tradeoff is that while training is very fast, **prediction becomes slower**, because the model must compute distances from the new point to **every training example** and then sort or select the nearest ones before making a decision.


**The autograder expects a prediction of approximately 70.5 loaves for today's conditions. Manually look at the dataset and identify which 4 historical days you think the model is averaging. Do their loaf counts average to 70.5?**

To answer this correctly, I need to actually see the dataset (the historical days and their loaf counts). Without that table, I can’t reliably identify which 4 rows correspond to the nearest neighbors or verify whether their average is 70.5.
But here’s exactly how you would do it:
Find the 4 historical days most similar to today’s conditions (based on the features: weather, weekend/holiday, game day, etc.).
Write down their loaf counts.
Compute the average.

**Why might a bakery prefer a slightly inaccurate ML prediction over a human guess for daily loaf counts?**

A bakery might prefer a slightly inaccurate ML prediction because it is **consistent, data-driven, and scalable**, meaning it can make the same type of informed estimate every day without bias or fatigue. Even if it’s not perfect, it often performs better overall than human guesses and helps **reduce waste and stockouts** by learning patterns from past data instead of relying on intuition.


**If the bakery wanted to MINIMIZE waste (unsold loaves) rather than just predict accurately, how might you change the approach?**

To minimize waste, you’d shift from just “best prediction” to **cost-aware prediction**. For example, you might intentionally **bias predictions slightly lower**, or use a model/threshold that penalizes overestimates more heavily than underestimates (a custom loss function). You could also factor in the **cost of unsold bread vs. lost sales**, so the model learns that overproducing is more expensive than occasionally running out.
