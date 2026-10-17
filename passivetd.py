current_utility = 0.0
reward = 5.0
next_state_utility = 10.0
alpha = 0.5       
gamma = 0.9       
td_error = reward + gamma * next_state_utility - current_utility
new_utility = current_utility + alpha * td_error
print("Current Utility:", current_utility)
print("Reward:", reward)
print("Next State Utility:", next_state_utility)
print("TD Error:", td_error)
print("New Utility:", new_utility)
print("\nUtilities over multiple episodes:")
utility = 0.0
next_utility = 10.0
for episode in range(1, 11):
    td_error = reward + gamma * next_utility - utility
    utility = utility + alpha * td_error
    print(f"Episode {episode}: Utility = {utility:.4f}")
