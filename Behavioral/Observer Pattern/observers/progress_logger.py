from .fitness_data_observer import FitnessDataObserver

class ProgressLogger(FitnessDataObserver):
    def update(self, data):
        print(f"Logger → Saving to DB: Steps={data.get_steps()}, "
              f"ActiveMinutes={data.get_active_minutes()}, "
              f"Calories={data.get_calories()}")
        # Simulate saving to DB
        print("DB: Successfully saved fitness data")