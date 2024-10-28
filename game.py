from Minefield import Minefield
import random,re

def check_user_input(x,lim:int)->bool:
        non_digit=re.search(r'\D',x)
        if non_digit:
            print("you have to enter numbers")
            return False
        x=int(x)     
        if not (0<=x<=lim or -1>=x>=-lim-1):
            print("the row is out of range of the field.")
            return False

            
    
        return True
def prompt_input_cell(rows:int,cols:int)->tuple:
    cell=[None,None]
    index=0
    lim=rows-1
    for coordinate in ("row","column"):
        while True:
           
           print("enter the coordinate of the cell.",coordinate,":")
           user_input=input("type an integer.")
           valid=check_user_input(user_input,lim)
           if valid:
               user_input=int(user_input)
               cell[index]=user_input
               index+=1
               break
        lim=cols-1
        
    return cell

   


if __name__=="__main__":
   print("Welcome to Minesweeper. Please enter the number of rows and columns for the minefield.")
   rows=int(input("enter the number of rows."))
   cols=int(input("enter the number of columns."))
   #set the number of mines as one-third of total cells.
   cell_total=rows*cols
   mine_total=cell_total//5
   minefield=Minefield(rows,cols,mine_total,cell_total)
   while not minefield.end:
       print(minefield)
       actions={"F":"flag","f":"flag","O":"open","o":"open"}
       #prompt user action
       while True:
           action=input("enter your action. \"F\" for flag,\"O\" for open")
           if action not in actions:
               print("you enter a wrong action.") 
           else:
               print("Are you sure you want to ",actions[action],"the cell?")
               confirmed=input("enter \"Y\" or \"N\".")
               if confirmed=="N" or confirmed=="n":
                   continue
               else:
                   break
       
       #prompt user to choose a cell and validate input.
       cell=prompt_input_cell(rows,cols)
       
       if actions[action]=="flag":
           if minefield.field[cell[0]][cell[1]][2]=="F":
               print("This cell has already been flagged.")
           else:
             minefield.field=minefield.flag(cell,minefield.field)
           continue
       else:
           if minefield.field[cell[0]][cell[1]][1]=="O":
               print("This cell has already been opened.")
               continue
           minefield.field=minefield.open(cell,minefield.field)
    
       minefield.end=minefield.check_endgame(minefield.field,cell)
       if minefield.end:
           print(minefield)
       



    
