from .fitness_data_subject import FitnessDataSubject
class FitnessData(FitnessDataSubject):
    def __init__(self):
        self.steps = 0
        self.active_minutes = 0
        self.calories = 0
        self.observers = []
    
    def register_observer(self, observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
    
    def new_fitness_data_pushed(self, steps, active_minutes, calories):
        self.steps = steps
        self.active_minutes = active_minutes
        self.calories = calories

        print(f"\nFitnessData: New data received – Steps: {steps}, "
              f"Active Minutes: {active_minutes}, Calories: {calories}")
        
        self.notify_observers()
    
    def daily_reset(self):
        self.steps = 0
        self.active_minutes = 0
        self.calories = 0
        print("\nFitnessData: Daily reset complete")
        self.notify_observers()
    
    # Getters
    def get_steps(self):
        return self.steps
    
    def get_active_minutes(self):
        return self.active_minutes
    
    def get_calories(self):
        return self.calories