## Lecture 4/6/26

### Random Variables

A **random variable (RV)** assigns the outcome of a random experiment to a numerical value.

The **distribution** of a RV describes how probability is assigned to the possible values of the RV.

* Discrete RVs map outcomes of a random experiment to discrete numerical values.
    * The **expected value**, $\mathbb{E}[X] = \sum_{x \in \mathrm{range}(X)} x\,P(X=x)$, is the probability-weighted average of RV $X$.
    * The **variance**, $Var(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$, is the average squared distance of the values from the mean.
    * $SD(X) = \sqrt{Var(X)}$

* Continuous RVs map outcomes of a random experiment to continuous numerical values.
    * Continuous RVs are described by a probability density function $f(x)$.
    * Properties:
        * $P(X \le x) = \int_{-\infty}^{x} f(t)\,dt$
        * $0 \le P(X \le x) \le 1$
        * $\int_{-\infty}^{\infty} f(x)\,dx = 1$

### Sampling

* A **sampling distribution** is the distribution of a statistic computed from all possible samples of size $n$ from the population.
* Let $X_1, \dots, X_n \overset{\text{iid}}{\sim} Z$, where $Z$ is the population distribution.
    * **Sample Mean** — $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$ is an unbiased estimator of $\mu$; i.e $\mathbb{E}[\bar{X}] = \mu$
    * **Sample Variance** — $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2$ is an unbiased estimator of $\sigma^2$; i.e. $\mathbb{E}[S^2] = \sigma^2$
 * A **simple random sample (SRS)** means that all possible samples of size n have an equal chance of being selected from the sampling distribution

### Bias Variance Decomposition
* Let $\mu$ be the point estimate of $\mu^*$. Then,
  \[
      \mathbb{E}\big[(\mu^*-\mu)^2\big]
      =
      \underbrace{\big(\mathbb{E}[\mu]-\mu^*\big)^2}_{\mathrm{bias}^2}
      +
      \underbrace{\mathbb{E}\big[(\mu-\mathbb{E}[\mu])^2\big]}_{\mathrm{variance}}
   \]


### Properties of Expectation and Variance

* $\mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y]$
* $Var(aX + bY) = a^2 Var(X) + b^2 Var(Y)$, if $X \perp Y$
