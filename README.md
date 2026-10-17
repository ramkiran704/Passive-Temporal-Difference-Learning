# Aim
---
**To implement Passive Temporal-Difference (TD) Learning in Python, update state utilities using observed rewards and next-state utilities, and observe how utilities change over multiple episodes.**
---
# Theory: Passive Temporal-Difference (TD) Learning

Passive Temporal-Difference (TD) Learning is a reinforcement learning technique used to estimate the utility of states while an agent follows a fixed policy. The agent observes the immediate reward and the next state after each action, then updates the utility estimate without requiring a complete model of the environment.

Initially, all state utilities are set to zero. As the agent interacts with the environment over multiple episodes, the utility estimates improve based on the rewards and observed transitions.

## TD Utility Update Equation

The TD(0) learning rule is:

U(s) = U(s) + α [R + γU(s') - U(s)]

Where:
- U(s): Current utility of the state.
- R: Immediate reward received.
- U(s'): Utility of the next state.
- α: Learning rate, which determines how much the estimate changes.
- γ: Discount factor, which determines the importance of future rewards.
- TD Error: The difference between the TD target and the current utility.

## Working Principle

1. Initialize the utility values of all states to zero.
2. Follow the given fixed policy to select actions.
3. Observe the immediate reward and next state.
4. Calculate the TD error using the current utility, reward, and next-state utility.
5. Update the current state's utility using the TD(0) equation.
6. Repeat the process over multiple episodes.
7. Observe how the utility estimates change and gradually approach their expected values.

## Advantages

- Does not require a complete model of the environment.
- Learns directly from experience.
- Updates utility estimates after each transition.
- Requires less computation than methods that repeatedly evaluate the full environment model.

## Applications

- Robot navigation.
- Grid-world problem solving.
- Autonomous decision-making.
- Reinforcement learning in dynamic environments.

## Conclusion

Passive Temporal-Difference Learning estimates state utilities by following a fixed policy and learning from observed rewards and state transitions. By repeatedly applying the TD(0) update rule, the agent gradually improves its utility estimates over multiple episodes.
