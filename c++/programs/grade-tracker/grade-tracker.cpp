#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <iomanip>

using namespace std;

// This program allows users to register, login, store grades per subject,
// and calculates an estimated ATAR based on their average grades.

// === Constants ===
// File where user login credentials are stored.
// It holds lines in the format: username,password
const string USERS_FILE = "users.txt";

/*
 * Function: userExists
 * --------------------
 * Purpose:
 *   Checks if a username already exists in the USERS_FILE.
 * How it works:
 *   - Opens the USERS_FILE for reading.
 *   - Reads line by line, splitting at comma to get usernames.
 *   - Returns true if username found, else false.
 * Why important:
 *   - Prevents duplicate usernames during registration.
 */
bool userExists(const string& username) {
    ifstream file(USERS_FILE);
    if (!file.is_open()) return false;  // File might not exist if no users yet

    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string fileUser;
        if (getline(ss, fileUser, ',')) {
            if (fileUser == username) return true;
        }
    }
    return false;
}

/*
 * Function: registerUser
 * ----------------------
 * Purpose:
 *   Registers a new user by adding username and password to USERS_FILE.
 * How it works:
 *   - Calls userExists to check for duplicates.
 *   - If no duplicate, appends username,password to USERS_FILE.
 * Returns:
 *   - true if registration succeeded, false if failed or username taken.
 * Teaching notes:
 *   - Uses file append mode (ios::app) to add new users.
 */
bool registerUser(const string& username, const string& password) {
    if (userExists(username)) {
        cout << "Username already exists.\n";
        return false;
    }

    ofstream file(USERS_FILE, ios::app);
    if (!file.is_open()) {
        cout << "Error opening users file for saving.\n";
        return false;
    }

    file << username << "," << password << "\n";
    cout << "User registered successfully!\n";
    return true;
}

/*
 * Function: authenticateUser
 * --------------------------
 * Purpose:
 *   Checks if given username and password match a record in USERS_FILE.
 * How it works:
 *   - Opens USERS_FILE.
 *   - Reads line by line, splits each into username and password.
 *   - Returns true if a matching pair is found.
 * Teaching notes:
 *   - Demonstrates simple authentication using plain text files.
 *   - Not secure for real applications, but fine for learning.
 */
bool authenticateUser(const string& username, const string& password) {
    ifstream file(USERS_FILE);
    if (!file.is_open()) {
        cout << "Error opening users file.\n";
        return false;
    }

    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string fileUser, filePass;
        if (getline(ss, fileUser, ',') && getline(ss, filePass)) {
            if (fileUser == username && filePass == password) {
                return true;
            }
        }
    }
    return false;
}

/*
 * Function: getGradesFilename
 * ---------------------------
 * Purpose:
 *   Generates a unique filename for storing a user's grades.
 * Explanation:
 *   - Each user has their own grades file: "<username>_grades.txt"
 * Teaching notes:
 *   - This separates data per user to avoid mixing grades.
 */
string getGradesFilename(const string& username) {
    return username + "_grades.txt";
}

/*
 * Function: loadGradesForUser
 * ---------------------------
 * Purpose:
 *   Loads a user's saved grades from their grades file into a map.
 * How it works:
 *   - Opens grades file for the user.
 *   - Reads each line formatted as "subject,grade".
 *   - Adds them to the map with subject as key and grade as value.
 * Teaching notes:
 *   - Shows how to persist and retrieve complex data (key-value pairs).
 */
void loadGradesForUser(const string& username, map<string, double>& grades) {
    ifstream file(getGradesFilename(username));
    if (!file.is_open()) return;  // No grades saved yet for this user

    string line;
    while (getline(file, line)) {
        stringstream ss(line);
        string subject;
        double grade;
        if (getline(ss, subject, ',') && ss >> grade) {
            grades[subject] = grade;
        }
    }
}

/*
 * Function: saveGradesForUser
 * ---------------------------
 * Purpose:
 *   Saves the user's current grades from the map to their grades file.
 * How it works:
 *   - Opens the file (overwrites).
 *   - Writes each subject and grade in "subject,grade" format on a line.
 * Teaching notes:
 *   - Demonstrates writing structured data for persistence.
 */
void saveGradesForUser(const string& username, const map<string, double>& grades) {
    ofstream file(getGradesFilename(username));
    if (!file.is_open()) {
        cout << "Error saving grades.\n";
        return;
    }

    for (const auto& pair : grades) {
        file << pair.first << "," << pair.second << "\n";
    }
}

/*
 * Function: calculateAverage
 * --------------------------
 * Purpose:
 *   Calculates the average grade from all subjects.
 * Returns:
 *   - 0 if no grades exist.
 * Teaching notes:
 *   - Simple aggregation example with a map.
 */
double calculateAverage(const map<string, double>& grades) {
    if (grades.empty()) return 0.0;

    double sum = 0;
    for (const auto& pair : grades) {
        sum += pair.second;
    }
    return sum / grades.size();
}

/*
 * Function: estimateATAR
 * ----------------------
 * Purpose:
 *   Estimates an ATAR score based on average grade.
 * Explanation:
 *   - Uses a simplified formula: (average / 100) * 99.95
 *   - Real ATAR calculations are more complex.
 * Teaching notes:
 *   - Shows basic formula implementation for educational purposes.
 */
double estimateATAR(double average) {
    return (average / 100.0) * 99.95;
}

/*
 * Main function
 * -------------
 * Controls the program flow:
 * 1. Ask user to Login or Register
 * 2. Perform registration or login with 3 attempts max
 * 3. Load user's existing grades (if any)
 * 4. Allow input/updating of grades interactively
 * 5. Save updated grades
 * 6. Calculate and display average and estimated ATAR
 */
int main() {
    cout << "=== Grade Tracker ===\n";
    cout << "1. Login\n2. Register\nChoose an option: ";
    string option;
    getline(cin, option);

    string username, password;

    // Registration flow
    if (option == "2") {
        cout << "=== User Registration ===\n";

        // Loop until user provides unique username
        while (true) {
            cout << "Choose a username: ";
            getline(cin, username);
            if (userExists(username)) {
                cout << "Username already taken. Try again.\n";
                continue;
            }
            break;
        }

        cout << "Choose a password: ";
        getline(cin, password);

        if (!registerUser(username, password)) {
            cout << "Registration failed. Exiting.\n";
            return 1;
        }
    }

    // Login flow (for both new and existing users)
    cout << "\n=== User Login ===\n";

    // Allow up to 3 login attempts
    for (int attempts = 0; attempts < 3; ++attempts) {
        // If user just registered, username/password already set.
        // Otherwise, prompt for login credentials.
        if (option != "2") {
            cout << "Username: ";
            getline(cin, username);
            cout << "Password: ";
            getline(cin, password);
        }

        if (authenticateUser(username, password)) {
            cout << "Login successful! Welcome, " << username << ".\n";
            break;
        } else {
            cout << "Invalid username or password. Try again.\n";
            if (attempts == 2) {
                cout << "Too many failed attempts. Exiting.\n";
                return 1;
            }
            option = ""; // force prompt next time
        }
    }

    // Load user's grades into a map
    map<string, double> grades;
    loadGradesForUser(username, grades);

    cout << "\nCurrent grades:\n";
    if (grades.empty()) {
        cout << "No grades recorded yet.\n";
    } else {
        for (const auto& pair : grades) {
            cout << " - " << pair.first << ": " << pair.second << "\n";
        }
    }

    cout << "\nEnter new grades or update existing ones.\nType 'done' when finished.\n";

    // Input loop: add or update grades until user types 'done'
    while (true) {
        string subject;
        cout << "\nSubject (or 'done'): ";
        getline(cin, subject);
        if (subject == "done") break;

        cout << "Grade for " << subject << " (0-100): ";
        string gradeStr;
        getline(cin, gradeStr);

        double grade;
        try {
            grade = stod(gradeStr);
        } catch (...) {
            cout << "Invalid input. Please enter a number.\n";
            continue;
        }

        if (grade < 0 || grade > 100) {
            cout << "Grade must be between 0 and 100.\n";
            continue;
        }

        grades[subject] = grade;
        cout << "Recorded: " << subject << " = " << grade << "\n";
    }

    // Save updated grades back to file
    saveGradesForUser(username, grades);

    // Calculate average and estimate ATAR
    double average = calculateAverage(grades);
    double atar = estimateATAR(average);

    cout << fixed << setprecision(2);
    cout << "\nYour average grade is: " << average << "\n";
    cout << "Estimated ATAR: " << atar << "\n";

    cout << "\nThank you for using the Grade Tracker!\n";

    return 0;
}
