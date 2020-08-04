#include <stdio.h>


int isWonRow(char player, char game[3][3], int rowNum)
{
    int flag = 1;
    for (int row = 0; row < 3; row++) {
        for (int col = 0; col < 3; col++) {
            if (player != game[col]) {
                flag = 0;
            } 
        } return flag;
    }
}

int main(void)
{
    char game[3][3] = {{'X', '.', '.'},
                      {'X', 'X', 'X'},
                      {'O', 'O', 'X'}};

    for (int row = 0; row < 3; row++) {
        for (int col = 0; col < 3; col++) {
            printf("%3c", game[row][col]);
        }
        printf("\n");

        printf("%d\n", isWonRow('X', game, 1));
    }

}
