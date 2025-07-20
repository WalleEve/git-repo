import React, { useState } from 'react';
import { ChevronRight, CheckCircle, XCircle, RotateCcw, Trophy, Code, Clock } from 'lucide-react';

const PythonInterviewQuiz = () => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState('');
  const [showResult, setShowResult] = useState(false);
  const [score, setScore] = useState(0);
  const [quizComplete, setQuizComplete] = useState(false);
  const [answers, setAnswers] = useState([]);

  const questions = [
    {
      question: "What's the time complexity of this function?\n\ndef find_duplicates(arr):\n    duplicates = []\n    for i in range(len(arr)):\n        for j in range(i+1, len(arr)):\n            if arr[i] == arr[j]:\n                duplicates.append(arr[i])\n    return duplicates",
      options: ["O(n)", "O(n log n)", "O(n²)", "O(2^n)"],
      correct: 2,
      explanation: "This has nested loops - outer loop runs n times, inner loop runs up to n times for each iteration. This gives us O(n²) time complexity.",
      category: "Algorithms & Complexity"
    },
    {
      question: "What will this code output?\n\ndef modify_list(lst):\n    lst = lst + [4]\n    return lst\n\noriginal = [1, 2, 3]\nresult = modify_list(original)\nprint(original)\nprint(result)",
      options: [
        "[1, 2, 3]\n[1, 2, 3, 4]",
        "[1, 2, 3, 4]\n[1, 2, 3, 4]",
        "[1, 2, 3, 4]\n[1, 2, 3]",
        "Error"
      ],
      correct: 0,
      explanation: "lst = lst + [4] creates a NEW list object and assigns it to lst (local variable). The original list remains unchanged. This is different from lst.append(4) which would modify the original.",
      category: "Python Fundamentals"
    },
    {
      question: "Which approach is most efficient for checking if an item exists in a collection of 1 million items?",
      options: [
        "Using a list: item in my_list",
        "Using a set: item in my_set", 
        "Using a tuple: item in my_tuple",
        "Using a dictionary: item in my_dict.values()"
      ],
      correct: 1,
      explanation: "Sets use hash tables for O(1) average case lookup. Lists and tuples require O(n) linear search. Checking dict.values() is also O(n) since it searches through all values.",
      category: "Data Structures"
    },
    {
      question: "What's wrong with this code?\n\nclass BankAccount:\n    balance = 0\n    \n    def __init__(self, name):\n        self.name = name\n    \n    def deposit(self, amount):\n        self.balance += amount",
      options: [
        "Nothing is wrong",
        "balance should be an instance variable, not class variable",
        "Missing return statement in deposit method",
        "Constructor should call super()"
      ],
      correct: 1,
      explanation: "balance = 0 is a class variable shared by ALL instances. Each account would share the same balance! It should be self.balance = 0 in __init__ to make it an instance variable.",
      category: "Object-Oriented Programming"
    },
    {
      question: "What will this generator function produce?\n\ndef fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        yield a\n        a, b = b, a + b\n\nresult = list(fibonacci(5))",
      options: [
        "[0, 1, 1, 2, 3]",
        "[1, 1, 2, 3, 5]", 
        "[0, 1, 2, 3, 5]",
        "[1, 2, 3, 5, 8]"
      ],
      correct: 0,
      explanation: "The generator yields 'a' first (0), then updates a,b. Sequence: yield 0, then a=1,b=1; yield 1, then a=1,b=2; yield 1, then a=2,b=3; yield 2, then a=3,b=5; yield 3.",
      category: "Advanced Python"
    },
    {
      question: "How would you handle this potential error in a production system?\n\nuser_input = input('Enter a number: ')\nresult = 10 / int(user_input)",
      options: [
        "if user_input != '0': result = 10 / int(user_input)",
        "Use try/except to catch ValueError and ZeroDivisionError",
        "Use assert to check the input",
        "Convert to float first: result = 10 / float(user_input)"
      ],
      correct: 1,
      explanation: "Production code needs robust error handling. try/except catches both ValueError (invalid int conversion) and ZeroDivisionError (division by zero). Other options miss edge cases.",
      category: "Error Handling"
    },
    {
      question: "What's the most Pythonic way to swap two variables?",
      options: [
        "temp = a; a = b; b = temp",
        "a, b = b, a",
        "a = a + b; b = a - b; a = a - b", 
        "a = 0 if a else b; b = 0 if b else a"
      ],
      correct: 1,
      explanation: "Python's tuple unpacking (a, b = b, a) is the most readable and Pythonic way to swap variables. It's clear, concise, and works with any data types.",
      category: "Python Best Practices"
    },
    {
      question: "What will this code output?\n\nmy_dict = {'a': 1, 'b': 2}\nfor key in my_dict:\n    if key == 'a':\n        my_dict['c'] = 3\nprint(my_dict)",
      options: [
        "{'a': 1, 'b': 2, 'c': 3}",
        "{'a': 1, 'b': 2}",
        "RuntimeError: dictionary changed size during iteration",
        "KeyError: 'c'"
      ],
      correct: 0,
      explanation: "In Python 3.7+, modifying a dict during iteration is allowed and the new items won't be included in the current iteration. The dict will have the new key added.",
      category: "Python Fundamentals"
    }
  ];

  const handleAnswerSelect = (answerIndex) => {
    setSelectedAnswer(answerIndex);
  };

  const handleSubmit = () => {
    const isCorrect = selectedAnswer === questions[currentQuestion].correct;
    const newAnswers = [...answers, { 
      question: currentQuestion, 
      selected: selectedAnswer, 
      correct: isCorrect 
    }];
    setAnswers(newAnswers);
    
    if (isCorrect) {
      setScore(score + 1);
    }
    setShowResult(true);
  };

  const handleNext = () => {
    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
      setSelectedAnswer('');
      setShowResult(false);
    } else {
      setQuizComplete(true);
    }
  };

  const resetQuiz = () => {
    setCurrentQuestion(0);
    setSelectedAnswer('');
    setShowResult(false);
    setScore(0);
    setQuizComplete(false);
    setAnswers([]);
  };

  const getScoreColor = () => {
    const percentage = (score / questions.length) * 100;
    if (percentage >= 80) return 'text-green-600';
    if (percentage >= 60) return 'text-yellow-600';
    return 'text-red-600';
  };

  const getPerformanceMessage = () => {
    const percentage = (score / questions.length) * 100;
    if (percentage >= 90) return "Excellent! You're ready for senior-level Python interviews! 🚀";
    if (percentage >= 80) return "Great job! Strong Python knowledge for most interview scenarios.";
    if (percentage >= 70) return "Good foundation! Review the missed concepts before your interview.";
    if (percentage >= 60) return "Decent start! Focus on the fundamentals and practice more problems.";
    return "Keep studying! Practice these core concepts before your interview.";
  };

  if (quizComplete) {
    return (
      <div className="max-w-3xl mx-auto p-6 bg-white rounded-lg shadow-lg">
        <div className="text-center">
          <Trophy className="mx-auto h-16 w-16 text-yellow-500 mb-4" />
          <h2 className="text-3xl font-bold text-gray-800 mb-4">Interview Quiz Complete!</h2>
          <div className={`text-4xl font-bold mb-2 ${getScoreColor()}`}>
            {score} / {questions.length}
          </div>
          <div className="text-lg text-gray-600 mb-4">
            {Math.round((score / questions.length) * 100)}% Correct
          </div>
          <p className="text-gray-700 mb-6 max-w-md mx-auto">
            {getPerformanceMessage()}
          </p>
          
          <div className="bg-gray-50 rounded-lg p-4 mb-6 max-w-md mx-auto">
            <h3 className="font-semibold text-gray-800 mb-2">Topics Covered:</h3>
            <div className="text-sm text-gray-600 space-y-1">
              <div>• Algorithms & Time Complexity</div>
              <div>• Data Structures & Collections</div>
              <div>• Object-Oriented Programming</div>
              <div>• Error Handling & Best Practices</div>
              <div>• Advanced Python Features</div>
            </div>
          </div>
          
          <button
            onClick={resetQuiz}
            className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-colors flex items-center mx-auto"
          >
            <RotateCcw className="mr-2 h-4 w-4" />
            Practice Again
          </button>
        </div>
      </div>
    );
  }

  const currentQ = questions[currentQuestion];

  return (
    <div className="max-w-3xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <div className="mb-6">
        <div className="flex justify-between items-center mb-2">
          <div className="flex items-center space-x-4">
            <span className="text-sm font-medium text-gray-500">
              Question {currentQuestion + 1} of {questions.length}
            </span>
            <span className="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded-full">
              {currentQ.category}
            </span>
          </div>
          <span className="text-sm font-medium text-gray-500">
            Score: {score}/{questions.length}
          </span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-2">
          <div 
            className="bg-blue-600 h-2 rounded-full transition-all duration-300"
            style={{ width: `${((currentQuestion + 1) / questions.length) * 100}%` }}
          ></div>
        </div>
      </div>

      <div className="mb-6">
        <div className="flex items-center mb-3">
          <Code className="h-5 w-5 text-blue-600 mr-2" />
          <h2 className="text-lg font-bold text-gray-800">
            Python Interview Question
          </h2>
        </div>
        
        <div className="bg-gray-50 border rounded-lg p-4 mb-4">
          <pre className="text-sm text-gray-800 whitespace-pre-wrap font-mono leading-relaxed">
            {currentQ.question}
          </pre>
        </div>
        
        <div className="space-y-3">
          {currentQ.options.map((option, index) => (
            <button
              key={index}
              onClick={() => handleAnswerSelect(index)}
              disabled={showResult}
              className={`w-full p-4 text-left border-2 rounded-lg transition-all duration-200 ${
                showResult
                  ? index === currentQ.correct
                    ? 'border-green-500 bg-green-50 text-green-800'
                    : index === selectedAnswer && index !== currentQ.correct
                    ? 'border-red-500 bg-red-50 text-red-800'
                    : 'border-gray-200 bg-gray-50 text-gray-600'
                  : selectedAnswer === index
                  ? 'border-blue-500 bg-blue-50 text-blue-800'
                  : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'
              }`}
            >
              <div className="flex items-center">
                <span className="flex-1 font-mono text-sm whitespace-pre-line">
                  {option}
                </span>
                {showResult && index === currentQ.correct && (
                  <CheckCircle className="h-5 w-5 text-green-500 ml-2" />
                )}
                {showResult && index === selectedAnswer && index !== currentQ.correct && (
                  <XCircle className="h-5 w-5 text-red-500 ml-2" />
                )}
              </div>
            </button>
          ))}
        </div>
      </div>

      {showResult && (
        <div className="mb-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
          <h3 className="font-semibold text-blue-800 mb-2 flex items-center">
            <Clock className="h-4 w-4 mr-2" />
            Explanation:
          </h3>
          <p className="text-blue-700 text-sm leading-relaxed">{currentQ.explanation}</p>
        </div>
      )}

      <div className="flex justify-end">
        {!showResult ? (
          <button
            onClick={handleSubmit}
            disabled={selectedAnswer === ''}
            className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed text-white font-bold py-2 px-6 rounded-lg transition-colors flex items-center"
          >
            Submit Answer
            <ChevronRight className="ml-2 h-4 w-4" />
          </button>
        ) : (
          <button
            onClick={handleNext}
            className="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-6 rounded-lg transition-colors flex items-center"
          >
            {currentQuestion < questions.length - 1 ? 'Next Question' : 'View Results'}
            <ChevronRight className="ml-2 h-4 w-4" />
          </button>
        )}
      </div>
    </div>
  );
};

export default PythonInterviewQuiz;