#include <unistd.h>

int main() {
    char *argv[] = {"flag"};
    execve("/bin/cat", argv, NULL);
    return 0;
}
