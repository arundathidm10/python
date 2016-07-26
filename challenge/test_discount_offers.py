import unittest
import discount_offers
from lib.suitabilityscore import SuitabilityScore, SuitabilityScoreEntry


class SuitabilityScoreTests(unittest.TestCase):
    def test_count_letters(self):    
        self.assertEqual(SuitabilityScore.count_letters("?abc1#"),3)
        self.assertEqual(SuitabilityScore.count_letters("John Doe"),7)
        self.assertEqual(SuitabilityScore.count_letters(""),0)

    def test_count_vowels(self):
        self.assertEqual(SuitabilityScore.count_vowels("aAeEiIoOuUyY"),12)
        self.assertEqual(SuitabilityScore.count_vowels("bBcCdDfF"),0)
        self.assertEqual(SuitabilityScore.count_vowels(""),0)
        self.assertEqual(SuitabilityScore.count_vowels("b B c  C d D f F"),0)
        

    def test_calculate_suitability_score(self):
        even_product_name = "milk"
        odd_product_name = "tea"
        one_vowel_name_common_factor = "John"
        one_vowel_name_no_common_factor = "Lex"
        one_consonant_name_common_factor = "bei"
        one_consonant_name_no_common_factor = "be"
        no_vowel_name = "tbn"
        no_consonant_name = "aei"
        
        self.assertEqual(SuitabilityScore.calculate_suitability_score(one_vowel_name_common_factor,even_product_name),2.25)
        self.assertEqual(SuitabilityScore.calculate_suitability_score(one_vowel_name_no_common_factor,even_product_name),1.5)
        self.assertEqual(SuitabilityScore.calculate_suitability_score(one_consonant_name_common_factor,odd_product_name),1.5)
        self.assertEqual(SuitabilityScore.calculate_suitability_score(one_consonant_name_no_common_factor,odd_product_name),1)
        self.assertEqual(SuitabilityScore.calculate_suitability_score(no_vowel_name,even_product_name),0)
        self.assertEqual(SuitabilityScore.calculate_suitability_score(no_consonant_name,odd_product_name),0)

    def test_get_suitability_score(self):
         customers_list1 = ['AB','BC','CD']
         customers_list2 = ['Peter','Ali','Smith']
         customers_list3 = ['first','second','third','fourth']

         products_list1 = ['x','y','z']
         products_list2 = ['one','two','three','four']
         products_list3 = ['product one','product two', 'product three']

         list1,total_suitability_score_1 = SuitabilityScore.get_suitability_score(customers_list1,products_list1)
         list2,total_suitability_score_2 = SuitabilityScore.get_suitability_score(customers_list2,products_list2)
         list3,total_suitability_score_3 = SuitabilityScore.get_suitability_score(customers_list3,products_list3)
        
         self.assertEqual(total_suitability_score_1,5)
         self.assertEqual(total_suitability_score_2,12)
         self.assertEqual(total_suitability_score_3,11.25)

         self.assertEqual(list1[0].customer_name,'AB')
         self.assertEqual(list1[0].product_name,'x')
         self.assertEqual(list1[0].suitability_score,1)
         self.assertEqual(list2[1].customer_name,'Ali')
         self.assertEqual(list2[1].product_name,'four')
         self.assertEqual(list2[1].suitability_score,3)
         self.assertEqual(list3[2].customer_name,'fourth')
         self.assertEqual(list3[2].product_name,'product three')
         self.assertEqual(list3[2].suitability_score,4.5)
         
    def test_load_test_cases(self):

        file = open('test.txt','r')
        input_lines_expected = ['a,b,c','d,e,f','g,h,i']
        self.assertEqual(discount_offers.load_test_cases(file),input_lines_expected)
        file.close()


    def test_parse_input_line(self):
        line_one = "A,B,C;one,two,three"
        line_two = "user1,user2;pr1,pr2,pr3"

        customers_list_one, products_list_one = discount_offers.parse_input_line(line_one)
        customers_list_two, products_list_two = discount_offers.parse_input_line(line_two)
        
        self.assertEqual(customers_list_one,['A','B','C'])
        self.assertEqual(customers_list_two,['user1','user2'])
        self.assertEqual(products_list_one,['one','two','three'])
        self.assertEqual(products_list_two,['pr1','pr2','pr3'])
          
#print(discount_offers.count_letters("asasa"))
unittest.main()
