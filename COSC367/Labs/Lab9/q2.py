from numbers import Number

def posterior(prior, likelihood, observation):
    prob_true = prior; prob_false = 1 - prior
    for _ in range(len(observation)):
        if observation[_]:
            prob_true *= likelihood[_][1]
            prob_false *= likelihood[_][0]
        else:
            prob_true *= (1 - likelihood[_][1])
            prob_false *= (1 - likelihood[_][0])
    return prob_true / (prob_true + prob_false)

prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))
