from InstructorEmbedding import INSTRUCTOR

try:
    model = INSTRUCTOR("hkunlp/instructor-xl")
    print("Instructor model loaded successfully!")
except Exception as e:
    print("Error loading the Instructor model:", e)
