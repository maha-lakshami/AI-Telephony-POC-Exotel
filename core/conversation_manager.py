class ConversationManager:

    QUESTIONS = [
        ("name", "May I know your full name?"),
        ("email", "What is your email address?"),
        ("phone", "Can you share your phone number?"),
        ("experience", "How many years of experience do you have?"),
        ("skills", "What are your primary technical skills?"),
        ("location", "Where are you currently located?"),
        ("expected_salary", "What is your expected salary?"),
        ("notice_period", "What is your notice period?"),
    ]

    def __init__(self):
        self.current_index = {}

    def start(self, stream_id):
        self.current_index[stream_id] = 0
        return (
            "Hello! Welcome to JobForm Automator. "
            "I'm your AI Recruiter. Let's begin your interview."
        )

    def next_question(self, stream_id):
        index = self.current_index.get(stream_id, 0)

        if index >= len(self.QUESTIONS):
            return None

        self.current_index[stream_id] += 1

        return self.QUESTIONS[index]

    def is_completed(self, stream_id):
        return self.current_index.get(stream_id, 0) >= len(self.QUESTIONS)

    def save_answer(self, session, field, value):
        """
        Save the candidate's answer into the current session.
        """
        session.save_candidate(field, value)

    def reset(self, stream_id):
        """
        Reset the interview state for a completed or cancelled call.
        """
        if stream_id in self.current_index:
            del self.current_index[stream_id]