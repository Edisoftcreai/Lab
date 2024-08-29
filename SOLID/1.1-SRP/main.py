class BlogPostManager:
    def __init__(self, title: str, content: str, author: str):
        self.title = title
        self.content = content
        self.author = author

    def create_post(self):
        if not self.validate_content(self.content):
            raise ValueError("Invalid content")

        self.save_to_database()
        self.log_operation("Post created")
        self.notify_subscribers()

    def validate_content(self, content: str) -> bool:
        # Simple content validation (e.g., no prohibited words, length check)
        prohibited_words = ["spam", "advertisement"]
        if any(word in content.lower() for word in prohibited_words):
            return False
        return len(content) > 0

    def save_to_database(self):
        # Simulate saving the post to the database
        print(f"Saving post '{self.title}' by {self.author} to the database.")

    def log_operation(self, message: str):
        # Simulate logging the operation
        print(f"LOG: {message}")

    def notify_subscribers(self):
        # Simulate sending notifications to subscribers
        print(f"Sending notification to subscribers about new post '{self.title}'.")

