class Order:
    class OrderBuilder:
        def __init__(self):
            self.weight = None
            self.distance = None
            self.value = None
        
        def set_weight(self, weight):
            self.weight = weight
            return self
        
        def set_distance(self, distance):
            self.distance = distance
            return self
        
        def set_value(self, value):
            self.value = value
            return self
        
        def build(self):
            return Order(self)
        
        
    def __init__(self, builder: OrderBuilder):
        self.weight = builder.weight
        self.distance = builder.distance
        self.value = builder.value
        
    def __repr__(self):
        return f"Order(weight={self.weight}, distance={self.distance}, value={self.value})"