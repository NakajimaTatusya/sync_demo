import socket
import time

# 順次処理


def blocking_way():
    sck = socket.socket()
    sck.connect(('www.ricoh.co.jp', 80))
    request = 'GET / HTTP/1.0\r\nHost: https://www.ricoh.co.jp/\r\n\r\n'
    sck.send(request.encode('ascii'))
    response = b''

    chunk = sck.recv(4096)
    while chunk:
        response += chunk
        chunk = sck.recv(4096)

    return response


def sync_way():
    res = []
    total_recieve_size = 0

    for i in range(10):
        response_data = blocking_way()
        total_recieve_size += response_data.__sizeof__()
        res.append(response_data)

    return total_recieve_size


if __name__ == "__main__":
    elapsed_times = 0
    rec_len = 0

    for _ in range(10):
        start = time.time()
        rec_len = sync_way()
        elapsed_time = time.time() - start
        elapsed_times += elapsed_time
        print(
            f"elapsed_time: {(elapsed_time):.2f}[sec] recieve size: {(rec_len):d}[byte]")

    print(f"mean_elapsed_time: {(elapsed_times/10):.2f}[sec]")
