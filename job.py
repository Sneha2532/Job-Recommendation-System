class Job:
    def __init__(self, title, description, skills):
        self.title = title
        self.description = description
        if isinstance(skills, str):
            self.skills = [skill.strip().lower() for skill in skills.split(',')]
        else:
            self.skills = [skill.strip().lower() for skill in skills]
        self.applicants = []

    def add_applicant(self, candidate):
        self.applicants.append(candidate)

    def remove_applicant(self, candidate):
        if candidate in self.applicants:
            self.applicants.remove(candidate)
        else:
            print(f"{candidate.name} is not an applicant for {self.title}")

    def get_applicants(self):
        return self.applicants

