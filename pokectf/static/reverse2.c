

#include <stdio.h>
#include <unistd.h>


long long time_sleep = 2000000;

int array[] = { 80, 79, 75, 69, 91, 52, 72, 20, 84, 63, 87, 20, 83, 63, 78, 16, 84, 14, 72, 65, 82, 68, 63, 41, 13, 72, 16, 80, 69, 93};

int steps[] = {2, 5, 10, -1, -3, -5, 1, 0, 3, 3, 7, -1, 8, -5, 10, -2};


int main() {
    for (int j = 0; j < 16; j++) {
        for (int i = 0; i < 30; i++) {
            array[i] += steps[j];
            printf("%c", array[i]);
            fflush(stdout);
            usleep(time_sleep);
        }
        puts("\n");
    }
}
