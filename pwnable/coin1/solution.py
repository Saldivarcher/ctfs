import pwn

UTF = 'UTF-8'

def connect():
    conn = pwn.remote('pwnable.kr', 9007)
    conn.recv(10024)
    return conn

def main():
    conn = connect()
    for _ in range(100):
        line = conn.recv(1024).decode(UTF).strip().split(' ')
        print(line)

        n = int(line[0].split('=')[1])
        c = int(line[1].split('=')[1])

        left = 0
        right = n

        for _ in range(c):
            guess = ' '.join(str(left) for left in range(left,
                int((left+right)/2)))

            conn.sendline(guess)

            output = int(conn.recv(1024).decode(UTF).strip())

            if (output % 10 == 0):
                left = int((left + right) / 2)
            else:
                right = int((left + right) / 2)

        conn.sendline(str(left))
        print(conn.recv(1024).decode(UTF))
    print(conn.recv(1024).decode(UTF))
    conn.close()
    
if __name__ == "__main__":
    main()
