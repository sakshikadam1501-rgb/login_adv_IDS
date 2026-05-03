user_patterns = {}

def update_behavior(username, login_hour):
    if username not in user_patterns:
        user_patterns[username] = []
    
    user_patterns[username].append(login_hour)

def is_anomalous(username, login_hour):
    if username not in user_patterns or len(user_patterns[username]) < 5:
        return False
    
    avg = sum(user_patterns[username]) / len(user_patterns[username])
    
    return abs(login_hour - avg) > 5