import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """Load the customer purchasing behavior dataset."""
    return pd.read_csv('data/customer_data.csv')

def explore_dataframe(df):
    """Demonstrate basic DataFrame operations."""
    print("First 5 rows:")
    print(df.head())
    
    print("\nDataFrame Info:")
    print(df.info())
    
    print("\nSummary Statistics:")
    print(df.describe())

def data_selection(df):
    """Demonstrate data selection and indexing."""
    print("Selecting 'age' and 'annual_income' columns:")
    print(df[['age', 'annual_income']].head())
    
    print("\nFiltering customers with loyalty_score > 75:")
    print(df[df['loyalty_score'] > 75].head())
    
    print("\nUsing loc to select specific rows and columns:")
    print(df.loc[0:4, ['user_id', 'age', 'purchase_amount']])

def data_operations(df):
    """Demonstrate basic data operations."""
    df['average_purchase'] = df['purchase_amount'] / df['purchase_frequency']
    print("Added 'average_purchase' column:")
    print(df.head())
    
    print("\nSorting by purchase_amount (descending):")
    print(df.sort_values('purchase_amount', ascending=False).head())

def grouping_and_aggregation(df):
    """Demonstrate grouping and aggregation."""
    age_groups = pd.cut(df['age'], bins=[0, 30, 50, 70, 100], labels=['0-30', '31-50', '51-70', '71+'])
    grouped = df.groupby(age_groups)
    
    print("Average purchase amount by age group:")
    print(grouped['purchase_amount'].mean())
    
    print("\nHighest loyalty score by age group:")
    print(grouped['loyalty_score'].max())

def basic_visualization(df):
    """Demonstrate basic visualization with Pandas."""
    plt.figure(figsize=(10, 6))
    df.plot(kind='scatter', x='annual_income', y='purchase_amount', alpha=0.5)
    plt.title('Annual Income vs Purchase Amount')
    plt.xlabel('Annual Income')
    plt.ylabel('Purchase Amount')
    plt.tight_layout()
    plt.savefig('income_vs_purchase.png')
    plt.close()
    print("Scatter plot saved as 'income_vs_purchase.png'")

def main():
    print("Welcome to Pandas Tutorial: Customer Purchasing Behavior Analysis!")
    
    df = load_data()
    
    print("\n1. Exploring DataFrame")
    explore_dataframe(df)
    
    print("\n2. Data Selection and Indexing")
    data_selection(df)
    
    print("\n3. Basic Data Operations")
    data_operations(df)
    
    print("\n4. Grouping and Aggregation")
    grouping_and_aggregation(df)
    
    print("\n5. Basic Data Visualization")
    basic_visualization(df)
    
    print("\nTutorial completed! You've learned Pandas basics with real customer data.")

if __name__ == "__main__":
    main()