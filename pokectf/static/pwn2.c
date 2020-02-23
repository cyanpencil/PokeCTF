/* compile: gcc -Wno-format-security ex1.c -o ex1 */ 
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void papa_please_let_me_win() {
    system("/bin/sh");
}

void main(int argc, char *argv[]) {
    setbuf(stdout, NULL);
    printf("What do you want me to print?\n");
    char buf[103]; 
    fgets(buf, 103, stdin); 
    buf[strlen(buf)-1] = 0x0; 
    printf("Ok, here you go:\n");
    printf(buf); 
    exit(0);
}
