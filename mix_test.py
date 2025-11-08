import mixbox

# 두 색상 (파랑, 노랑)
rgb1 = (0, 33, 133)
rgb2 = (252, 211, 0)
t = 0.5  # 혼합 비율

rgb_mix = mixbox.lerp(rgb1, rgb2, t)
print("혼합 결과 RGB:", rgb_mix)
