from budget import*
import unittest



class BasicTest(unittest.TestCase):
  
    # make sure that all the words in the lexicon are recognized
    def testTotal(self):

        #Please enter two items in the list as follows:car-$40-2 and bag-$30-3
        b=Budget()
        b.setBudget(400)
        b.getItems()
        b.CostList()
        self.assertEqual(b.Total(), 170)

    def testTotalCostList(self):
        #Please enter three items in the list as follows:car-$10-2 ,bag-$50-3,and sweet-$7-4
        b=Budget()
        b.setBudget(200)
        b.getItems()
        self.assertEqual(b.CostList(), [20,150,28])

    def testExceedsBudget(self):
        #Please enter three items in the list as follows:car-$10-2 ,bag-$50-3,and sweet-$7-5
        b=Budget()
        b.setBudget(200)
        b.getItems()
        b.CostList()
        b.Total()
        self.assertEqual(b.itemChecker(),True)

    def testEqualToBudget(self):
        #Please enter two items in the list as follows:car-$100-1 ,bag-$50-3,and sweet-$7-5
        b=Budget()
        b.setBudget(200)
        b.getItems()
        b.CostList()
        b.Total()
        self.assertEqual(b.itemChecker(),False)
    def testPercentages(self):
        #Please enter two items in the list as follows:car-$30-1 and bag-$50-2
        b=Budget()
        b.setBudget(200)
        b.getItems()
        b.CostList()
        b.Total()
        b.itemChecker()
        self.assertEqual(b.getPercentage(),[23.08,76.92])
    
    def testPercentageDoesNotAutomaticallyFixExceedingBudget(self):
        #Please enter three items in the list as follows:car-$10-2 ,bag-$50-3,and sweet-$7-5
        b=Budget()
        b.setBudget(200)
        b.getItems()
        b.CostList()
        b.Total()
        b.itemChecker()
        self.assertEqual(b.getPercentage(),[9.76,73.17,17.07])

    def testBelowBudget(self):
        #Please enter three items in the list as follows:car-$10-2,bag-$50-3 and sweet-$3-6
        b=Budget()
        b.setBudget(200)
        b.getItems()
        b.CostList()
        b.Total()
        self.assertEqual(b.itemChecker(),False)"""
        
        


if __name__ == '__main__':
    unittest.main()
