# CSE304-2026-1-Algorithms
# Week10-leetcode_131_problem.py
# https://leetcode.com/problems/palindrome-partitioning/description/

from typing import List

def partition(s: str) -> List[List[str]]:
    # 결과를 담을 리스트
    res = []
    # 디버그: 실행 다이어그램을 보고 싶을 때 True로 설정하세요.
    DEBUG = False

    # Helper: 회문 여부 검사
    def is_palindrome(sub: str) -> bool:
        # 여기가 회문인가? 회문이면 True 반환
        return sub == sub[::-1]
    # 실행 로그(디버그)와 동작 다이어그램(주석):
    # 아래는 실제 `DEBUG=True`로 실행했을 때 출력된 예시 로그(일부 발췌).
    # - 로그는 각 분기 진입(ENTER), 후보 시도(TRY), 재귀 호출(RECURSE),
    #   결과 저장(APPENDED), 복귀 전/후(RETURN/AFTER pop), 분기 종료(EXIT)을 보여줍니다.
    # 예시: input = "aab"
    # ENTER start=0 path=[]
    #   TRY sub='a' (start=0, end=1) -> path+['a'] = ['a']
    #     RECURSE to start=1 path=['a']
    # ENTER start=1 path=['a']
    #   TRY sub='a' (start=1, end=2) -> path+['a'] = ['a','a']
    #     RECURSE to start=2 path=['a','a']
    # ENTER start=2 path=['a','a']
    #   TRY sub='b' (start=2, end=3) -> path+['b'] = ['a','a','b']
    #     RECURSE to start=3 path=['a','a','b']
    #   APPENDED res <- ['a','a','b']
    #     RETURN from start=3 before pop path=['a','a','b']
    #     AFTER pop path=['a','a']
    # EXIT start=0 path=[]
    # ✔ 위 로그를 통해 관찰할 수 있는 동작 원리:
    # - `res.append(list(path))`는 `path`의 '현재 상태'를 복사해서 저장하므로,
    #   이후 `path.pop()`으로 `path`를 변경해도 저장된 결과는 안전합니다.
    # - 백트랙은 "형제 분기"를 시도하기 위해 부모 상태로 정확히 복원(pop)합니다.
    # - 동일한 '값'(예: 'a')이 여러 분기에서 반복 등장할 수 있지만, 인덱스 조합(start,end)이
    #   다르므로 서로 다른 분할로 `res`에 각각 기록됩니다.
    # Mermaid 다이어그램(요약: input = "aabaa"):
    # ```mermaid
    # graph TD
    #   Root["start=0\npath=[]"]
    #   A1["TRY 'a'\n(0,1) -> path=['a']"]
    #   Root --> A1
    #   A1A["TRY 'a'\n(1,2) -> path=['a','a']"]
    #   A1 --> A1A
    #   A1A1["TRY 'b'\n(2,3) -> path=['a','a','b']"]
    #   A1A --> A1A1
    #   A1A1A["TRY 'a'\n(3,4) -> path=['a','a','b','a']"]
    #   A1A1 --> A1A1A
    #   A1A1A1["TRY 'a'\n(4,5)\nAPPEND ['a','a','b','a','a']"]
    #   A1A1A --> A1A1A1
    #   A1A1A2["TRY 'aa'\n(3,5)\nAPPEND ['a','a','b','aa']"]
    #   A1A1 --> A1A1A2
    #   A1B["TRY 'aba'\n(1,4) -> path=['a','aba']"]
    #   A1 --> A1B
    #   A1B1["TRY 'a'\n(4,5)\nAPPEND ['a','aba','a']"]
    #   A1B --> A1B1
    #   A2["TRY 'aa'\n(0,2) -> path=['aa']"]
    #   Root --> A2
    #   A2A["TRY 'b'\n(2,3) -> path=['aa','b']"]
    #   A2 --> A2A
    #   A2A1["TRY 'a'\n(3,4) -> path=['aa','b','a']"]
    #   A2A --> A2A1
    #   A2A1A["TRY 'a'\n(4,5)\nAPPEND ['aa','b','a','a']"]
    #   A2A1 --> A2A1A
    #   A2A1B["TRY 'aa'\n(3,5)\nAPPEND ['aa','b','aa']"]
    #   A2A --> A2A1B
    #   A3["TRY 'aabaa'\n(0,5)\nAPPEND ['aabaa']"]
    #   Root --> A3
    # ```
    # 위 다이어그램과 로그로부터 파악한 추가 설명(주석으로 포함):
    # 1) "긴 길이 문자열이 회문으로 append 됐어도 다음에 한 글자가 회문으로 append 될 수 있다" 이유:
    #    - 백트랙은 트리 구조로 동작한다. 어떤 노드에서 긴 조각을 선택해 리프(또는 중간 노드)를
    #      만든 뒤 리턴하면, 부모 노드는 동일한 start에서 다음 end 후보(더 짧거나 더 긴)를 계속 시도한다.
    #    - 즉, "긴 조각을 선택한 분기"는 하나의 서브트리이고, 그 서브트리가 끝나고 돌아오면
    #      부모가 다른 자식(예: 한 글자짜리)을 시도할 수 있으므로 결과적으로 한 글자짜리 조각이
    #      나중에 append 될 수 있다(다른 분기에서).
    # 2) `backtrack(end, path)`에서 `end`를 다음 `start`로 넘기는 이유:
    #    - 파티셔닝은 연속 구간들의 나열이다. 선택한 조각 s[start:end]의 바로 다음 문자인
    #      인덱스 `end`부터 다음 조각을 시작해야 문자열 전체를 겹치지 않고 빠짐없이 덮을 수 있다.
    #    - `end`를 넘기지 않으면 분할이 겹치거나 건너뛰는 잘못된 분할을 생성할 수 있다.
    #    - 그러므로 `end`를 다음 `start`로 사용하는 것은 "조각들이 정확히 이어지도록" 보장하는 핵심 규칙입니다.
    # backtrack 파라미터 의미(문제 맥락):
    # 가능한 모든 부분문자열을 검사해 유망한(회문인) 분기만 재귀로 확장한다.
    
    # 한줄 요약(사고방식): 여기가 정답인가? 정답이면 저장하자. 유망하면 분기하고 아니면 포기.
    # 전체 아이디어(단계별):
    # 1) 'start'부터 가능한 모든 'end'를 이동시키며 s[start:end]을 만든다.
    # 2) 그 조각이 회문이면 '유망'하므로 path에 추가하고 다음 탐색은 그 조각 바로 다음 인덱스(end)부터 시작한다.
    # 3) 비회문이면 그 분기는 포기한다(path에 append하지 않음).
    # 4) 이렇게 모든 start,end 조합을 시도하면 가능한 모든 회문인 조각들을 path에 얻을 수 있다.
    def backtrack(start: int, path: List[str]):
        if DEBUG:
            print(f"ENTER start={start} path={path}")
        if start == len(s): # 모든 문자를 처리했다(start == len(s))면 현재 path는 완전한 회문 조각(정답)
            # 정답이면 res 저장
            # 중요: 여기서는 `path`의 '현재 상태'를 복사해서 저장한다.
            # - `list(path)`는 `path`의 얕은 복사본을 만들어 `res`에 넣는다.
            # - 그 이후에 부모/다른 분기에서 `path.pop()`으로 `path`를 변경해도
            #   이미 저장된 복사본은 영향을 받지 않는다.
            # 따라서 동일한 부분문자열 값이 여러 분기에서 반복 등장하더라도
            # 각 분기는 서로 다른 인덱스 조합(start,end)을 기반으로 하므로
            # "값이 같은 조각"이 여러 번 `res`에 반영될 수 있다(중복된 '값'은 허용됨).
            res.append(list(path))
            if DEBUG:
                print(f"  RESULT res = {res}")
            return
        
        # 다음 분할 위치(end)를 start+1 .. len(s)까지 이동시키며
        # s[start:end]가 palindrome인지 확인하고, 맞으면 재귀로 진행
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]           # 현재 고려하는 조각(현재)
            # 이 조각은 회문인가?
            if is_palindrome(sub):
                if DEBUG:
                    print(f"  TRY sub={sub!r} (start={start}, end={end}) -> path+[{sub!r}] = {path + [sub]}")
                # 현재 호출(이 레벨)이 책임지고 추가한 조각을 path에 추가
                path.append(sub)        # 회문이면 조각을 회문 조각 리스트에 추가
                if DEBUG:
                    print(f"    RECURSE to start={end} path={path}")
                backtrack(end, path)    # 다음 분할로 분기 (end를 다음 start로 입력)
                if DEBUG:
                    print(f"    RETURN from start={end} before pop path={path}")
                # 재귀가 끝나고 돌아오면, 이 레벨이 추가한 '한 조각'만 pop()한다.
                path.pop()              # 재귀 종료 후
                if DEBUG:
                    print(f"    AFTER pop path={path}")
        if DEBUG:
            print(f"EXIT start={start} path={path}")
    # 초기 호출: 시작 인덱스 0, 빈 경로
    backtrack(0, [])
    return res


def partition_solver(s: str) -> List[List[str]]:
    return partition(s)


########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################

def test_partition(s: str, expected: List[List[str]]):
    actual = partition_solver(s)
    actual_sorted = sorted(actual, key=lambda x: str(x))
    expected_sorted = sorted(expected, key=lambda x: str(x))

    if actual_sorted == expected_sorted:
        print("✅ 테스트 통과")
    else:
        print("❌ 테스트 실패")


def main():
    test_partition("aab", [["a","a","b"],["aa","b"]])
    test_partition("a", [["a"]])
    test_partition("aba", [["a","b","a"],["aba"]])
    test_partition(
        "aabaa",
        [
            ["a", "a", "b", "a", "a"],
            ["a", "a", "b", "aa"],
            ["a", "aba", "a"],
            ["aa", "b", "a", "a"],
            ["aa", "b", "aa"],
            ["aabaa"]
        ]
    )


if __name__ == "__main__":
    main()

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 5 (Custom)
# test_partition("abc", [...])
