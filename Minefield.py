import random
class Minefield:
    def __init__(self,size,num):
        self.num_of_mine=num
        self.size=size
        self.field=None
        self.displayed_field=None
    
    def display_all_cells(self):
        for row in self.field:
            print(row)
    
     
    
    def display_field(self):
        for row in self.displayed_field:
            print(row)
    
    def make_displayed_field(self):
        (rows,cols)=self.size
        #'*' is unopened,' ' reserves for flag
        self.displayed_field=[[('*',' ')for i in range(cols)]for j in range(rows)]

    def make_field(self):
        (num_of_rows,num_of_cols)=self.size
        self.field=[[-1 for i in range(num_of_cols)]for j in range(num_of_rows)]
        self.plant_mines(self.num_of_mine,num_of_rows,num_of_cols)
        self.write_mine_nums(num_of_rows,num_of_cols)
    
    def plant_mines(self,num,rows,cols):
        for i in range(num):
            row,col=self.get_cell(rows,cols)
            self.field[row][col]='M'
    
    def write_mine_nums(self,rows,cols):
        for i in range(rows):
            for j in range(cols):
                if self.field[i][j]=='M':
                    continue
                self.field[i][j]=self.count_mine(i,j,rows,cols)
        

    def get_cell(self,rows,cols):
        row,col=random.randint(0,rows-1),\
                random.randint(0,cols-1)
        while self.field[row][col]=='M':
            row,col=random.randint(0,rows-1),\
                random.randint(0,cols-1)
        return row,col
    
    def count_mine(self,r,c,rows,cols):
        num=0
        for i in range(max(r-1,0),min(r+1,rows-1)+1):
            for j in range(max(c-1,0),min(c+1,cols-1)+1):
                if i==r and j==c:
                    continue
                if self.field[i][j]=='M':
                    num+=1
        return num

            
minefield=Minefield((4,5),7)
minefield.make_field()
minefield.make_displayed_field()
minefield.display_field()
minefield.display_all_cells()


            

            

        

