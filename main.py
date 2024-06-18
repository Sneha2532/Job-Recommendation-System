from user_interface import UserInterface

if __name__ == "__main__":
    ui = UserInterface()
    
    # Example usage: adding jobs and candidates to the database
    ui.add_job("Software Developer", "Develop software applications using Python and Java", "C, Java, Software Development")
    ui.add_job("Data Scientist", "Analyzing data using machine learning algorithms", "Machine Learning, Data Analysis, Python")
    ui.add_candidate("Alice", "C, Data Analysis, SQL")
    ui.add_candidate("Bob", "Data Analysis, Software Development, Machine Learning,Python")
    
    # Collect feedback from candidates
    ui.collect_feedback("Alice", "Software Developer", 5)
    ui.collect_feedback("Alice", "Data Scientist", 1)

    ui.collect_feedback("Bob", "Software Developer", 2)
    ui.collect_feedback("Bob", "Data Scientist", 4)
    
    # Refining recommendations based on feedback
    ui.refine_recommendations()
    
    # Matching candidates to jobs
    ui.match_candidates_to_jobs()
    
    # Displaying the results
    ui.display_results()

