class BlogPostValidator:
    def validate_content(self, content: str) -> bool:
        # Simple content validation (e.g., no prohibited words, length check)
        prohibited_words = ["spam", "advertisement"]
        if any(word in content.lower() for word in prohibited_words):
            return False
        return len(content) > 0

class BlogPostRepository:
    def save_to_database(self):
    # Simulate saving the post to the database
        print(f"Saving post '{self.title}' by {self.author} to the database.")

class BlogPostNotifier:
    def notify_subscribers(self):
        # Simulate sending notifications to subscribers
        print(f"Sending notification to subscribers about new post '{self.title}'.")

class BlogPostLogger:
    def log_operation(self, message: str):
        # Simulate logging the operation
        print(f"LOG: {message}")

class BlogPostManager:
    def __init__(self, title: str, content: str, author: str,
                 validator: BlogPostValidator,
                 repository: BlogPostRepository,
                 notifier: BlogPostNotifier,
                 logger: BlogPostLogger):
        self.title = title
        self.content = content
        self.author = author
        self.validator = validator
        self.repository = repository
        self.notifier = notifier    
        self.logger = logger

    def create_post(self):
        if not self.validator.validate_content(self.content):
            raise ValueError("Invalid content")

        self.repository.save_to_database()
        self.logger.log_operation("Post created")
        self.notifier.notify_subscribers()

