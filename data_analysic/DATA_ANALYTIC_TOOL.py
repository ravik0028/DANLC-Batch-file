import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Step 1: Import File
def list_files(folder):
    """List all CSV and Excel files in the specified folder."""
    try:
        files = [f for f in os.listdir(folder) if f.endswith('.csv') or f.endswith('.xlsx')]
        return files
    except FileNotFoundError:
        print(f"Folder not found: {folder}")
        return []


def load_file(folder):
    """Load a file from the specified folder."""
    files = list_files(folder)
    if not files:
        print("No files found in the folder!")
        return None

    print("\nAvailable Files:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")

    try:
        choice = int(input("\nEnter the number of the file you want to select: "))
        selected_file = os.path.join(folder, files[choice - 1])
        if selected_file.endswith('.xlsx'):
            return pd.read_excel(selected_file), selected_file
        elif selected_file.endswith('.csv'):
            return pd.read_csv(selected_file), selected_file
    except (IndexError, ValueError):
        print("Invalid selection. Please try again.")
    except Exception as e:
        print(f"Error loading file: {e}")
    return None, None


# Step 2: Cleaning Options
def show_data(df):
    """Display the full dataset."""
    print("\nFull Data Set:")
    print(df)


def save_file(df, original_file):
    """Save changes to the original file or create a new file."""
    try:
        choice = input("\nDo you want to save changes to the original file? (y/n): ")
        if choice.lower() == 'y':
            if original_file.endswith('.csv'):
                df.to_csv(original_file, index=False)
                print(f"Changes saved to {original_file}")
            elif original_file.endswith('.xlsx'):
                df.to_excel(original_file, index=False)
                print(f"Changes saved to {original_file}")
        else:
            new_file = input("Enter the name of the new file (including extension, e.g., 'new_file.csv'): ")
            new_file_path = os.path.join(os.path.dirname(original_file), new_file)
            if new_file.endswith('.csv'):
                df.to_csv(new_file_path, index=False)
                print(f"Changes saved to {new_file_path}")
            elif new_file.endswith('.xlsx'):
                df.to_excel(new_file_path, index=False)
                print(f"Changes saved to {new_file_path}")
    except PermissionError:
        print(f"Error saving file. You do not have permission to write to {original_file}.")
        new_location = input(
            "Enter a new location and file name to save the file (e.g., C:\\Users\\Mayank\\Documents\\new_file.csv): ")
        if new_location.endswith('.csv'):
            df.to_csv(new_location, index=False)
            print(f"Changes saved to {new_location}")
        elif new_location.endswith('.xlsx'):
            df.to_excel(new_location, index=False)
            print(f"Changes saved to {new_location}")
    except Exception as e:
        print(f"An error occurred while saving: {e}")


def clean_data(df, original_file):
    """Perform data cleaning operations."""
    print("\nCleaning Options:")
    print("1. Remove Duplicates")
    print("2. Handle Missing Values (Fill with Mean)")
    print("3. Drop Missing Values")
    print("4. Standardize Column Names")
    print("5. Remove Outliers")
    print("6. Skip Cleaning")

    try:
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            df = df.drop_duplicates()
            print("\nData After Removing Duplicates:")
            show_data(df)
        elif choice == 2:
            df = df.fillna(df.mean(numeric_only=True))
            print("\nData After Filling Missing Values:")
            show_data(df)
        elif choice == 3:
            df = df.dropna()
            print("\nData After Dropping Missing Values:")
            show_data(df)
        elif choice == 4:
            df.columns = df.columns.str.strip().str.lower().str.replace(' ', '').str.replace(r'[^a-zA-Z0-9]', '',
                                                                                             regex=True)
            print("\nStandardized Column Names:")
            show_data(df)
        elif choice == 5:
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            for col in numeric_cols:
                q1 = df[col].quantile(0.25)
                q3 = df[col].quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
            print("\nData After Removing Outliers:")
            show_data(df)
        else:
            print("No cleaning performed.")
    except ValueError:
        print("Invalid choice. No cleaning performed.")

    save_file(df, original_file)  # Option to save after cleaning
    return df


# Step 3: Analyzing and Transforming
def analyze_transform(df, original_file):
    """Perform data analysis and transformation."""
    print("\nAnalyzing and Transforming Options:")
    print("1. Merge with Another File")
    print("2. Split Column into Multiple Columns")
    print("3. Sort Data by a Column")
    print("4. Filter Rows by a Condition")
    print("5. Group Data and Calculate Aggregates")
    print("6. Create a Pivot Table")
    print("7. Skip Analysis/Transformation")

    try:
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            folder = "C:\\Users\\Mayank\\Downloads"  # Folder for additional files
            other_df, _ = load_file(folder)
            if other_df is not None:
                df = pd.concat([df, other_df], axis=0, ignore_index=True)
                print("\nFiles Merged Successfully:")
                show_data(df)
        elif choice == 2:
            column = input("Enter the column name to split: ")
            separator = input("Enter the separator (e.g., ','): ")
            if column in df.columns:
                new_columns = df[column].str.split(separator, expand=True)
                new_column_names = [f"{column}_part{i + 1}" for i in range(new_columns.shape[1])]
                new_columns.columns = new_column_names
                df = pd.concat([df, new_columns], axis=1)
                print("\nData After Splitting the Column:")
                show_data(df)
        elif choice == 3:
            column = input("Enter the column name to sort by: ")
            if column in df.columns:
                df = df.sort_values(by=column)
                print("\nData After Sorting:")
                show_data(df)
        elif choice == 4:
            column = input("Enter the column name for filtering: ")
            condition = input("Enter the condition (e.g., '> 50'): ")
            if column in df.columns:
                try:
                    df = df.query(f"{column} {condition}")
                    print("\nData After Filtering:")
                    show_data(df)
                except Exception as e:
                    print(f"Error in filtering: {e}")
        elif choice == 5:
            column = input("Enter the column name to group by: ")
            if column in df.columns:
                agg_func = input("Enter the aggregation function (e.g., sum, mean): ")
                try:
                    grouped = df.groupby(column).agg(agg_func)
                    print("\nGrouped Data:")
                    show_data(grouped)
                except Exception as e:
                    print(f"Error in grouping: {e}")
        elif choice == 6:
            print("\nCreating Pivot Table:")
            print("Available columns:", df.columns.tolist())
            rows = input("Enter the column name for rows: ")
            columns = input("Enter the column name for columns: ")
            values = input("Enter the column name for values: ")
            agg_func = input("Enter the aggregation function (e.g., 'sum', 'mean'): ")

            if all(col in df.columns for col in [rows, columns, values]):
                try:
                    pivot = pd.pivot_table(df, index=rows, columns=columns, values=values, aggfunc=agg_func)
                    print("\nPivot Table:")
                    show_data(pivot)
                except Exception as e:
                    print(f"Error creating pivot table: {e}")
        else:
            print("No transformation performed.")
    except ValueError:
        print("Invalid choice. No transformation performed.")

    save_file(df, original_file)  # Option to save after transformation
    return df


# Step 4: Data Visualization
def visualize_data(df):
    """Visualize the data using charts."""
    print("\nVisualization Options:")
    print("1. Bar Chart")
    print("2. Pie Chart")
    print("3. Line Chart")
    print("4. Scatter Plot")
    print("5. Histogram")
    print("6. Box Plot")
    print("7. Heatmap")
    print("8. Skip Visualization")

    try:
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            column = input("Enter the column name for the bar chart: ")
            if column in df.columns:
                df[column].value_counts().plot(kind='bar')
                plt.title("Bar Chart")
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.show()
            else:
                print(f"Column '{column}' not found.")
        elif choice == 2:
            column = input("Enter the column name for the pie chart: ")
            if column in df.columns:
                df[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
                plt.title("Pie Chart")
                plt.show()
            else:
                print(f"Column '{column}' not found.")
        elif choice == 3:
            column = input("Enter the column name for the line chart: ")
            if column in df.columns:
                df[column].plot(kind='line')
                plt.title("Line Chart")
                plt.xlabel("Index")
                plt.ylabel(column)
                plt.show()
            else:
                print(f"Column '{column}' not found.")
        elif choice == 4:
            x_column = input("Enter the column name for the x-axis: ")
            y_column = input("Enter the column name for the y-axis: ")
            if x_column in df.columns and y_column in df.columns:
                plt.scatter(df[x_column], df[y_column])
                plt.title("Scatter Plot")
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.show()
            else:
                print("One or both specified columns not found.")
        elif choice == 5:
            column = input("Enter the column name for the histogram: ")
            if column in df.columns:
                df[column].plot(kind='hist', bins=10)
                plt.title("Histogram")
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.show()
            else:
                print(f"Column '{column}' not found.")
        elif choice == 6:
            column = input("Enter the column name for the box plot: ")
            if column in df.columns:
                sns.boxplot(x=df[column])
                plt.title("Box Plot")
                plt.xlabel(column)
                plt.show()
            else:
                print(f"Column '{column}' not found.")
        elif choice == 7:
            print("Generating Heatmap for Numeric Data")
            numeric_data = df.select_dtypes(include=[np.number])
            if not numeric_data.empty:
                sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
                plt.title("Heatmap")
                plt.show()
            else:
                print("No numeric data available for heatmap.")
        else:
            print("Skipping visualization.")
    except ValueError:
        print("Invalid choice. Skipping visualization.")


# Main Program
def main():
    folder = "C:\\Users\\ravic\\Downloads"  # Folder containing the files
    df = None
    original_file = None

    while True:
        print("\nMain Menu:")
        print("1. Import File")
        print("2. Clean Data")
        print("3. Analyze and Transform")
        print("4. Visualize Data")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                df, original_file = load_file(folder)
                if df is not None:
                    print("\nFile Loaded Successfully:")
                    show_data(df)
            elif choice == 2 and df is not None:
                df = clean_data(df, original_file)
            elif choice == 3 and df is not None:
                df = analyze_transform(df, original_file)
            elif choice == 4 and df is not None:
                visualize_data(df)
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("No file loaded or invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Run the program
if __name__ == "__main__":
    main()