from abc import ABC

class vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity  
        self.fuel_consumption = fuel_consumption  
    
    def drive(self, distance):
        pass
    
    def refuel(self, fuel):
        pass

class car(vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
    
    def drive(self, distance):
        required_fuel = (self.fuel_consumption + 0.9) * distance
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel
            print(f"Xe hơi đã di chuyển {distance} km")
        else:
            print("Xe hơi không đủ nhiên liệu để đi quãng đường này")
    
    def refuel(self, fuel):
        self.fuel_quantity += fuel
        print(f"Xe hơi đã đổ thêm {fuel} lít nhiên liệu")

class truck(vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
    
    def drive(self, distance):
        required_fuel = (self.fuel_consumption + 1.6) * distance
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel
            print(f"Xe tải đã di chuyển {distance} km")
        else:
            print("Xe tải không đủ nhiên liệu để đi quãng đường này")
    
    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95  # Giữ lại 95% nhiên liệu do rò rỉ
        print(f"Xe tải đã đổ thêm {fuel} lít nhiên liệu (giữ lại 95%)")

car = car(20, 5) 
car.drive(3) 
print(car.fuel_quantity) 
car.refuel(10) 
print(car.fuel_quantity) 
truck = truck(100, 15) 
truck.drive(5) 
print(truck.fuel_quantity) 
truck.refuel(50) 
print(truck.fuel_quantity)
