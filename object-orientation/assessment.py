"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction- You don't need to know the information that a method uses. For
                example, you can use min() without knowing exactly how it figures 
                out the mininum value.

   Encapsulation- The data lives close to its functionality. It is contained. It allows
                for a class to change its implementation without having to change the
                rest of your code.

   Polymorphism- Flexibility of types without having to use conditionals. It allows
                us to use different things that are interchangable. For example, 
                there a many different types of buttons (round button, square button,
                colored buttons). You can use the same method on all of them becuase
                they all share the same core concept. 



2. What is a class?
    A prototype that has attributes that characterizes any object of that class. 

3. What is an instance attribute?
    An instance attribute is an attribute that could be different between all
    of the instances. For example, one dog's name could be Eli and another dogs
    name could be Poppy and they are still both dogs. 

4. What is a method?
    A method is a special kind function that is defined in a class. You can
    call methods on an instance.

5. What is an instance in object orientation?
    An instance is when a object of the class is created(instantiated).

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Class attributes are a value that every single instance will share when it is instantiated.
   For example, if every order has a tax rate of 10 percent then it would go under
   the class attribute and when the orders are created they would all have tax rate
   set to 10 percent.

   Instance attributes are a value that is determined during instantiation. Not all
   instances need to share the same value for the attribute. For example, for one order
   (instance) the shipping destination attribute might be France while another order 
   (instance) the shipping destination attribute might be Costa Rica.



"""


# Parts 2 through 5:
# Create your classes and class methods


"""
Part 2: Classes and Init methods

"""

class Student(object):
    """ Student with first name, last name, and address as attributes"""

    def __init__(self, first_name, last_name, address):
        """Initialize student with instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """ Question and answer"""

    def __init__(self, question, correct_answer):
        """Initialize question with corrext answer"""

        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        """Returns a string of the questions rather
         than the <obejct at xxxxxx> message"""

        return "<Questions %s" % self.question

    def ask_and_evaluate(self):
        """Asks questions, accepts input, and checks if the answer is correct"""

        print self.question
        answer_input = raw_input("What is your answer? ").lower()
        if answer_input == self.correct_answer:
            return True
        else:
            return False



class Exam(object):
    """ Exam that can have a list of question objects as an attribute"""

    def __init__(self, name):
        """Initalize exam with instance attributes"""

        self.name = name
        self.questions = []

    def add_questions(self, question, correct_answer):
        """Add question object and then add that object to the questions attribute"""

        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer(self):
        """Administers test"""

        score = 0
        count = 0
        for question in self.questions:
            if question.ask_and_evaluate() == True:
                score += 1
                count += 1
            else:
                count += 1
        # Catches a score of zero because it throws error if you try to 
        # divide with a zero
        if score == 0:
            return 0
        else:
            total_score =  float(score) / float(count)
            return total_score


class Quiz(Exam):
    """ Quiz object that inherits from Exam"""

    def administer(self):
        """Calls super administer method. Then return true or false 
        depending on percentage correct"""

        total_score = super(Quiz, self).administer()
        if total_score > .50:
            return True
        else:
            return False

"""
Part 4: Creat an actual Exam
"""

def example(assessment_name, first_name, last_name, address):
    """Creates an exam, adds questions, creates student,
        and calls take_test method."""

    assessment = Exam(assessment_name)
    assessment.add_questions("Is this fun? ", "yes")
    assessment.add_questions("Is Hackbright awesome? ", "yes")
    assessment.add_questions("Is Eli the best dog ever? ", "yes")
    student = Student(first_name, last_name, address)
    take_test(assessment, student)


def take_test(Exam, Student):
    """Calls administer to give exam, prints score, add score to 
    student attribute"""

    assessment = Exam
    student = Student
    total_score = assessment.administer()
    student.score = total_score
    print "Your score is {0:.0%}".format(total_score)
    return total_score


def quiz_example(assessment_name, first_name, last_name, address):

    assessment = Quiz(assessment_name)
    assessment.add_questions("Is this fun? ", "yes")
    assessment.add_questions("Is Hackbright awesome? ", "yes")
    assessment.add_questions("Is Eli the best dog ever? ", "yes")
    student = Student(first_name, last_name, address)
    take_test(assessment, student)


quiz_example("Assessment", "Amelia", "Green", "14 Wanderlust Ave")

