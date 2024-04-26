def balanced_sample(df, target_column, sample_size):

    import pandas as pd
    df_positive = df[df[target_column] == 1]
    df_negative = df[df[target_column] == 0]
    assert sample_size <= 1, 'Sample size Cannot exceed 1'
    # Sample an equal number of samples from each subset
    sample_positive = df_positive.sample(n=int(len(df_positive) * sample_size // 2), replace=False)
    sample_negative = df_negative.sample(n=int(len(df_negative) * sample_size // 2), replace=False)

    # Concatenate the sampled subsets back together
    balanced_sample = pd.concat([sample_positive, sample_negative])

    return balanced_sample



def evaluate_features(df, target, sample_size=1):
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
    import statsmodels.api as sm
    import numpy as np

    df = balanced_sample(df, target, sample_size)

    # Separate features and target variable
    X = df.drop(['url', target], axis=1)
    y = df[target]

    # Apply one-hot encoding to categorical variables
    X = pd.get_dummies(X, drop_first=True, dtype=int)

    # X.head()
    # Train a random forest classifier
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_classifier.fit(X, y)

    # Train a logistic regression model
    lr_model = LogisticRegression(random_state=42, max_iter=2000)
    lr_model.fit(X, y)

    # Calculate feature importance scores from random forest
    feature_importances = rf_classifier.feature_importances_

    # Calculate coefficients and statistics from logistic regression
    coefs = lr_model.coef_[0]

    # Calculate p-values, std_err, and z-scores for logistic regression coefficients
    # x_np = X.values
    
    # X_with_intercept = sm.add_constant(X)  # Add constant term for intercept
    # lr_result = sm.Logit(y, X_with_intercept).fit(maxiter=1000)
    # lr_coefs = lr_result.params[1:]  # Exclude intercept

    # # Get p-values, std_err, and z-scores
    # lr_p_values = lr_result.pvalues[1:]  # Exclude intercept
    # lr_std_err = lr_result.bse[1:]  # Exclude intercept
    # lr_z_scores = lr_result.tvalues[1:]  # Exclude intercept

    # Calculate accuracy for both models
    rf_accuracy = accuracy_score(y, rf_classifier.predict(X))
    lr_accuracy = accuracy_score(y, lr_model.predict(X))

    # Combine results into a DataFrame
    result_df = pd.DataFrame({
        'Feature Importance (RF)': feature_importances,
        'Coefficient (LR)': coefs,
        'Accuracy (RF)': [rf_accuracy],
        'Accuracy (LR)': [lr_accuracy]
    }, index=X.columns)


    return result_df