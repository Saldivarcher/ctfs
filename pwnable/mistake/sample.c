#include <stdio.h>
#include <string.h>

void xor(char *s, int len) {
    for (int i = 0; i < len; i++) {
        s[i] ^= 1;
    }
}

int main() {
    char pw_buf[11];
    char pw_buf2[11] = {[0 ... 10] = 'A'};

    scanf("%10s", pw_buf);
    xor(pw_buf, 10);

    if (!strncmp(pw_buf, pw_buf2, 10)) {
        printf("HERE!\n");
    }
}
