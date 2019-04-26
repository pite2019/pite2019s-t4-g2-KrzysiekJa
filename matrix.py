class Matrix:
    def __init__(self, row1column1 = 0, row1column2 = 0, row2column1 = 0, row2column2 = 0):
        self.row1column1 = row1column1
        self.row1column2 = row1column2
        self.row2column1 = row2column1
        self.row2column2 = row2column2
        
    def add(self,new_one):
        r1c1 = self.row1column1 + new_one.row1column1
        r1c2 = self.row1column2 + new_one.row1column2
        r2c1 = self.row2column1 + new_one.row2column1
        r2c2 = self.row2column2 + new_one.row2column2
        
        return r1c1, r1c2, r2c1, r2c2
    
    def dotProduct(self,new_one):
        r1c1 = self.row1column1 * new_one.row1column1
        r1c2 = self.row1column2 * new_one.row1column2
        r2c1 = self.row2column1 * new_one.row2column1
        r2c2 = self.row2column2 * new_one.row2column2
        
        return r1c1 + r1c2 + r2c1 + r2c2
    
    def crossProduct(self,new_one):
        r1c1 = self.row1column1 * new_one.row1column1 + self.row1column2 * new_one.row2column1
        r1c2 = self.row1column1 * new_one.row1column2 + self.row1column2 * new_one.row2column2
        r2c1 = self.row2column1 * new_one.row1column1 + self.row2column2 * new_one.row2column1
        r2c2 = self.row2column1 * new_one.row1column2 + self.row2column2 * new_one.row2column2
        
        return r1c1, r1c2, r2c1, r2c2
