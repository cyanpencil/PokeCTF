#include <stdio.h>
#include <string.h>

char * flag = "onjdzF/nc^xnt^b`m^fds^rs`qsdc^mnv|";

int main() {
    printf("Please input the correct password:\n");
    char correct_passwd [200];
    fgets(correct_passwd, 199, stdin);
    if (!strcmp(correct_passwd, "the correct password:\n")) {
        puts("Thanks! Here you go:");
        for (int i = 0; i < strlen(flag); i++) printf("%c", flag[i] + 1);
    } else {
        printf("Look, I don't think I asked anything too hard... \nCan't you follow simple instructions??\n");
    }
}
