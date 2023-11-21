def alpha_beta_pruning(state, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_terminal_state(state):
        return evaluate_state(state)

    if maximizing_player:
        value = float('-inf')
        for child_state in generate_child_states(state):
            child_value = alpha_beta_pruning(child_state, depth - 1, alpha, beta, False)
            if child_value is not None:
                value = max(value, child_value)
                alpha = max(alpha, value)
                if alpha >= beta:
                    break  # Beta cut-off
        return value
    else:
        value = float('inf')
        for child_state in generate_child_states(state):
            child_value = alpha_beta_pruning(child_state, depth - 1, alpha, beta, True)
            if child_value is not None:
                value = min(value, child_value)
                beta = min(beta, value)
                if beta <= alpha:
                    break  # Alpha cut-off
        return value

# ... (rest of the code remains the same)
