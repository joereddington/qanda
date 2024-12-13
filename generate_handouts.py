import os
from QuestionDatabase import QuestionDatabase

def create_latex_file(qd, num_iterations, output_file, snippets_dir="snippets"):
    """
    Create a LaTeX file with the sequence: header, intro (n times), 11 random questions, outro, and footer.
    
    Parameters:
    - qd (QuestionDatabase): An instance of the QuestionDatabase class.
    - num_iterations (int): Number of times to insert intro.
    - output_file (str): Output file name for the generated LaTeX.
    - snippets_dir (str): Directory where the LaTeX snippet files are located.
    """
    with open(output_file, "w") as latex_file:
        # Include header snippet
        with open(os.path.join(snippets_dir, "header.tex"), "r") as header_file:
            latex_file.write(header_file.read() + "\n")
            latex_file.write("%Header written\n")
             
        # Include 'num_iterations' of intro snippet
        for _ in range(num_iterations):
            with open(os.path.join(snippets_dir, "intro.tex"), "r") as intro_file:
                latex_file.write(intro_file.read() + "\n")
                latex_file.write("%Intro written\n")
            # Get 11 random questions from the Question Database
            random_questions = qd.get_random_questions(11,['Bonus','Incident Management','Legal and Ethical Aspects','Staff Management'])
            question_list = [q["Question"] for q in random_questions]
            latex_itemized_questions = qd.create_latex_itemize(question_list)
            
            # Write the random questions in LaTeX format
            latex_file.write(latex_itemized_questions + "\n")
            latex_file.write("%Questions written\n")
        
            # Include outro snippet
            with open(os.path.join(snippets_dir, "outtro.tex"), "r") as outro_file:
                latex_file.write(outro_file.read() + "\n")
                latex_file.write("%outro written\n")
        
        # Include footer snippet
        with open(os.path.join(snippets_dir, "footer.tex"), "r") as footer_file:
            latex_file.write(footer_file.read() + "\n")
    
    print(f"LaTeX file '{output_file}' has been created successfully.")

if __name__ == "__main__":
    # Initialize the QuestionDatabase with the renamed CSV file
    qd = QuestionDatabase("question_database.csv")

    # Number of intro iterations
    num_iterations = 30

    # Output LaTeX file
    output_file = "generated_latex_document.tex"

    # Call the function to create the LaTeX file
    create_latex_file(qd, num_iterations, output_file)

