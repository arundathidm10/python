import sys,os
import unittest
from lib.suitabilityscore import SuitabilityScore, SuitabilityScoreEntry

def load_test_cases(input_file):
     '''
     reads all the lines in the input file
     into input_lines_list
     and makes sure it ignores all the lines
     that just have new line characters
     '''

     input_lines_list = []
     while True:
          line = input_file.readline()
          if '\n' == line:
               continue
          elif "" == line:
               #print ("end of file !")
               break
          else:
               line = line.strip()
               if "" == line:
                    break
               else:
                    input_lines_list.append(line)
     return input_lines_list


     
def parse_input_line(line):
     '''
     separate the customers names & the product names
     create a list of customer names
     create a list of product names
     '''  
     separated_list = line.split(";")
     customer_list = separated_list[0].split(",")
     product_list = separated_list[1].split(",")


     return (customer_list,product_list)


    
def print_entries(customer_product_entries,total_suitability_score):
    '''
    prints a list where each entry in the list contains a list 
    [customer,product] that he is likely to buy
    based on the suitability score
    '''
    
    for entry in customer_product_entries:
        entry_tuple = (entry.get_customer_name(),entry.get_product_name(),entry.get_suitability_score())
        print(entry_tuple)

    print("The total suitabilty score is: " + str(total_suitability_score) + "\n")

def get_file():
     '''
     returns a file name
     either from command line argument
     or aks the user to input a file name
     '''
     while True:
          
         if len(sys.argv) == 1:
             file_name = input('Enter the file name: ')
             return file_name
         elif len(sys.argv) == 2:
             file_name = sys.argv[1]
             return file_name
         else:
             os.listdir()
            #continue
            #ask for file name again

    
def main():
    try:
        file_name = open(get_file(),'r')
    except FileNotFoundError:
        print("File is not found in the current directory")
        print(os.listdir())
        sys(exit(0))
        
    input_lines_list = load_test_cases(file_name)

    if len(input_lines_list) == 0:
        print("File is empty, exiting.")
        sys(exit(0))

    for input_line in input_lines_list:
         customer_list, product_list = parse_input_line(input_line)
         customer_product_entries, total_suitability_score = SuitabilityScore.get_suitability_score(customer_list,product_list)
         print_entries(customer_product_entries,total_suitability_score)

    file_name.close()

main()



