#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm> // For transform() and remove_if()
using namespace std;

// Helper function to trim leading and trailing spaces from a string
string trim(const string& str) {
    size_t first = str.find_first_not_of(" \t\r\n");
    size_t last = str.find_last_not_of(" \t\r\n");
    return (first == string::npos || last == string::npos) ? "" : str.substr(first, last - first + 1);
}

// Helper function to convert a string to lowercase for case-insensitive comparison
string toLower(const string& str) {
    string result = str;
    transform(result.begin(), result.end(), result.begin(), ::tolower);
    return result;
}

int main() {
    vector<string> questions;
    vector<string> answers;
    string line;

    // Open quiz file
    ifstream file("quiz.txt");
    if (!file) {
        cerr << "❌ Error: Could not open 'quiz.txt'. Make sure the file exists." << endl;
        return 1;
    }

    // Load questions and answers from the file
    while (getline(file, line)) {
        stringstream ss(line);
        string q, a;
        if (getline(ss, q, '|') && getline(ss, a)) {
            questions.push_back(trim(q));
            answers.push_back(trim(a));
        }
    }

    file.close();

    if (questions.empty()) {
        cout << "⚠️ No questions found in the file." << endl;
        return 0;
    }

    cout << "🧠 Welcome to the Enhanced Quiz Challenge!\n";
    cout << "You will be asked " << questions.size() << " question(s). Type your answers below.\n" << endl;

    int score = 0;
    string userAnswer;

    for (size_t i = 0; i < questions.size(); i++) {
        cout << "Q" << (i + 1) << ": " << questions[i] << endl;
        cout << "Your answer: ";
        getline(cin, userAnswer);

        // Trim and compare answers in lowercase
        if (toLower(trim(userAnswer)) == toLower(answers[i])) {
            cout << "✅ Correct!\n" << endl;
            score++;
        } else {
            cout << "❌ Incorrect. The correct answer was: " << answers[i] << "\n" << endl;
        }
    }

    // Show final score
    cout << "🎉 Quiz Complete! Your final score: " << score << " out of " << questions.size() << endl;

    // Provide feedback based on performance
    double percentage = (double)score / questions.size() * 100;

    if (percentage == 100)
        cout << "🏆 Incredible! You got a perfect score!" << endl;
    else if (percentage >= 70)
        cout << "👏 Well done! You're pretty sharp." << endl;
    else if (percentage >= 40)
        cout << "👍 Not bad! Keep learning." << endl;
    else
        cout << "📘 Time to hit the books!" << endl;

    // Save result to a file
    ofstream resultFile("quiz_results.txt", ios::app);
    if (resultFile) {
        resultFile << "Quiz result: " << score << "/" << questions.size() << " (" << percentage << "%)" << endl;
        resultFile << "-----------------------------" << endl;
        resultFile.close();
        cout << "\n📁 Your result has been saved to 'quiz_results.txt'" << endl;
    } else {
        cerr << "⚠️ Failed to write results to file." << endl;
    }

    return 0;
}
