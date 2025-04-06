#############################
# Source: 
# https://medium.com/@patwariraghottam/mastering-chi-square-goodness-of-fit-tests-with-python-implementation-and-visualization-58d619b5e02c
#############################


#Import the required libraries
from scipy import stats as st

class ChiSquareGoodnessOfFit:
    
    #Initialize the ChiSquareGoodnessOfFit class with observed and expected frequencies
    def __init__(self, observed, expected):
        self.observed = observed
        self.expected = expected
        
    #Calculate the Chi-Square statistic for the given observed and expected frequencies.    
    def calculate_chi_square(self):
        # Calculate total observations
        total_observed = sum(self.observed)
        
        # Calculate total expected (assuming uniform distribution)
        total_expected = sum(self.expected)
        
        # Calculate degrees of freedom
        self.degrees_of_freedom = len(self.observed) - 1
        
        # Initialize Chi-Square statistic
        chi_square_statistic = 0.0
        
        # Calculate Chi-Square statistic
        for i in range(len(self.observed)):
            O_i = self.observed[i]
            E_i = self.expected[i]
            
            chi_square_statistic += ((O_i - E_i)**2) / E_i
        
        return chi_square_statistic
    
    #Perform Chi-Square goodness of fit test and print results. 
    def testing(self,alpha):
        self.alpha=0.05
        critical_value = st.chi2.ppf(1 - alpha,len(self.observed)-1)
        print("Chi-square_Critical : {}".format(critical_value))
        print("*"*70)
        # if self.calculate_chi_square()>critical_value:
        #     print("Reject the null hypothesis i.e, we can say that observed and expected frequencies are different")
        # else:
        #     print("fail to reject the null hypothesis i.e, observed and expected frequencies are same")
