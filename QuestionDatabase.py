import pandas as pd
import random

class QuestionDatabase:
    def __init__(self, csv_file):
        """Initialize the class with the CSV data."""
        self.df = pd.read_csv(csv_file)
    
    def get_random_questions(self, n, category=None):
        """
        Returns a randomized list of n questions. Optionally filters by category.
        
        Parameters:
        - n (int): Number of questions to return.
        - category (str): Filter by category (Introduction, Standards, Risk).
        
        Returns:
        - list: List of randomized questions.
        """
        if category:
            filtered_df = self.df[self.df["Category"] == category]
        else:
            filtered_df = self.df
        
        return filtered_df.sample(n=min(n, len(filtered_df))).to_dict('records')
    
    def create_latex_itemize(self, questions):
        """
        Creates a LaTeX itemized list for Google Docs based on the provided list of questions.
        
        Parameters:
        - questions (list): List of questions to include in the itemized list.
        
        Returns:
        - str: LaTeX formatted string in Google Docs compatible format.
        """
        latex_str = "\\begin{itemize}\n"
        for question in questions:
            latex_str += f"  \\item {question}\n"
        latex_str += "\\end{itemize}\n"
        
        return latex_str

if __name__ == "__main__":
    # Initialize the class with the renamed CSV file
    qd = QuestionDatabase("question_database.csv")

    # Get 6 random questions from the 'Risk' category
    random_risk_questions = qd.get_random_questions(6, category="Risk")
    risk_list = [q["Question"] for q in random_risk_questions]

    # Get 4 random questions from the 'Standards' category
    random_standards_questions = qd.get_random_questions(4, category="Standards")
    standards_list = [q["Question"] for q in random_standards_questions]

    # Get 1 random question from the 'Introduction' category
    random_introduction_question = qd.get_random_questions(1, category="Introduction")
    introduction_list = [q["Question"] for q in random_introduction_question]

    # Combine the questions into one list
    combined_questions = risk_list + standards_list + introduction_list

    # Generate the LaTeX itemized list for the selected questions
    latex_output = qd.create_latex_itemize(combined_questions)
    
    # Output the selected questions and LaTeX formatted string
    print("Random Questions from Risk, Standards, and Introduction Categories:")
    for question in combined_questions:
        print(question)

    print("\nLaTeX Itemized List (Google Docs Format):")
    print(latex_output)

