def solution(k, dungeons):
  answer = 0
  # 더 이상 돌 수 있는 던전이 없으면
  if len(dungeons) == 0:
    return answer

  for i in range(len(dungeons)):
    if dungeons[i][0] <= k:
      min_piro, use_piro = dungeons.pop(i)
      answer = max(answer, 1 + solution(k - use_piro, dungeons))
      dungeons.insert(i, [min_piro, use_piro])

  return answer