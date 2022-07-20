#sophia.bahru@slu.edu
#joshitooo.nuka@slu.edu


class Budget():
    """The Budget Class helps users to set up a shopping list that
    supports the amount of the user’s expendable income by displaying
    a table accompanied by percentages that each item takes up in the
    budget.

    The class also aids users choices of items and costs by some one
    step suggestions to ensure that the budget is not exceeded.""" 
    

    def __init__(self):
        """Instantiates various lists that will be used through
        out the implementation of the different methods"""
        
        self.starting_budget=0                                                              #initial budget is zero
        
    
    
    def greeting(self):
        """The initial greeting from the app that determines the title of the
        final budget table"""
        
        print('Welcome to the BudgetApp!')
        self.Budget_Name=input('What would you like the title of your budget to be?')         #budget name
        
    def setBudget(self,income):
        """This function sets up the initial expendable income"""
        
        self.starting_budget=income
  
        
    def getItems(self):
         """This function appends the various item names,costs and amount
         to lists instantiated when the function is called"""
         self.items=[]                                                                        #lists that would keep track of elements
         self.costs=[]
         self.quantity=[]
         self.totalCostlist=[]
    
         number=int(input('How many items do you want in your list?'))
         for i in range(number):
            name=input('\nItem Name: ')
            cost=-1                                                                           #wrong input
            while not 10000>cost>0:                                                           #Error checking.Ensures the cost isn't outside the range
                try:
                    c=input('Cost of item: ')
                    cost=int(c.strip('$'))
                    if not 100000>cost>0:
                        print('Your cost must be non-negative and cannot exceed 5-digits')
                except ValueError:
                    print('Your cost must be a rational number')
            quantity=-1                                                                      #wrong input
            while not 100>quantity>0:                                                        #Ensures the quantity isn't outside the range
                try:
                    quantity=int(input('Item amount: '))
                    if not 100>=quantity>0:
                        print('Your amount must be non-negative and cannot exceed 100')
                except ValueError:
                    print('Your quantity must be a rational number')
            self.items.append(name)
            
            self.costs.append(cost)
             
            self.quantity.append(quantity)
             
            
            
    def CostList(self):
        """This creates a list of the total cost of each item based on the amount needed"""
        for i in range(len(self.costs)):                                                    #iterates through the list of costs
            self.totalCost=self.costs[i]*self.quantity[i]                                   #item cost*quantity
            self.totalCostlist.append(self.totalCost)
        return self.totalCostlist
            
             
    def Total(self):
        """This calculates the total cost of all the items that have been added to the list"""
        
        self.total=0               
        for p in range(0,len(self.totalCostlist)):                                         #total of costs in the cost list
            self.total=self.total+self.totalCostlist[p]
        return self.total
                
    def itemChecker(self):
        """This function iterates through the lists of costs and
        determines if the budget is exceeded.If this occurs it returns
        True and pops the exceeding item from the list,if not it returns False."""

        
        self.shoppinglist=[(self.items[i],self.totalCostlist[i]) for i in range(0, len(self.items))]        #list of tuples
        if self.total > self.starting_budget:
            print('\nAn item you added exceeds your budget!')
            total=0
          
            for ele in self.totalCostlist:
                total=total+ele
                if total>self.starting_budget:
                    if self.totalCostlist.count(ele)==1:                                                    #no duplicates of the cost value
                        self.ind=self.totalCostlist.index(ele)
                        break
                    else:
                        found=0
                        count=0
                        
                        while found!=self.totalCostlist.count(ele):                                   
                            for y in self.totalCostlist:
                                count=count+1
                                if y==ele:
                                    found=found+1
                    
                        self.ind=count-1
            if self.totalCostlist[self.ind] == self.totalCostlist[-1]:                                    #if the only item in the list exceeds the budget 
                b=self.items.pop(self.ind)                                                                #removes just that element
                self.total=self.total-self.totalCostlist[self.ind]
                self.t=self.totalCostlist.pop(self.ind)
            else:
                b=self.items.pop(self.ind)
                del self.items[self.ind:]                                                                 #removes the element and all the others after it.
                self.total=self.total-self.totalCostlist[self.ind]
                self.t=self.totalCostlist.pop(self.ind)
                del self.totalCostlist[self.ind:]
                

            return True
        
        else:
            
            return False
    def suggestions(self):
        """This function suggests the first item in the list that
        exceeds the budget and guides the user through an interactive
        session that ensures that the user does not go above the
        budget again.It returns False if the user still can't seem to
        strike a balance and this re-calls the getItems() function"""

        self.reply=input('Would you like to know our own suggestion to fit your item ?(yes/no) ')
        if self.reply.lower()=='yes':
           
                value=self.t
                s=self.shoppinglist[self.ind]
                if s[1]==value:                                                                                           
                        suggest=s[0]                                                                                                        #the first value that exceeds the total
                        print('We would suggest you reduce the amount of','<<'+suggest+'>>','or remove it completely from your list.')
                        print('If you added any other items after','<<'+suggest+'>>',', they must be completely removed.')
                        goAhead=input('If you want to go ahead with that enter yes, if not enter no.')
                        if goAhead=='yes':
                            print('\n\n')
                            self.getItems()                                                                                                 #user re-enters values
                            self.CostList()
                            self.Total()
                            if self.itemChecker()==False:
                                return True
                                
                        
                        else:
                            print('Enter no for the next question')
                            self.suggestions()
                 
        elif self.reply.lower()=='no':
            
            while True:   
                suggestInstead=input("If you don't like that idea ,which other item would you like to edit/remove that will ensure that your budget is not surpassed? ")
                if suggestInstead not in [element[0] for element in self.shoppinglist]:
                    print('Your suggestion is not valid.Enter your suggestion again')
                else:
                    break
            for i in self.shoppinglist:
                if i[0]==suggestInstead:
                    reply2=input('Do you want to change the amount or remove completely?(remove/change) ')
                    if reply2=='remove':
                        self.shoppinglist.remove(i)
                    elif reply2=='change':
                        current=int(input('Enter current amount: '))
                        new=int(input('Enter the new amount(i.e the amount youre changing it to): '))
                        j=list(i)                                                                                                       #converts tuple to list
                        j[1]=(i[1]/current)*new                                                                                         #mutates value
                        k=tuple(j)                                                                                                      #converts back to tuple
                        indx=self.shoppinglist.index(i)
                        self.shoppinglist.pop(indx)
                        self.shoppinglist.insert(indx,k)
                        self.items.append(suggestInstead)
                        self.totalCostlist.append(j[1])
                        
                        
                        
            more=input('If you still have an error,enter "yes" so we can auto-correct the list for you:),else enter "no":')
            if more =='yes':
              return False                                                                                                                 #automatically fixes the problem
              self.getItems()
              
            else:
                return self.itemChecker()
        
    def getPercentage(self):
        """This function creates a list of the percentages of each item
        that made it to the final budgetting table
        This percentage is based on how much of the income is eventually utilized"""
        
        self.totalsum=0
        for i in self.shoppinglist:                           #a new total of all the items that made the final list
                self.totalsum=self.totalsum+i[1]
        self.percentages=[]
        for l in self.shoppinglist:
                percent=(l[1]/self.totalsum)*100
                self.percentages.append(round(percent,2))   #percentage must be 2dp
        return self.percentages
    
    def displayTable(self):
        """This function creates a budget table based on the list of the percentages
        and the final items list that doesn't surpass the budget.
        
            It does this by utilizing loops and f-literals.It also displays the amount
            of expendable income the user has left."""


        print('\n             '+self.Budget_Name)
        print('No. Item   price  amount  total  Percentage')
        print('===========================================')
        for k in range(len(self.totalCostlist)):                                                    #iterates using the number of items that made the final shopping list
                s=self.shoppinglist[k]
                itemName=s[0]
                itemTotal=s[1]
                price=self.costs[k]
                amount=itemTotal/price
                percents=self.percentages[k]
                
                msg=f'{k+1}   {itemName:7}${price:4}  {amount:>3}     ${itemTotal:>4}  {percents}%'    #f-literal that forms table
                print(msg)
        print('Expendable income left= $'+str(self.starting_budget-self.totalsum))
            
            
            




