class Vehicle:
    def __init__(self,model,brand,seriel):
        self.brand = brand
        self.model = model
        self.seriel = seriel

Bugati = Vehicle("Bugati","BugatiChiron"," (VIN)")
Ferrari = Vehicle("Ferrari","298 GTS","(TIN)")
print(f"Name:{Bugati.brand},Model:{Bugati.model},Type:{Bugati.seriel}")
print(f"Name:{Ferrari.brand},Model:{Ferrari.model},Type:{Ferrari.seriel}")