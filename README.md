# Credit Risk Probability Model for Alternative Data

## Credit Scoring Business Understanding

### Regulatory Context and Model Interpretability

The Basel II Capital Accord places strong emphasis on accurate risk measurement, transparency, and governance in credit risk modeling. Financial institutions are required not only to quantify credit risk but also to clearly explain how risk estimates are produced and how they are used in decision-making. As a result, credit scoring models must be interpretable, well-documented, and auditable. An interpretable model allows risk managers, regulators, and business stakeholders to understand the drivers of credit risk, validate model behavior, and ensure compliance with regulatory expectations. Poorly documented or opaque models increase model risk and may lead to regulatory challenges or misinformed credit decisions.

### Need for a Proxy Default Variable

In this project, the dataset does not contain an explicit label indicating whether a customer has defaulted on a loan. To address this limitation, a proxy target variable is required to approximate credit risk. We use customer behavioral patterns derived from transaction data, such as Recency, Frequency, and Monetary (RFM) metrics, to identify disengaged customers who are more likely to pose higher credit risk. Creating a proxy enables model development in the absence of direct default data; however, it introduces business risks. The proxy may not perfectly represent true default behavior, which can lead to misclassification of customers. This may result in rejecting potentially good customers or approving risky ones, affecting profitability and customer trust. Therefore, assumptions behind the proxy must be clearly stated, validated, and monitored over time.

### Model Complexity vs. Interpretability Trade-offs

There is a fundamental trade-off between model interpretability and predictive performance in credit risk modeling. Simple models such as Logistic Regression combined with Weight of Evidence (WoE) are highly interpretable, stable, and easier to justify in a regulated financial environment. They allow clear understanding of how individual features influence risk and are often preferred by regulators. In contrast, complex models like Gradient Boosting can capture non-linear relationships and interactions, often achieving higher predictive accuracy. However, they operate as black-box models, making them harder to explain and govern. In regulated contexts, this increases model risk and requires additional explainability techniques. The choice of model therefore involves balancing regulatory compliance, transparency, and performance, often favoring simpler models unless performance gains from complex models are substantial and well-justified.
