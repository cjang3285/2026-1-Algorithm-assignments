# CSE304-2026-1-Algorithms
# Week11-leetcode_64_problem.py
# https://leetcode.com/problems/minimum-path-sum/description/

from collections import deque
from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    # 빈 격자 예외 처리: 이동 경로가 없으므로 0 반환
    if not grid or not grid[0]:
        return 0
    
    # 행(m), 열(n) 크기 계산
    m, n = len(grid), len(grid[0])
    # BFS 큐: (행, 열, 시작점부터 현재 칸까지의 누적 합)
    queue = deque([(0, 0, grid[0][0])])
    # 각 칸에 도달한 "현재까지 최소 누적 합"을 기록(더 나쁜 경로 재방문 방지)
    visited = {(0, 0): grid[0][0]}
    # 도착점까지의 최소 경로 합(처음에는 무한대로 시작)
    min_path_sum = float('inf')
        
    # 큐가 빌 때까지 너비 우선으로 상태 탐색
    while queue:
        # 가장 먼저 들어온 상태를 꺼냄
        i, j, current_sum = queue.popleft()

        # 도착점에 도달했다면 최소값 갱신 후보로 사용
        if (i, j) == (m - 1, n - 1):
            # 더 작은 누적 합이면 정답 후보를 갱신
            if current_sum < min_path_sum:
                min_path_sum = current_sum
            # 도착점 상태는 더 확장할 필요가 없음
            continue

        # 오른쪽 칸이 격자 내부라면 이동 시도
        if j + 1 < n:
            # 오른쪽으로 이동했을 때의 새 누적 합
            next_sum = current_sum + grid[i][j + 1]
            # 기존 기록보다 좋고, 이미 찾은 최적 도착합보다도 작은 경우만 큐에 추가
            if next_sum < visited.get((i, j + 1), float('inf')) and next_sum < min_path_sum:
                # 해당 칸까지의 최소 누적 합 기록 갱신
                visited[(i, j + 1)] = next_sum
                # 다음 탐색 대상으로 큐에 삽입
                queue.append((i, j + 1, next_sum))

        # 아래쪽 칸이 격자 내부라면 이동 시도
        if i + 1 < m:
            # 아래로 이동했을 때의 새 누적 합
            next_sum = current_sum + grid[i + 1][j]
            # 기존 기록보다 좋고, 현재 최적 도착합보다 작은 경우만 큐에 추가
            if next_sum < visited.get((i + 1, j), float('inf')) and next_sum < min_path_sum:
                # 해당 칸의 최소 누적 합 기록 갱신
                visited[(i + 1, j)] = next_sum
                # 다음 탐색 대상으로 큐에 삽입
                queue.append((i + 1, j, next_sum))
    
    # 최종 최소 경로 합 반환
    return min_path_sum


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################

def test_min_path_sum(grid, expected_sum):
    print(f"\n--- 테스트 케이스 {grid} ---")
    print("Grid:")
    for row in grid:
        print(row)
    
    min_sum = minPathSum(grid)
    
    print(f"최소 경로 합: {min_sum}")
    
    if min_sum == expected_sum:
        print("✅ 테스트 통과: 정답입니다!")
    else:
        print(f"❌ 테스트 실패: 예상 합은 {expected_sum}이지만, {min_sum}을 찾았습니다.")
    
    print("-" * 40)
    return min_sum


def main():
    grid1 = [[1,3,1],[1,5,1],[4,2,1]]
    test_min_path_sum(grid1, 7)
    
    grid2 = [[1,2,3],[4,5,6]]
    test_min_path_sum(grid2, 12)
    
    grid3 = [[1,2],[5,6],[1,1]]
    test_min_path_sum(grid3, 8)


if __name__ == "__main__":
    main()

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example (Custom)
# test_min_path_sum([[...]], expected_sum)
