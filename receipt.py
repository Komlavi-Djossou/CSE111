import csv
# from datetime import datetime
import time
# timestamp = 1528797322
# date_time = datetime.fromtimestamp(timestamp)
# d = date_time.strftime("%c")
print('KD STORE')

def main():

    # call the read_products function in order to print out the 
    # content of the products dictionary
    products = read_products()


    print(products)

    # call the products_request function in order to print out the 
    # content of the items requested on the request.csv file
    process_request(products)


def read_products():
    try:

        products = {}
    # open a csv file
        with open("products.csv", "rt") as csv_file:
        # read the content of the csv file  
            reader = csv.reader(csv_file)
        # skip the first line in the list because it contains column headings.
            next(reader)  

        # Read each row in the csv file, one row at a time.
            for row in reader:

                product = row[0]
                name = row[1]
                price = float(row[2])

        # store the data in the products dictionary
                products[product] = [name, price]          

     # Include a try block and except blocks to handle 
    # FileNotFoundError, PermissionError, and KeyError.               
    except FileNotFoundError as file_not_found_err:
        print(f"Error: cannot open your file"
                    " because it doesn't exist.")
                    
    except PermissionError as perm_err:
        print(f"Error: cannot read from your file"
                    " because you don't have permission.")

    return products        
def process_request(products): 
    try:
    # open as file named request.csv
        with open('request.csv', 'rt') as csv_file:
                # read the content of the request.csv file
            reader = csv.reader(csv_file)
                # skip the first line in the list because it contains column headings
            next(reader)
                # read and process each row from the request.csv 

            number_of_item = 0
            subtotal = 0
            sale_tax_rate = 0.06
            discount = 0.30
            credit_card_amount = 50
                
            for row in reader: 
                key = row[0]
                quantity = int(row[1])
                

                if key in products:
                    product = products[key]
                        # print()
                    print(f'{product[0]}: {quantity} @ {product[1]}')
                
                    number_of_item = number_of_item + quantity
                        # Calculate the subtotal
                    subtotal = subtotal + (quantity * product[1])
                        # calculate the sales tax
                    sale_tax = subtotal * sale_tax_rate
                    # calculate the total of the expenses
                    total = subtotal + sale_tax
                    # calcluate the total amount  after the discount
                    discount_amount = (total * 30) / 100
                    total_amount = total - discount_amount
                    # calculate the remaining balance on the credit card
                    account_balance = credit_card_amount - total_amount

            
        print()
            # print the number of item
        print(f'Number of Items: {number_of_item}')
            # print out the valuee of the subtotal
        print(f'Subtotal: {subtotal}')
            # print out the sales tax
        print(f'Sales Tax: {sale_tax:.2f}')
            # print out the total
        print(f'Total: {total:.2f}')
        # print total amount after the discount
        print(f'Total_amount: {total_amount:.2f}')
        # print remaining money on the account
        print(f"The account balance: ${account_balance:.2f}")
        print('Thank you for shopping at the KD STORE.')
        # print(d)
        print(time.strftime("%a, %d %b %Y %H:%M:%S"))	
    # Include a try block and except blocks to handle 
    # FileNotFoundError, PermissionError, and KeyError.
    except KeyError as key_err:
        print('Sorry you have entered the wrong key')

    except FileNotFoundError as file_not_found_err:
        print(f"Error: cannot open your file"
                " because it doesn't exist.")
                
    except PermissionError as perm_err:
        print(f"Error: cannot read from your file"
                " because you don't have permission.")
    except ZeroDivisionError as zero_div_err:
        print("Sorry, you have entered zero as division number")

# Call main to start this program.
if __name__ == "__main__":
    main() 