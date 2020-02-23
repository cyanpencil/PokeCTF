#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int secret = 0;
    char name[100] = {0};
    read(0, name, 0x100);
    if (secret == 0xcafebabe) {
        puts("Wow! How did you do that???");
        puts("Here, have a shell ;)");
        system("/bin/sh");
    } else {
        puts("I guess you're not cool enough....");
    }
}
