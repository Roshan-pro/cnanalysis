import pandas as pd
from cnanalysis import CombineAnalysis

def test_combine_analysis_plot_and_stats():
    # Sample data
    df = pd.DataFrame({
        'category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B'],
        'value': [10, 20, 15, 30, 25, 12, 28, 35, 18]
    })

    # Instantiate the class
    comb = CombineAnalysis(
        data=df,
        number_col='value',
        categorical_col='category',
        group_stats='mean',
        figure_size=(8, 4),
        rotation=45,
        palette='Set2'
    )

    # Call the plotting function (also returns grouped DataFrame)
    grouped_df = comb.PlotGroupedData()

    # Print for manual inspection (optional)
    print(grouped_df)

test_combine_analysis_plot_and_stats()