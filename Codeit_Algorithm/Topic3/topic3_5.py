# 제목: 강남역 폭우
def trapping_rain(buildings):
    rain_vol = 0

    for walk in range(1, len(buildings)-1):
        tallest_left = max(buildings[:walk])
        tallest_right = max(buildings[walk+1:])

        upper_bound = min(tallest_left, tallest_right)

        rain_vol += max(0, upper_bound - buildings[walk])

    return rain_vol


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))