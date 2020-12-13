#This GUI is about online sales of the past three years

# I know the months are very repetitive but after I have already coded them, I was too lazy to change the code but it still functions like supposed to! 
# Kept me busy during quarentine! But sorry for the ugly code!
# Please use the month_sales.csv and item sales.csv please.
#This code will write you a new csv. It is formatted professionally and nice.
#Thank you for the semster sir. See you soon for 515.


import csv
import tkinter
import tkinter.messagebox
import tkinter.ttk



#Start coding the def functions and with both files open, may need to create a write file. 
totals_list = []
item_totals = []
new_list = []

def sales():
    """This function is for the average online sales."""
    global year_box, to_box, start_box, item1_box, item2_box, item3_box
    
    try:
        with open("month_sales.csv", "r") as file, open("item sales.csv", "r") as file_2, open("calculations.csv", "w") as file_3:
            reader = csv.reader(file)
            reader_2 = csv.reader(file_2)
            writer = csv.writer(file_3, lineterminator = "\n")
            
            month_rows = list(reader)       
            jan_total = (month_rows[1][7])
            feb_total = (month_rows[5][7])
            mar_total = (month_rows[9][7])
            april_total = (month_rows[13][7])
            may_total = (month_rows[17][7])     #this block converts the totals of the months in past 3 months but just the sum
            june_total = (month_rows[21][7])
            july_total = (month_rows[25][7])
            aug_total = (month_rows[29][7])
            sep_total = (month_rows[33][7])
            oct_total = (month_rows[37][7])
            nov_total = (month_rows[41][7])
            dec_total = (month_rows[45][7])
            
            totals_list.append(jan_total)
            totals_list.append(feb_total)
            totals_list.append(mar_total)
            totals_list.append(april_total)
            totals_list.append(may_total)
            totals_list.append(june_total)   #this block appends the strings to list
            totals_list.append(july_total)
            totals_list.append(aug_total)
            totals_list.append(sep_total)
            totals_list.append(oct_total)
            totals_list.append(nov_total)
            totals_list.append(dec_total)
            
            month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            
            make_digit = list(map(float,totals_list))  #converts to digits
            
            item_rows = list(reader_2)
            
            acc_totals = (item_rows[1][5])
            art_totals = (item_rows[2][5])
            basket_totals = (item_rows[3][5])
            christmas_totals = (item_rows[4][5])
            easter_totals = (item_rows[5][5])
            fair_totals = (item_rows[6][5])
            furniture_totals = (item_rows[7][5])
            gift_totals = (item_rows[8][5])        #code block gets the totals in the csv 
            home_totals = (item_rows[9][5])
            jewelry_totals = (item_rows[10][5])
            kids_totals = (item_rows[11][5])
            kitchen_totals = (item_rows[12][5])
            music_totals = (item_rows[13][5])
            one_totals = (item_rows[14][5])
            recycled_totals = (item_rows[15][5])
            skin_totals = (item_rows[16][5])
            soap_totals = (item_rows[17][5])
            text_totals = (item_rows[18][5])
            
            item_totals.append(acc_totals)
            item_totals.append(art_totals)
            item_totals.append(basket_totals)
            item_totals.append(christmas_totals)
            item_totals.append(easter_totals)
            item_totals.append(fair_totals)
            item_totals.append(furniture_totals)    # block gets the totals and append them all to one list
            item_totals.append(gift_totals)
            item_totals.append(home_totals)
            item_totals.append(jewelry_totals)
            item_totals.append(kids_totals)
            item_totals.append(kitchen_totals)
            item_totals.append(music_totals)
            item_totals.append(one_totals)
            item_totals.append(recycled_totals)
            item_totals.append(skin_totals)
            item_totals.append(soap_totals)
            item_totals.append(text_totals)
            
            item_int = list(map(float,item_totals))   #converts them into ints
            
            row_1 = ["Online", "Business", "sales data", "are from", "the past", "three years."]
            writer.writerow(row_1)
            
            row_2 = ["Your input", "averages are", "below:"]
            writer.writerow(row_2)
            
            row_3 = ["", ""]
            writer.writerow(row_3)
            
            # Month selection possibilities below
            try:
                #January
                if start_box.get() == "January":
                    if to_box.get() == "January":
                        total = make_digit[0]
                        row_4 = ["Total sales", "of", "January:", "$", total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "February":
                        total = make_digit[0] + make_digit[1]
                        row_4 = ["Total","from January", "to February:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "March":
                        total = make_digit[0] + make_digit[1] + make_digit[2]
                        row_4 = ["Total","from January", "to March:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "April":
                        total = make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3]
                        row_4 = ["Total","from January", "to April:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "May":
                        total = make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4]
                        row_4 = ["Total","from January", "to May:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "June":
                        total = make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5]
                        row_4 = ["Total","from January", "to June:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "July":
                        total = make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6]
                        row_4 = ["Total","from January", "to July:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "August":
                        total = make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7]
                        row_4 = ["Total","from January", "to August:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "September":
                        total = make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8]
                        row_4 = ["Total","from January", "to September:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "October":
                        total = make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9]
                        row_4 = ["Total","from January", "to October:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "November":
                        total = make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10]
                        row_4 = ["Total","from January", "to November:", "$",total]
                        writer.writerow(row_4)
                    
                    else:
                        total = make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11]
                        row_4 = ["Total","from January", "to December:", "$",total]
                        writer.writerow(row_4)
                
                #February
                if start_box.get() == "February":
                    
                    if to_box.get() == "February":
                        total = make_digit[1]
                        row_4 = ["Total sales", "of", "February:", "$", total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "March":
                        total = make_digit[1] + make_digit[2]
                        row_4 = ["Total","from February", "to March:", "$",total]
                        writer.writerow(row_4)
                
                    elif to_box.get() == "April":
                        total =   make_digit[1] + make_digit[2] + make_digit[3]
                        row_4 = ["Total","from February", "to April:", "$",total]
                        writer.writerow(row_4)
                
                    elif to_box.get() == "May":
                        total = make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4]
                        row_4 = ["Total","from February", "to May:", "$",total]
                        writer.writerow(row_4)
                
                    elif to_box.get() == "June":
                        total =  make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5]
                        row_4 = ["Total","from February", "to June:", "$",total]
                        writer.writerow(row_4)
                
                    elif to_box.get() == "July":
                        total = make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6]
                        row_4 = ["Total","from February", "to July:", "$",total]
                        writer.writerow(row_4)
                
                    elif to_box.get() == "August":
                        total = make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7]
                        row_4 = ["Total","from February", "to August:", "$",total]
                        writer.writerow(row_4)
                
                    elif to_box.get() == "September":
                        total = make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8]
                        row_4 = ["Total","from February", "to September:", "$",total]
                        writer.writerow(row_4)
                
                    elif to_box.get() == "October":
                        total = make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9]
                        row_4 = ["Total","from February", "to October:", "$",total]
                        writer.writerow(row_4)
                
                    elif to_box.get() == "November":
                        total = make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10]
                        row_4 = ["Total","from February", "to November:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "December":
                        total = make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11]
                        row_4 = ["Total","from February", "to December:", "$",total]
                        writer.writerow(row_4)
                    else:
                        total = make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11]
                        row_4 = ["Total","from February", "to January:", "$",total]
                        writer.writerow(row_4)

                        

                #March
                if start_box.get() == "March":
                    
                    if to_box.get() == "March":
                        total = make_digit[2]
                        row_4 = ["Total sales", "of", "March:", "$", total]
                        writer.writerow(row_4)
                        
                    elif to_box.get() == "April":
                        total = make_digit[2] + make_digit[3]
                        row_4 = ["Total","from March", "to April:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "May":
                        total = make_digit[2] + make_digit[3] + make_digit[4]
                        row_4 = ["Total","from March", "to May:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "June":
                        total = make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5]
                        row_4 = ["Total","from March", "to June:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "July":
                        total = make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6]
                        row_4 = ["Total","from March", "to July:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "August":
                        total = make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7]
                        row_4 = ["Total","from March", "to August:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "September":
                        total = make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8]
                        row_4 = ["Total","from March", "to September:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "October":
                        total = make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9]
                        row_4 = ["Total","from March", "to October:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "November":
                        total = make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10]
                        row_4 = ["Total","from March", "to November:", "$",total]
                        writer.writerow(row_4)
                    
                    
                    elif to_box.get() == "December":
                        total = make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11]
                        row_4 = ["Total","from March", "to December:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "January":
                        total = make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0]
                        row_4 = ["Total","from March", "to January:", "$",total]
                        writer.writerow(row_4)
                    
                    else:
                        total = make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0]+ make_digit[1]
                        row_4 = ["Total","from March", "to February:", "$",total]
                        writer.writerow(row_4)
                    
                        
                        
                    
                #April
                if start_box.get() == "April":
                    
                    if to_box.get() == "April":
                        total = make_digit[3]
                        row_4 = ["Total sales", "of", "April:", "$", total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "May":
                        total = make_digit[3] + make_digit[4]
                        row_4 = ["Total","from April", "to May:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "June":
                        total = make_digit[3] + make_digit[4] + make_digit[5]
                        row_4 = ["Total","from April", "to June:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "July":
                        total = make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6]
                        row_4 = ["Total","from April", "to July:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "August":
                        total = make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7]
                        row_4 = ["Total","from April", "to August:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "September":
                        total = make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8]
                        row_4 = ["Total","from April", "to September:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "October":
                        total = make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9]
                        row_4 = ["Total","from April", "to October:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "November":
                        total = make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10]
                        row_4 = ["Total","from April", "to November:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "December":
                        total = make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11]
                        row_4 = ["Total","from April", "to December:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "January":
                        total = make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0]
                        row_4 = ["Total","from April", "to January:", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "February":
                        total = make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1]
                        row_4 = ["Total","from April", "to February:", "$",total]
                        writer.writerow(row_4)
                    
                    else:
                        total = make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2]
                        row_4 = ["Total","from April", "to March:", "$",total]
                        writer.writerow(row_4)
                        
                        
            
                #May
                if start_box.get() == "May":
                    
                    if to_box.get() == "May":
                        total = make_digit[4]
                        row_4 = ["Total sales", "of", "May:", "$", total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "June":
                        total = make_digit[4] + make_digit[5]
                        row_4 = ["Total","from May", "to June:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "July":
                        total = make_digit[4] + make_digit[5] + make_digit[6]
                        row_4 = ["Total","from May", "to July:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "August":
                        total = make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7]
                        row_4 = ["Total","from May", "to August:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "September":
                        total = make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8]
                        row_4 = ["Total","from May", "to September:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "October":
                        total = make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9]
                        row_4 = ["Total","from May", "to October:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "November":
                        total = make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10]
                        row_4 = ["Total","from May", "to November:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "December":
                        total = make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11]
                        row_4 = ["Total","from May", "to December:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "January":
                        total = make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0]
                        row_4 = ["Total","from May", "to January:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "February":
                        total = make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1]
                        row_4 = ["Total","from May", "to February:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "March":
                        total = make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2]
                        row_4 = ["Total","from May", "to March:", "$",total]
                        writer.writerow(row_4)
                    else:
                        total = make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3]
                        row_4 = ["Total","from May", "to April:", "$",total]
                        writer.writerow(row_4)
                        
                
                   
                #June
                if start_box.get() == "June":
                    
                    if to_box.get()== "June":
                        total = make_digit[5]
                        row_4 = ["Total sales", "of", "June:", "$", total]
                        writer.writerow(row_4)
                        
                    elif to_box.get() == "July":
                        total = make_digit[5] + make_digit[6]
                        row_4 = ["Total","from June", "to July:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "August":
                        total = make_digit[5] + make_digit[6] + make_digit[7]
                        row_4 = ["Total","from June", "to August:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "September":
                        total = make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8]
                        row_4 = ["Total","from June", "to September:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "October":
                        total = make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9]
                        row_4 = ["Total","from June", "to October:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "November":
                        total = make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10]
                        row_4 = ["Total","from June", "to November:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "December":
                        total = make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11]
                        row_4 = ["Total","from June", "to December:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "January":
                        total = make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0]
                        row_4 = ["Total","from June", "to January:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "February":
                        total = make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1]
                        row_4 = ["Total","from June", "to February:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "March":
                        total = make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2]
                        row_4 = ["Total","from June", "to March:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "April":
                        total = make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3]
                        row_4 = ["Total","from June", "to April:", "$",total]
                        writer.writerow(row_4)
                    else:
                        total = make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4]
                        row_4 = ["Total","from June", "to May:", "$",total]
                        writer.writerow(row_4)
                          
        
                #July
                if start_box.get() == "July":
                    
                    if to_box.get() == "July":
                        total = make_digit[6]
                        row_4 = ["Total sales", "of", "July:", "$", total]
                        writer.writerow(row_4)
                        
                    elif to_box.get() == "August":
                        total = make_digit[6] + make_digit[7]
                        row_4 = ["Total","from July", "to August:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "September":
                        total = make_digit[6] + make_digit[7] + make_digit[8]
                        row_4 = ["Total","from July", "to September:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "October":
                        total = make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9]
                        row_4 = ["Total","from July", "to October:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "November":
                        total = make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10]
                        row_4 = ["Total","from July", "to November:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "December":
                        total = make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11]
                        row_4 = ["Total","from July", "to December:", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "January":
                        total = make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0]
                        row_4 = ["Total","from July", "to January:", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "February":
                        total = make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1]
                        row_4 = ["Total","from July", "to February:", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "March":
                        total = make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2]
                        row_4 = ["Total","from July", "to March:", "$",total]
                        writer.writerow(row_4)
                        
                    elif to_box.get() == "April":
                        total = make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3]
                        row_4 = ["Total","from July", "to April:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "May":
                        total = make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4]
                        row_4 = ["Total","from July", "to May:", "$",total]
                        writer.writerow(row_4)
                        
                    else:
                        total = make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5]
                        row_4 = ["Total","from July", "to June:", "$",total]
                        writer.writerow(row_4)        
                        
                        
                #August
                if start_box.get() == "August":
                    if to_box.get() == "August":
                        total = make_digit[7]
                        row_4 = ["Total sales", "of", "August:", "$", total]
                        writer.writerow(row_4)
                        
                    elif to_box.get() == "September":
                        total = make_digit[7] + make_digit[8]
                        row_4 = ["Total","from August", "to September:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "October":
                        total = make_digit[7] + make_digit[8] + make_digit[9]
                        row_4 = ["Total","from August", "to October:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "November":
                        total = make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10]
                        row_4 = ["Total","from August", "to November:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "December":
                        total = make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11]
                        row_4 = ["Total","from August", "to December:", "$",total]
                        writer.writerow(row_4)
                        
                    elif to_box.get() == "January":
                        total = make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0]
                        row_4 = ["Total","from August", "to January:", "$",total]
                        writer.writerow(row_4)
                        
                    elif to_box.get() == "February":
                        total = make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1]
                        row_4 = ["Total","from August", "to February:", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "March":
                        total = make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2]
                        row_4 = ["Total","from August", "to March:", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "April":
                        total = make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3]
                        row_4 = ["Total","from August", "to April:", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "May":
                        total = make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4]
                        row_4 = ["Total","from August", "to May:", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "June":
                        total = make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5]
                        row_4 = ["Total","from August", "to June:", "$",total]
                        writer.writerow(row_4)
                    else:
                        total = make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6]
                        row_4 = ["Total","from August", "to July:", "$",total]
                        writer.writerow(row_4)
                    
                        
                        
                        
                #September
                if start_box.get() == "September":
                    
                    if to_box.get() == "September":
                        total = make_digit[8]
                        row_4 = ["Total sales", "of", "September:", "$", total]
                        writer.writerow(row_4)
        
                    elif to_box.get() == "October":
                        total = make_digit[8] + make_digit[9]
                        row_4 = ["Total","from September", "to October:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "November":
                        total = make_digit[8] + make_digit[9] + make_digit[10]
                        row_4 = ["Total","from September", "to November:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "December":
                        total = make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11]
                        row_4 = ["Total","from September", "to December:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "January":
                        total = make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0]
                        row_4 = ["Total","from September", "to January:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "February":
                        total = make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1]
                        row_4 = ["Total","from September", "to February", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "March":
                        total = make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2]
                        row_4 = ["Total","from September", "to March", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "April":
                        total = make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3]
                        row_4 = ["Total","from September", "to April", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "May":
                        total = make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4]
                        row_4 = ["Total","from September", "to May", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "June":
                        total = make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5]
                        row_4 = ["Total","from September", "to June", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "July":
                        total = make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6]
                        row_4 = ["Total","from September", "to July", "$",total]
                        writer.writerow(row_4)
                    else:
                        total = make_digit[8] + make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7]
                        row_4 = ["Total","from September", "to August", "$",total]
                        writer.writerow(row_4)

                
                
                #October
                if start_box.get() == "October":
                    if to_box.get() == "October":
                        total = make_digit[9]
                        row_4 = ["Total sales", "of", "October:", "$", total]
                        writer.writerow(row_4)

                    if to_box.get() == "November":
                        total = make_digit[9] + make_digit[10]
                        row_4 = ["Total","from October", "to November:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "December":
                        total = make_digit[9] + make_digit[10] + make_digit[11]
                        row_4 = ["Total","from October", "to December:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "January":
                        total = make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0]
                        row_4 = ["Total","from October", "to January:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "February":
                        total = make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1]
                        row_4 = ["Total","from October", "to February:", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "March":
                        total = make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2]
                        row_4 = ["Total","from October", "to March:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "April":
                        total = make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digt[3]
                        row_4 = ["Total","from October", "to April:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "May":
                        total = make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digt[3] + make_digit[4]
                        row_4 = ["Total","from October", "to May:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "June":
                        total = make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digt[3] + make_digit[4] + make_digit[5]
                        row_4 = ["Total","from October", "to June:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "July":
                        total = make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digt[3] + make_digit[4] + make_digit[5] + make_digit[6]
                        row_4 = ["Total","from October", "to July:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "August":
                        total = make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digt[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7]
                        row_4 = ["Total","from October", "to August:", "$",total]
                        writer.writerow(row_4)
                    
                    else:
                        total = make_digit[9] + make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digt[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8]
                        row_4 = ["Total","from October", "to September:", "$",total]
                        writer.writerow(row_4)
                        
                    
                #November
                if start_box.get() == "November":
                    
                    if to_box.get() == "November":
                        total = make_digit[10]
                        row_4 = ["Total sales", "of", "November:", "$", total]
                        writer.writerow(row_4)
                    elif to_box.get() == "December":
                        total = make_digit[10] + make_digit[11]
                        row_4 = ["Total","from November", "to December:", "$",total]
                        writer.writerow(row_4)
                    elif to_box.get() == "January":
                        total = make_digit[10] + make_digit[11] + make_digit[0]
                        row_4 = ["Total","from November", "to January:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "February":
                        total = make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1]
                        row_4 = ["Total","from November", "to February:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "March":
                        total = make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2]
                        row_4 = ["Total","from November", "to March:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "April":
                        total = make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3]
                        row_4 = ["Total","from November", "to April:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "May":
                        total = make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4]
                        row_4 = ["Total","from November", "to May:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "June":
                        total = make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5]
                        row_4 = ["Total","from November", "to June:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "July":
                        total = make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6]
                        row_4 = ["Total","from November", "to July:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "August":
                        total = make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7]
                        row_4 = ["Total","from November", "to August:", "$",total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "September":
                        total = make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8]
                        row_4 = ["Total","from November", "to September:", "$",total]
                        writer.writerow(row_4)
                    else:
                        total = make_digit[10] + make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9]
                        row_4 = ["Total","from November", "to October:", "$",total]
                        writer.writerow(row_4)
                    
                    
                #December
                if start_box.get() == "December":
                    
                    if to_box.get() == "December":
                        total = make_digit[11]
                        row_4 = ["Total sales", "of", "December:", "$", total]
                        writer.writerow(row_4)
                    
                    elif to_box.get() == "January":
                        total = make_digit[11] + make_digit[0]
                        row_4 = ["Total", "from December", "to January:", "$", total]
                        writer.writerow(row_4)
                    elif to_box.get() == "February":
                        total = make_digit[11] + make_digit[0] + make_digit[1]
                        row_4 = ["Total", "from December", "to February:", "$", total]
                        writer.writerow(row_4)
                    elif to_box.get() == "March":
                        total = make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2]
                        row_4 = ["Total", "from December", "to March:", "$", total]
                        writer.writerow(row_4)
                    elif to_box.get() == "April":
                        total = make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3]
                        row_4 = ["Total", "from December", "to April:", "$", total]
                        writer.writerow(row_4)
                    elif to_box.get() == "May":
                        total = make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4]
                        row_4 = ["Total", "from December", "to May:", "$", total]
                        writer.writerow(row_4)
                    elif to_box.get() == "June":
                        total = make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5]
                        row_4 = ["Total", "from December", "to June:", "$", total]
                        writer.writerow(row_4)
                    elif to_box.get() == "July":
                        total = make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6]
                        row_4 = ["Total", "from December", "to July:", "$", total]
                        writer.writerow(row_4)
                    elif to_box.get() == "August":
                        total = make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7]
                        row_4 = ["Total", "from December", "to August:", "$", total]
                        writer.writerow(row_4)
                    elif to_box.get() == "September":
                        total = make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8]
                        row_4 = ["Total", "from December", "to September:", "$", total]
                        writer.writerow(row_4)
                    elif to_box.get() == "October":
                        total = make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9]
                        row_4 = ["Total", "from December", "to October:", "$", total]
                        writer.writerow(row_4)
                    else:
                        total = make_digit[11] + make_digit[0] + make_digit[1] + make_digit[2] + make_digit[3] + make_digit[4] + make_digit[5] + make_digit[6] + make_digit[7] + make_digit[8] + make_digit[9] + make_digit[10]
                        row_4 = ["Total", "from December", "to November:", "$", total]
                        writer.writerow(row_4)
                
                
                
                #code block below is for the items!
                        
                new_dict = {"Accessories": item_int[0], "Art and Sculpture": item_int[1], "Basket": item_int[2], "Christmas": item_int[3], "Easter": item_int[4], "Fair Trade Gifts": item_int[5], "Furniture": item_int[6] , "Gift Baskets": item_int[7], "Home Decoration": item_int[8], "Jewelry": item_int[9], "Kids": item_int[10], "Kitchen": item_int[11], "Music": item_int[12],"One-of-a-kind": item_int[13], "Recycled Art": item_int[14], "Skin Care": item_int[15], "Soapstone": item_int[16], "Textiles": item_int[17]}
        
        
                access = new_dict.get("Accessories")
                art = new_dict.get("Art and Sculpture")
                bask = new_dict.get("Basket")
                chris = new_dict.get("Christmas")
                easter = new_dict.get("Easter")
                trade = new_dict.get("Fair Trade Gifts")
                furniture = new_dict.get("Furniture")
                gift = new_dict.get("Gift Baskets")
                home = new_dict.get("Home Decoration")
                jewelry = new_dict.get("Jewelry")
                kids = new_dict.get("Kids")
                kitchen = new_dict.get("Kitchen")
                music = new_dict.get("Music")
                kind = new_dict.get("One-of-a-kind")
                skin = new_dict.get("Skin Care")
                soap = new_dict.get("Soapstone")
                textiles = new_dict.get("Textiles")
                
                new_list.append(access)
                new_list.append(art)
                new_list.append(bask)
                new_list.append(chris)
                new_list.append(easter)
                new_list.append(trade)
                new_list.append(furniture)
                new_list.append(gift)
                new_list.append(home)
                new_list.append(jewelry)
                new_list.append(kids)
                new_list.append(kitchen)
                new_list.append(music)
                new_list.append(kind)
                new_list.append(skin)
                new_list.append(soap)
                new_list.append(textiles)
                
                row_5 = ["", ""]
                writer.writerow(row_5)
                row_6 = ["Your three","items", "have been", "ranked based", "on sales", "below:"]
                writer.writerow(row_6)
                
                gap_row = ["",""]
                writer.writerow(gap_row)
                

                while new_list:
                    
                    item_1 = new_dict.get(item1_box.get())
                    item_2 = new_dict.get(item2_box.get())
                    item_3 = new_dict.get(item3_box.get())
                    
                    if item_1 >= item_2 and item_1 >= item_3:
                        row_7 = ["1.", item1_box.get(), "$",item_1]
                        writer.writerow(row_7)
                    
                        if item_2 >= item_3:
                            row_8 = ["2.", item2_box.get(), "$", item_2]
                            row_9 = ["3.", item3_box.get(), "$", item_3]
                            writer.writerow(row_8)
                            writer.writerow(row_9)
                        else:
                            row_8 = ["2.", item3_box.get(), "$", item_3]
                            row_9 = ["3.", item2_box.get(), "$",item_2]
                            writer.writerow(row_8)
                            writer.writerow(row_9)
                        
                        
                    if item_2 >= item_1 and item_2 >= item_3:
                        row_7 = ["1.", item2_box.get(), "$", item_2]
                        writer.writerow(row_7)
                        if item_1 >= item_3:
                            row_8 = ["2.", item1_box.get(), "$",item_1]
                            row_9 = ["3.", item3_box.get(), "$", item_3]
                            writer.writerow(row_8)
                            writer.writerow(row_9)
                        else:
                            row_8 = ["2.", item3_box.get(), "$", item_3]
                            row_9 = ["3.", item1_box.get(), "$",item_1]
                            writer.writerow(row_8)
                            writer.writerow(row_9)
                
                    if item_3 >= item_2 and item_3 >= item_1:
                        row_7 = ["1.", item3_box.get(),"$", item_3]
                        writer.writerow(row_7)
                        if item_2 >= item_1:
                            row_8 = ["2.", item2_box.get(),"$", item_2]
                            row_9 = ["3.", item1_box.get(),"$", item_1]
                            writer.writerow(row_8)
                            writer.writerow(row_9)
                        else:
                            row_8 = ["2.", item1_box.get(), "$", item_1]
                            row_9 = ["3.", item2_box.get(), "$", item_2]
                            writer.writerow(row_8)
                            writer.writerow(row_9)
                                 
            
                    tkinter.messagebox.showinfo("Calculated!", "Your calculations have been recorded in the calculations.csv file.")
                    
                    break
                
                
            except:
                tkinter.messagebox.showwarning("Warning!", "Please check the ending month is in the future of the initial month you are setting.")
    
    
    except:
        tkinter.messagebox.showwarning("Warning!", "Could not get your averages. Please check your files before proceeding.")
        


def quitt():
    """Basic quit function for the quit button."""
    global root
    root.destroy()


root = tkinter.Tk()
root.title("Online Business Sales")
root.configure(bg = "LemonChiffon2")



brief_label = tkinter.Label(root, text = "Welcome! This application will show the average online business sales in the past three years.")
brief_label.configure(bg = "LemonChiffon2")
brief_label.configure(font = "Arial 15 bold")
brief_label.grid(row = 0, column = 1)


start_label = tkinter.Label(root, text = "From: ") #list of months
start_label.configure(bg = "LemonChiffon2")
start_label.grid(row = 1, column = 0, pady = (2,2))


to_label = tkinter.Label(root, text = "To:")
to_label.configure(bg = "LemonChiffon2")
to_label.grid(row = 2, column = 0, pady = (2,2))


which_label = tkinter.Label(root, text = "Which three items of emphasis are you seeking for your online business?") 
which_label.configure(bg = "LemonChiffon2")
which_label.grid(row = 4, column = 0) # going to need a pady to separate sections

end_label = tkinter.Label(root, text = "Select three items of interest:")
end_label.configure(bg = "LemonChiffon2")
end_label.grid(row = 5, column = 0)


selection_label = tkinter.Label(root, text = "Item 1:")
selection_label.configure(bg = "LemonChiffon2")
selection_label.grid(row = 6, column = 0, pady = (2,2))

selection_label2 = tkinter.Label(root, text = "Item 2:")
selection_label2.configure(bg = "LemonChiffon2")
selection_label2.grid(row = 7, column = 0, pady = (2,2))

selection_label3 = tkinter.Label(root, text = "Item 3:")
selection_label3.configure(bg = "LemonChiffon2")
selection_label3.grid(row = 8, column = 0, pady = (2,2))


#.get() from the ones below


start_box = tkinter.ttk.Combobox(root, values = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state = "readonly")
start_box.grid(row = 1, column = 1, pady = (2,2))

to_box = tkinter.ttk.Combobox(root, values = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state = "readonly")
to_box.grid(row = 2, column = 1, pady = (2,2))


item1_box = tkinter.ttk.Combobox(root, values = ["Accessories", "Art and Sculpture", "Basket", "Christmas","Easter", "Fair Trade Gifts","Furniture", "Gift Baskets", "Home Decoration", "Jewelry", "Kids", "Kitchen","Music","One-of-a-kind", "Recycled Art", "Skin Care", "Soapstone", "Textiles"], state = "readonly")
item1_box.grid(row = 6, column = 1, pady = (2,2))

item2_box = tkinter.ttk.Combobox(root, values = ["Accessories", "Art and Sculpture", "Basket", "Christmas","Easter", "Fair Trade Gifts","Furniture", "Gift Baskets", "Home Decoration", "Jewelry", "Kids", "Kitchen","Music","One-of-a-kind", "Recycled Art", "Skin Care", "Soapstone", "Textiles"], state = "readonly")
item2_box.grid(row = 7, column = 1, pady = (2,2))

item3_box = tkinter.ttk.Combobox(root, values = ["Accessories", "Art and Sculpture", "Basket", "Christmas","Easter", "Fair Trade Gifts","Furniture", "Gift Baskets", "Home Decoration", "Jewelry", "Kids", "Kitchen","Music","One-of-a-kind", "Recycled Art", "Skin Care", "Soapstone", "Textiles"], state = "readonly")
item3_box.grid(row = 8, column = 1, pady = (2,2))



calc_button = tkinter.Button(root, text = "Calculate", command = sales)
calc_button.configure(bg = "green")
calc_button.grid(row = 6, column = 2, pady = (2,2))

quit_button = tkinter.Button(root, text = "Quit", command = quitt)
quit_button.configure(bg = "red")
quit_button.grid(row = 7, column = 2, pady = (2,2))


root.mainloop()
