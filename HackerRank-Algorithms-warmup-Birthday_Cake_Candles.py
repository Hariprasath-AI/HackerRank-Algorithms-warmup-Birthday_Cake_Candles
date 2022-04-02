def birthdayCakeCandles(candles):
    n = len(candles)
    for i in range(0, n - 1):
        if i == 0:
            if candles[i] > candles[i+1]:
                large = candles[i]
                count = 1
            elif candles[i] < candles[i + 1]:
                large = candles[i + 1]
                count = 1
            elif candles[i] == candles[i + 1]:
                large = candles[i + 1]
                count = 2
        else:
            if candles[i] > candles[i+1]:
                if candles[i] > large:
                    large = candles[i]
                    count = 1
                elif candles[i] < large:
                    continue
                elif candles[i] == large:
                    count += 0

            elif candles[i] < candles[i + 1]:
                if candles[i + 1] > large:
                    large = candles[i + 1]
                    count = 1
                elif candles[i + 1] < large:
                    continue
                elif candles[i + 1] == large:
                    count += 1

            elif candles[i] == candles[i + 1]:
                if candles[i] == large:
                    count += 1
                elif candles[i] < large:
                    continue
                elif candles[i] > large:
                    large = candles[i]
                    count = 1

    print(count)
if __name__ == '__main__':
    n = int(input())

    candles = list(map(int, input().split()))

    birthdayCakeCandles(candles)
