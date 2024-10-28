import random
class Minefield:
    def __init__(self,rows:int,cols:int,num_of_mines:int,num_of_cells):
        self.MINE_TOTAL=num_of_mines
        self.ROWS=rows
        self.COLS=cols
        self.CELL_TOTAL=num_of_cells
        self.opened_cells=0
        #each cell has three data:num of adjacent mines/mine presence, opened status, flagged status)
        self.field=[[[-1,-1,-1] for i in range(self.COLS)]for j in range(self.ROWS)]
        self.end=False
        
    def __str__(self):
        field=""
        if self.end:#when game over or win
            for r in range(self.ROWS):
                single_row="|"
                for c in range(self.COLS):
                    x=str(self.field[r][c][0])
                    single_row+=x+'|'
                single_row+="\n"
                field+=single_row
            return field
        #when the game hasn't ended
        for r in range(self.ROWS):
            single_row="|"
            for c in range(self.COLS):
                if self.field[r][c][1]==-1:
                    if self.field[r][c][2]=="F":
                        x="F" 
                    else:
                        x=" "
                      
                else:
                    x=str(self.field[r][c][0])
                single_row+=x+'|'
            single_row+="\n"
            field+=single_row
        return field  
        
    def set_up_field(self,first_chosen_cell:tuple[int:int])->list:
        
        self.field=self.plant_mines(self.MINE_TOTAL,self.field,first_chosen_cell)
        self.field=self.write_mine_nums(self.field,self.ROWS,self.COLS)  

    def plant_mines(self,mine_total:int, field:list,first_chosen_cell):
        for i in range(mine_total):
            r,c=self.get_cell(self.ROWS,self.COLS,field,first_chosen_cell)
            field[r][c][0]='M'
        return field
    
    def write_mine_nums(self,field:list,rows:int,cols:int)->list:
        for i in range(rows):
            for j in range(cols):
                if field[i][j][0]=='M':
                    continue
                field[i][j][0]=self.count_mine(i,j,rows,cols)
        return field
        

    def get_cell(self,rows:int,cols:int,field:list,first_chosen_cell:tuple[int:int])->tuple[int,int]:
        r,c=random.randint(0,rows-1),\
                random.randint(0,cols-1)
        while field[r][c][0]=='M'or (r==first_chosen_cell[0] and c==first_chosen_cell[1]):
            r,c=random.randint(0,rows-1),\
                random.randint(0,cols-1)
        return r,c
    
    def count_mine(self,r:int,c:int,rows:int,cols:int)->int:
        num=0
        for i in range(max(r-1,0),min(r+1,rows-1)+1):
            for j in range(max(c-1,0),min(c+1,cols-1)+1):
                if self.field[i][j][0]=='M':
                    num+=1
        return num
    def check_endgame(self,field:list,cell:tuple[int:int]) -> bool:
        if field[cell[0]][cell[1]][0]=='M':
            print("You opened a mine cell.\nGame over.")
            return True
    
        elif self.opened_cells+self.MINE_TOTAL==self.CELL_TOTAL:
            print("Congraduations. You win.")
            return True
        return False
       
            

    def open(self,cell:tuple,field:list)->list:
        if self.opened_cells==0:#ensure the player won't open bomb cell at the first round.
           self.set_up_field(cell)
        self.opened_cells+=1
        field[cell[0]][cell[1]][1]="O"
        if field[cell[0]][cell[1]][0]==0:
            field=self.open_adjacent_cells(cell[0],cell[1],field)
        return field
         
    def flag(self,cell:tuple,field:list)->list:
            field[cell[0]][cell[1]][2]="F"
            return field
        
    def open_adjacent_cells(self,row:int,col:int,field:list)->list:
        for i in range(max(0,row-1),min(row+1,self.ROWS-1)+1):
            for j in range(max(0,col-1),min(col+1,self.COLS-1)+1):
                if not (field[i][j][1]=="O"):
                    field=self.open((i,j),field)
        return field
                
                   

            


            

            

        


            

        

