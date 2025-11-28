from .fitness_data_observer import FitnessDataObserver

class GoalNotifier(FitnessDataObserver):
    def __init__(self):
        self.step_goal = 10000
        self.goal_reached = False

    def update(self, data):
        if data.get_steps() >= self.step_goal and not self.goal_reached:
            self.goal_reached = True
            print(f"Notifier → 🎉 Goal Reached! You've hit {self.step_goal} steps!")

    def reset(self):
        self.goal_reached = False