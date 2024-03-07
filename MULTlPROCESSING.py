import multiprocessing
import time
from datetime import datetime

def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
        print(f"Data written to {file_path}")

def main():
    file_path3 = 'file3.txt'
    file_path4 = 'file4.txt'
    file_path5 = 'file5.txt'
    file_path6 = 'file6.txt'
    file_path7 = 'file7.txt'
    file_path8 = 'file8.txt'

    data3 = 'Hello from Process 1!'
    data4 = 'Greetings from Process 2!'
    data5 = 'Assalamu alekum process3!'
    data6 = 'PYTHONBACKEND!'
    data7 = 'JAVAC#C++!'
    data8 = 'DATA SCIENCE!'

    # Create processes
    process1 = multiprocessing.Process(target=write_to_file, args=(file_path3, data3))
    process2 = multiprocessing.Process(target=write_to_file, args=(file_path4, data4))
    process3 = multiprocessing.Process(target=write_to_file, args=(file_path5, data5))
    process4 = multiprocessing.Process(target=write_to_file, args=(file_path6, data6))
    process5 = multiprocessing.Process(target=write_to_file, args=(file_path7, data7))
    process6 = multiprocessing.Process(target=write_to_file, args=(file_path8, data8))

    # Start processes
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()

    print("Main process continues execution.")

if __name__ == "__main__":
    print(datetime.now().time())
    main()
    print(datetime.now().time())