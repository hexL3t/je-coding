#include <iostream>
#include <ctime>    // For random seed
#include <cstdlib>  // For rand()
using namespace std;

const int SIZE = 5;         // Board is 5x5
const int MINES = 3;        // Number of hidden mines

// Boards
char visibleBoard[SIZE][SIZE];   // What the player sees
char hiddenBoard[SIZE][SIZE];    // Contains the mines

// Function to initialize both boards
void initializeBoards() {
    // Set all cells in both boards to default values
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            visibleBoard[i][j] = '*'; // Hide everything from player
            hiddenBoard[i][j] = '0';  // Set all to empty for now
        }
    }
}

// Function to randomly place mines
void placeMines() {
    int count = 0;
    while (count < MINES) {
        int x = rand() % SIZE;
        int y = rand() % SIZE;
        if (hiddenBoard[x][y] != 'M') {
            hiddenBoard[x][y] = 'M'; // Place a mine
            count++;
        }
    }
}

// Count surrounding mines for a cell
int countMines(int x, int y) {
    int count = 0;

    // Loop over all adjacent cells
    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            int nx = x + dx;
            int ny = y + dy;

            // Check if neighbor is within bounds
            if (nx >= 0 && nx < SIZE && ny >= 0 && ny < SIZE) {
                if (hiddenBoard[nx][ny] == 'M') {
                    count++;
                }
            }
        }
    }

    return count;
}

// Reveal a cell and show nearby mine count
bool revealCell(int x, int y) {
    // Check for out-of-bounds
    if (x < 0 || x >= SIZE || y < 0 || y >= SIZE) {
        cout << "Invalid coordinates!" << endl;
        return true;  // Continue game
    }

    if (hiddenBoard[x][y] == 'M') {
        visibleBoard[x][y] = 'M';
        return false; // Hit a mine - game over
    }

    int mines = countMines(x, y);
    visibleBoard[x][y] = '0' + mines; // Convert int to char
    return true; // Safe move
}

// Display the board that the player sees
void displayBoard() {
    cout << "\n  ";
    for (int i = 0; i < SIZE; i++)
        cout << i << " ";
    cout << endl;

    for (int i = 0; i < SIZE; i++) {
        cout << i << " ";
        for (int j = 0; j < SIZE; j++) {
            cout << visibleBoard[i][j] << " ";
        }
        cout << endl;
    }
}

// Main game loop
void playGame() {
    int x, y;
    bool gameRunning = true;
    int safeMoves = SIZE * SIZE - MINES; // Total number of non-mine cells
    int revealed = 0;

    while (gameRunning && revealed < safeMoves) {
        displayBoard();
        cout << "\nEnter cell to reveal (row and column): ";
        cin >> x >> y;

        if (visibleBoard[x][y] != '*') {
            cout << "Cell already revealed. Try another.\n";
            continue;
        }

        gameRunning = revealCell(x, y);
        if (gameRunning) revealed++;
    }

    if (!gameRunning) {
        cout << "\n💥 BOOM! You hit a mine. Game Over.\n";
    } else {
        cout << "\n🎉 Congratulations! You cleared the board safely!\n";
    }

    // Reveal full board for review
    cout << "\nFinal Board (Hidden Mines):\n";
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            cout << hiddenBoard[i][j] << " ";
        }
        cout << endl;
    }
}

// Main entry point
int main() {
    srand(time(0)); // Seed random number generator

    initializeBoards(); // Start with clean boards
    placeMines();       // Add mines randomly
    playGame();         // Start game loop

    return 0;
}
