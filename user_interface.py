from job_database import JobDatabase
from candidate_database import CandidateDatabase
from job_match_engine import JobMatchEngine
class UserInterface:
    def __init__(self):
        self.job_database = JobDatabase()
        self.candidate_database = CandidateDatabase()
        self.job_match_engine = JobMatchEngine(self.job_database, self.candidate_database)

    def add_job(self, title, description, skills):
        self.job_database.add_job(title, description, skills)

    def add_candidate(self, name, skills):
        self.candidate_database.add_candidate(name, skills)

    def collect_feedback(self, candidate_name, job_title, score):
        candidate = self.candidate_database.find_candidate_by_name(candidate_name)
        job = self.job_database.find_job_by_title(job_title)
        if candidate and job:
            candidate.add_feedback(job, score)

    def refine_recommendations(self):
        for candidate in self.candidate_database.get_candidates():
            self.job_match_engine.refine_candidate_profile(candidate)

    def match_candidates_to_jobs(self):
        for candidate in self.candidate_database.get_candidates():
            job_matches = self.job_match_engine.match_jobs(candidate.name)
            setattr(candidate, 'job_matches', job_matches)

    def display_results(self):
        for candidate in self.candidate_database.get_candidates():
            print(f"Job matches for candidate {candidate.name}:")
            for job, similarity_score in candidate.job_matches:
                print(f" - {job.title} (Similarity Score: {similarity_score:.2f})")
            print()

