import pandas as pd
from cnanalysis import ChiSquareTest

def test_chisquare_test():
    # Sample DataFrame with categorical columns
    df = pd.DataFrame({
        'gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
        'purchased': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No']
    })

    # Instantiate the class
    chi_test = ChiSquareTest(data=df, col1='gender', col2='purchased')

    # Run the test
    result = chi_test.test()

    # Print result (optional for manual check)
    print(result)

test_chisquare_test()
