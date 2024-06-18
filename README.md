# Job-Recommendation-System
The project utilizes content-based filtering to recommend jobs based on candidate skills and job requirements. It employs NLP for text preprocessing and Jaccard similarity for matching. With structured data management, the engine refines recommendations using user feedback to enhance candidate profiles and improve job matches. This is a Python-based job matching system using NLP techniques and cosine similarity algorithms for skill and job alignment.
# Overview
The Job Recommendation System consists of multiple components:

- 'main.py': Entry point of the program.
- 'job.py': Defines the Job class.
- 'candidate.py': Defines the Candidate class.
- 'nlp_utils.py': Contains NLP utilities for processing text data.
- 'cosine_similarity.py': Implements cosine similarity calculation.
- 'job_database.py': Manages the database of available jobs.
- 'candidate_database.py': Manages the database of candidates.
- 'job_match_engine.py': Implements the core logic of the job matching engine.
- 'user_interface.py': Provides the user interface for interacting with the system.
- 'requirements.txt': Contains the required dependencies for the project.
#Usage
1. First, ensure you have all dependencies installed by running:
    pip install -r requirements.txt

2.  Then, open the visual studio copy the path of the file and run the main script or in the terminal copy the path of the file by changing the directory using command --
     In visual studio:-
         * copy path/main.py
    In command prompt:-
         * cd path of file
         * conda activate(optional)
     * python main.py
    
