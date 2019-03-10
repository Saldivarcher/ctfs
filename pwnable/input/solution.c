#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>

char *PATH = "/home/vagrant/pwnable/input/input";

int main(void) {
    // Set all the whole array to contain "A"
    char *argv[101] = {[0 ... 100] = "A"};
    extern char **environ;

    // Stage 1 - argv
    argv[100] = NULL;
    argv['A'] = "\x00";
    argv['B'] = "\x20\x0a\x0d";
    
    // Part of Stage 5
    argv['C'] = "5001";


    // Stage 3 - env
    setenv("\xde\xad\xbe\xef", "\xca\xfe\xba\xbe", 1);

    // Stage 4 - file
    FILE *file = fopen("\x0a", "w");
    fwrite("\x00\x00\x00\x00", 4, 1, file);
    fclose(file);


    // Stage 2 - stdio
    pid_t childpid;
    int pipe_stdin[2], pipe_stderr[2];

    if (pipe(pipe_stdin) < 0 || pipe(pipe_stderr) < 0) {
        perror("Broken pipe\n");
        exit(1);
    }

    if ((childpid = fork()) < 0) {
        perror("Broken fork\n");
        exit(1);
    }

    if (childpid == 0) {
        close(pipe_stdin[0]);
        close(pipe_stderr[0]);

        write(pipe_stdin[1], "\x00\x0a\x00\xff", 4);
        write(pipe_stdin[1], "\x00\x0a\x02\xff", 4);

        // Stage 5 - networking
        int sd, cd;
        struct sockaddr_in saddr;
        sd = socket(AF_INET, SOCK_STREAM, 0);

        saddr.sin_family = AF_INET;
        saddr.sin_addr.s_addr = inet_addr("127.0.0.1");
        saddr.sin_port = htons(atoi(argv['C']));

        if (connect(sd, (struct soaddr *)&saddr, sizeof(saddr)) < 0) {
            perror("Broken network!");
            return -1;
        }

        write(sd, "\xde\xad\xbe\xef", 4);
        close(sd);

        return 0;
    } else {
        close(pipe_stdin[1]);
        close(pipe_stderr[1]);

        dup2(pipe_stdin[0], 0);
        dup2(pipe_stdin[0], 2);

        close(pipe_stdin[0]);
        close(pipe_stderr[0]);

        execve(PATH, argv, environ);
    }
}
