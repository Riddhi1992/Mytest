# Find the prime numbers between 0 to 500

# Enter the Starting and Ending number between which you want to see all prime numbers
#start_num = input("Enter starting number: ")
#end_num = input("Enter Ending number: ")

start_num = 0
end_num = 500

for current_num in range(start_num, end_num + 1):
    if current_num>1:
        for z in range(2, current_num):
            if current_num % z ==0:
                break
        else:
            print(current_num)


def test_current_num():
    response = current_num(start_num, end_num)
    assert response == 0



def test_prime(start_num, end_num):
    response = prime(start_num, end_num)
    response[0] == [4]

