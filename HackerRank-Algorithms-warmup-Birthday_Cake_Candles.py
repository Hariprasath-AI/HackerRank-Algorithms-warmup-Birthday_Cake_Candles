def birthdayCakeCandles(candles, n):
    # Initialize large and count value as 0
    large = 0
    count = 0
    # It compares the large value and i'th value in the 'candles' and returns count of maximum value
    for i in range(0, n):
        if candles[i] > large:
            large = candles[i]
            count = 1
        elif candles[i] == large:
            count += 1
        elif candles[i] < large:
            continue
    print(count)

if __name__ == '__main__':
    # This n will be passed as a argument in for loop.. make sure the number of values in the input will perfectly match with 'n'. 
    n = int(input())

    # Get input from user and converted into a list
    candles = list(map(int, input().split()))

    birthdayCakeCandles(candles, n)
