import pandas as pd
from cnanalysis import CardinalityAndRareCategoryAnalyzer

def test_cardinality_and_rare_category_analyzer():
    # Sample DataFrame
    df = pd.DataFrame({
        'color': ['red', 'blue', 'red', 'green', 'blue', 'red', 'yellow', 'blue', 'yellow', 'purple'],
        'shape': ['circle', 'square', 'circle', 'triangle', 'square', 'circle', 'square', 'circle', 'circle', 'hex']
    })

    # Instantiate the analyzer
    analyzer = CardinalityAndRareCategoryAnalyzer(data=df, thresh=0.2)

    # Run the analysis
    result = analyzer.get_cardinality_n_rare_cat()

    # Print result (for manual testing)
    print(result)

test_cardinality_and_rare_category_analyzer()