#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

const int SIZE = 5;        // Board Size is 5 x 5
const int MINES = 3;       // Number of hidden mines

// Boards
char visableBoard[SIZE][SIZE];  // What the player sees
char hiddenBoard[SIZE][SIZE];   // Contains the mines
bool revealed[SIZE][SIZE];      // Track revealed cells
int cellsToReveal = SIZE * SIZE - MINES;

// Function to initialise both boards
void initaliseBoards(){
    // set all cells in both boards to default values
    for(int i = 0; i < SIZE; i++){
        for(int j = 0; j < SIZE; j++){
            visableBoard[i][j] = '*';   // Hide everything from player
            hiddenBoard[i][j] = '0';    // set all to empty for now
            revealed[i][j] = false;
        }
    }
}

// Function to place random mines on the hidden board
void placeMines(){
    int placed = 0;

    // Keep placing mines until we reach the required number
    while (placed < MINES ) {
        int row = rand() % SIZE; // Random row index (0 to SIZE - 1)
        int col = rand() % SIZE; // Random column index (0 to SIZE - 1)

        // Only place a mine if there isnt one already
        if (hiddenBoard[row][col] != 'M') {
            hiddenBoard[row][col] = 'M';    // Place Mine
            placed++;                       // Increment placed count.
        }
    }

     // After placing mines, calculate adjacent mine counts
     for (int i =  0; i < SIZE; i++){
        for (int j = 0; j < SIZE; j++){
            if (hiddenBoard[i][j] == 'M') continue;
            int mineCount = 0;

            for (int r = i - 1; r <= i + 1; r++ ){
                for (int c = j - 1; c <= j + 1; r++ ){
                    if (r >= 0 && r < SIZE && c >= 0 && c < SIZE && hiddenBoard[r][c] == 'M'){
                        mineCount++;
                    }
                }
            }

            hiddenBoard[i][j] = mineCount + '0';
        }
     }
}

// Function to print the visible board with grid formatting
void printVisibleBoard() {
    // Print column headers
    cout << "\n    ";
    for (int i = 0; i < SIZE; i++)
        cout << " " << i << "  ";
    cout << "\n   +" << string(SIZE * 4 - 1, '-') << "+\n";

    // Print each row with borders
    for (int i = 0; i < SIZE; i++) {
        cout << " " << i << " |";  // Row number and left border
        for (int j = 0; j < SIZE; j++) {
            cout << " " << visableBoard[i][j] << " |";  // Cell value and vertical border
        }
        cout << "\n   +" << string(SIZE * 4 - 1, '-') << "+\n";  // Bottom border of row
    }
}

// Function to show the hidden board (for learning/debugging purposes)
void printHiddenBoard(){
    cout << "\n >>> Hidden Board <<<\n" << endl;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            cout << " " << hiddenBoard[i][j] << " ";  // Cell value and vertical border
        }
        cout << endl;
    }
}

// Recursive function to reveal a cell adjacent ones if its zero.
void revealCell(int row, int col){

}

// Main Game Loop
void minesweeper(){
    int row, col;
    bool gameOver = false;

    // Continue asking for player moves until game ends
    while (!gameOver){
        printVisibleBoard(); // Show the current visible board

        // Ask the player for input
        cout << "\nChoose a coordinate to uncover (row column): > ";
        cin >> row >> col;

        // Validate input range
        if(row < 0 || row >= SIZE || col < 0 || col >= SIZE){
            cout << "❗ Invalid coordinates. Try again." << endl;
            continue;  // Skip the rest and go back to input
        }

        if(revealed[row][col]){
            cout << "⚠️ Already Revealed. Pick Another." << endl;
            continue;
        }

        // Check if the player hit a mine
        if (hiddenBoard[row][col] == 'M') {
            visableBoard[row][col] = 'M';   // Show the mines on the visable board
            cout << "\n💥 BOOM! You hit a mine! 💥" << endl;
            gameOver = true;                // End the game
        } else {
            revealCell[row][col];  // Safe cell is revealed (could be replaced with a mine count)
            cout << "✅ Safe! Keep Going..." << endl;
        }
    }

    // After the game ends, show final board and actual mine locations
    printVisibleBoard();
    printHiddenBoard();

}

int main() {
    srand(time(0)); // Seed random number generator

    cout << "\n===[ M I N E S W E E P E R ]===" << endl;
    cout << "Uncover cells... carefully!" << endl;

    initaliseBoards(); // Start with clean boards
    placeMines();
    minesweeper();

    // Final Message
    cout << "\n🎮 Game Over. Thanks for Playing." << endl;

    return 0;
}