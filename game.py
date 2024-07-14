from Minefield import Minefield

def check_opened_cells(row,col,displayed_field):
        have_except=check_exceptions(row,col,displayed_field)
        if have_except:
             return False
             
        if displayed_field[row][col][0]!='*':
             print("The cell is already opened.")
             return False
        return True

def check_flagged_cells(row,col,displayed_field):
     have_except=check_exceptions(row,col,displayed_field)
     if have_except:
        return False
     not_opened=check_opened_cells(row,col,displayed_field)
     if not not_opened:
        return False
           
     if displayed_field[row][col][1]=='F':
             print("The cell is already flagged.")
             return False
     return True

def check_exceptions(row,col,displayed_field):
    try:
        displayed_field[row][col]
    except IndexError:
         print("The cell doesn't exist.")
         return True
    except TypeError:
         print("The row and col must be int.")
         return True
    else:
         return False

          
          
      
def input_cell_to_be_opened():
    print("Please enter a cell to open.")
    row=int(input("Cell row: "))
    col=int(input("Cell column: "))
    valid=check_opened_cells(row,col,minefield.displayed_field)
    while not valid:
        print("Please enter a cell to open.")
        row=int(input("Cell row: "))
        col=int(input("Cell column: "))
        valid=check_opened_cells(row,col,minefield.displayed_field)
    return row,col

def input_cell_to_be_flagged():
    print("Please enter a cell to flag")
    row=int(input("Cell row: "))
    col=int(input("Cell column: "))
    valid=check_flagged_cells(row,col,minefield.displayed_field)
    while not valid:
        print("Please enter a cell to flag")
        row=int(input("Cell row: "))
        col=int(input("Cell column: "))
        valid=check_flagged_cells(row,col,minefield.displayed_field)
    return row,col


print("Welcome to Minesweeper.")
minefield=Minefield((4,5),7)
end=False
while not end:
    row,col=input_cell_to_be_opened()
    f_row,f_col=input_cell_to_be_flagged()
    end=minefield.check_endgame(row,col)
    if not end:
         minefield.display_field()

minefield.display_all_cells()


    
    
    



    