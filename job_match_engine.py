from nlp_utils import preprocess_text, calculate_text_similarity

class JobMatchEngine:
    def __init__(self, job_database, candidate_database):
        self.job_database = job_database
        self.candidate_database = candidate_database

    def match_jobs(self, candidate_name):
        candidate = self.candidate_database.find_candidate_by_name(candidate_name)
        if not candidate:
            print(f"Candidate '{candidate_name}' not found in the database.")
            return []

        candidate_skills = set(candidate.skills)
        job_matches = []
        for job in self.job_database.get_jobs():
            job_skills = set(job.skills)
            similarity_score = len(candidate_skills.intersection(job_skills)) / len(candidate_skills.union(job_skills))
            job_matches.append((job, similarity_score))
        return sorted(job_matches, key=lambda x: x[1], reverse=True)

    def recommend_jobs(self, candidate_name, num_recommendations=5):
        matched_jobs = self.match_jobs(candidate_name)
        recommended_jobs = [job[0].title for job in matched_jobs[:num_recommendations]]
        return recommended_jobs

    def refine_candidate_profile(self, candidate):
        for job, score in candidate.feedback:
            if score >= 4:  # Threshold 
                candidate.skills.extend([skill for skill in job.skills if skill not in candidate.skills])
                candidate.skills = list(set(candidate.skills))  


