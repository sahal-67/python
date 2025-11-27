
current_year=int(input("enter the current year: "))
end_year = int(input("Enter the ending year: "))
check=False

                   
for year in range(current_year, end_year+1):
    if(year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print(year)
        check=True

        
if (check==False):
        print("there is no leap year.")
