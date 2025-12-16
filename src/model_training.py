import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, classification_report


def split_features_target(df: pd.DataFrame, target_col: str):
    """
    Splits dataframe into features (X) and target (y).
    """

    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found")

    X = df.drop(columns=["CustomerId", target_col])
    y = df[target_col]

    if X.empty or y.empty:
        raise ValueError("Features or target is empty")

    return X, y


def train_test_data(X, y, test_size=0.2, random_state=42):
    """
    Creates stratified train-test split.
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    )


def train_logistic_regression(X_train, y_train):
    """
    Trains baseline Logistic Regression model.
    """

    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    )

    model.fit(X_train, y_train)
    return model


def train_random_forest(X_train, y_train):
    """
    Trains a Random Forest classifier.
    """

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced"
    )

    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluates model performance.
    """

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    auc = roc_auc_score(y_test, y_proba)
    report = classification_report(y_test, y_pred, output_dict=True)

    return auc, report
