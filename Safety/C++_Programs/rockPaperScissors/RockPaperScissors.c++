#include<iostream>
#include<stdlib.h>
#include<time.h>

using namespace std;

int main(){
    string options[3] = {"Rock", "Paper", "Scissors"};
    int choice = 0;
    bool run = true;
    srand (time(NULL));
    int bot = rand() % 3;

    while (choice != -1) {
        cout << "Enter your choice: ";
        int bot = rand() % 3;
        cin >> choice;
        if (2 < choice){
            cout << "Invalid Selection" << endl;
            cin >> choice;
        }
        
        cout << "You: " << options[choice] << endl;
        cout << "Bot: "<<options[bot] << endl;
        if (choice == bot){
            cout << "Its a draw" << endl;
        }

        // Rock and Scissor
        if (choice == 0 && bot == 1){
            cout << "You lose" << endl;
        }

        // Rock and Paper
        if (choice == 0 && bot == 2){
            cout << "You win" << endl;
        }

        // Scissor and Rock
        if (choice == 1 && bot == 0){
            cout << "You lose" << endl;
        }

        // Scissor and Paper
        if (choice == 1 && bot == 2){
            cout << "You win" << endl;
        }

        // Paper and Scissor
        if (choice == 2 && bot == 1){
            cout << "You lose" << endl;
        }

        // Paper and Rock
        if (choice == 2 && bot == 0){
            cout << "You lose" << endl;
        }
        
        
    }

    

}