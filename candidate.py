class Candidate:
    def __init__(self, name, skills):
        self.name = name
        if isinstance(skills, str):
            self.skills = [skill.strip().lower() for skill in skills.split(',')]
        else:
            self.skills = [skill.strip().lower() for skill in skills]
        self.applications = []
        self.feedback = []  # List to store feedback as (job, score) tuples

    def apply_for_job(self, job):
        if job not in self.applications:
            self.applications.append(job)
            job.add_applicant(self)
        else:
            print(f"{self.name} has already applied for {job.title}")

    def withdraw_application(self, job):
        if job in self.applications:
            self.applications.remove(job)
            job.remove_applicant(self)
        else:
            print(f"{self.name} has not applied for {job.title}")

    def get_applications(self):
        return self.applications

    def add_feedback(self, job, score):
        self.feedback.append((job, score))
