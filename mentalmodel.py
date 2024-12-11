class mentalIllnessData:
    def __init__(
        self,
        Entity,
        Code,
        Year,
        Depressive,
        Schizophrenia,
        Bipolar,
        Eating,
        Anxiety
    ):
        self.Entity = Entity
        self.Code = Code
        self.Year = int(Year)
        self.Depressive = float(Depressive)
        self.Schizophrenia = float(Schizophrenia)
        self.Bipolar = float(Bipolar)
        self.Eating = float(Eating)
        self.Anxiety = float(Anxiety)
    
    def __str__(self):
        return f"{self.Entity}: {self.Year} - {self.Depressive}"
    
