## Lecture 4/6/26

### Random Variables

A **random variable (RV)** assigns the outcome of a random experiment to a numerical value.

The **distribution** of a RV describes how probability is assigned to the possible values of the RV.

* Discrete RVs map outcomes of a random experiment to discrete numerical values.
    * The **expected value**, $\mathbb{E}[X] = \sum_{x \in \mathrm{range}(X)} x\,P(X=x)$, is the probability-weighted average of RV $X$.
    * The **variance**, $\operatorname{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$, is the average squared distance of the values from the mean.
    * $\operatorname{SD}(X) = \sqrt{\operatorname{Var}(X)}$

* Continuous RVs map outcomes of a random experiment to continuous numerical values.
    * Continuous RVs are described by a probability density function $f(x)$.
    * Properties:
        * $P(X \le x) = \int_{-\infty}^{x} f(t)\,dt$
        * $0 \le P(X \le x) \le 1$
        * $\int_{-\infty}^{\infty} f(x)\,dx = 1$

### Sampling

* A **sampling distribution** is the distribution of a statistic computed from all possible samples of size $n$ from the population.
* Let $X_1, \dots, X_n \overset{\text{iid}}{\sim} Z$, where $Z$ is the population distribution.
    * **Sample Mean** — $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$ is an unbiased estimator of $\mathbb{E}[X]$
    * **Sample Variance** — $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2$ is an unbiased estimator of $\operatorname{Var}(X)$

### Properties of Expectation and Variance

* $\mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]$
* $\operatorname{Var}(aX + bY) = a^2 \operatorname{Var}(X) + b^2 \operatorname{Var}(Y)$, if $X \perp Y$
