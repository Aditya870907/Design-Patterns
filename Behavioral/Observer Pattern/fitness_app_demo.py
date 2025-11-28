from subject.fitness_data import FitnessData
from observers.live_activity_display import LiveActivityDisplay
from observers.progress_logger import ProgressLogger
from observers.goal_notifier import GoalNotifier

class FitnessAppDemo:
    def main():
        fitness_data = FitnessData()

        live_display = LiveActivityDisplay()
        progress_logger = ProgressLogger()
        goal_notifier = GoalNotifier()

        # Register observers
        fitness_data.register_observer(live_display)
        fitness_data.register_observer(progress_logger)
        fitness_data.register_observer(goal_notifier)

        # Simulate updates
        fitness_data.new_fitness_data_pushed(1000, 30, 200)
        fitness_data.new_fitness_data_pushed(1500, 45, 250)
        fitness_data.new_fitness_data_pushed(11000, 60, 300)

        # Daily reset
        fitness_data.daily_reset()
        goal_notifier.reset()

if __name__ == "__main__":
    print("\n\n=== Observer Pattern Approach ===")
    FitnessAppDemo.main()