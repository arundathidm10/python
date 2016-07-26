from math import gcd
from munkres import Munkres, make_cost_matrix

class SuitabilityScoreEntry:
   
    def __init__(self, customer_name, product_name, suitability_score):
        self.customer_name = customer_name
        self.product_name = product_name
        self.suitability_score = suitability_score
   
    def get_customer_name(self):
        return self.customer_name

    def get_product_name(self):
        return self.product_name

    def get_suitability_score(self):
        return self.suitability_score


  
class SuitabilityScore:
     
    @staticmethod 
    def calculate_suitability_score(customer,product):
        '''
        returns the calculated suitability score for the given
        customer and product
        '''
         
        suitability_score_value = 0
         
        customer_length = SuitabilityScore.count_letters(customer)
        product_length =  SuitabilityScore.count_letters(product)

        if product_length % 2 == 0:
            suitability_score_value = SuitabilityScore.count_vowels(customer) * 1.5
        else:
            suitability_score_value = customer_length - SuitabilityScore.count_vowels(customer)
        if gcd(customer_length,product_length) != 1:
            suitability_score_value *= 1.5

        return suitability_score_value

    @staticmethod    
    def get_suitability_score(customer_list, product_list):
        '''
        calculate the total maximum suitability score
        by using munkres algorithm and returns a detailed
        customer_product_enties & total suitability score
        '''
        suitability_scores = []
        customer_suitability_scores = []

        for customer in customer_list:
            for product in product_list:
                customer_suitability_scores.append(SuitabilityScore.calculate_suitability_score(customer,product))
            suitability_scores.append(customer_suitability_scores)
            customer_suitability_scores = []


        customer_product_entries = []
        cost_matrix = make_cost_matrix(suitability_scores, lambda cost: 1e10 - cost)
        munkres = Munkres()
        indexes = munkres.compute(cost_matrix)
        total_suitability_score = 0
        for customer_index, product_index  in indexes:
            suitability_score = suitability_scores[customer_index][product_index]
            total_suitability_score += suitability_score
            suitability_score_entry = SuitabilityScoreEntry(customer_list[customer_index],product_list[product_index],suitability_score)
            customer_product_entries.append(suitability_score_entry)
            #print(customer_index,product_index)

        return customer_product_entries,total_suitability_score

    @staticmethod 
    def count_letters(name):
        '''
        returns the number of letters in the string
        '''
        
        count = 0
        for c in name.lower():
            if c.isalpha():
                count += 1
        return count

    @staticmethod
    def count_vowels(name):
        '''
        returns the number of vowels in the string
        '''
        
        vowels = "aeiouy"
        count = 0
        for i in name.lower():
            if i in  vowels:
                 count +=1
        return count
