# CSE304-2026-1-Algorithms
# Week08-4.5.huffman_problem.py

from heapq import heappush, heappop

class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol  # 문자 또는 '*' (내부 노드)
        self.freq = freq      # 빈도 또는 병합된 빈도의 합
        self.left = None
        self.right = None
        
    def preorder(self, path):
        # 전위 순회: 루트 → 왼쪽 → 오른쪽
        path.append((self.symbol, self.freq))
        if self.left != None:
            self.left.preorder(path)
        if self.right != None:
            self.right.preorder(path)

    def inorder(self, path):
        # 중위 순회: 왼쪽 → 루트 → 오른쪽
        if self.left != None:
            self.left.inorder(path)
        path.append((self.symbol, self.freq))
        if self.right != None:
            self.right.inorder(path)

def huffman(n, s, f):
    # n: 문자의 개수
    # s: 문자 리스트 (예: ['b', 'e', 'c', 'a', 'd', 'f'])
    # f: 각 문자의 빈도 리스트 (예: [5, 10, 12, 16, 17, 25])
    
    heap = []
    # 힙에 (빈도, Node) 튜플을 저장
    # heappush로 삽입할 때마다 새 노드를 트리 우하단에 붙인 후
    # 부모와 비교하며 올라가는 percolate up 과정으로 정렬됨
    for i in range(n):
        heappush(heap, (f[i], Node(s[i], f[i])))

    # 허프만 트리 구성: 한 개의 루트 노드가 남을 때까지 반복
    while len(heap) > 1:
        freq1, node1 = heappop(heap)  # 빈도가 가장 낮은 노드
        freq2, node2 = heappop(heap)  # 빈도가 두 번째로 낮은 노드
        
        # 두 노드를 병합: 빈도는 합산
        merged_freq = freq1 + freq2
        # '*'는 내부 노드(internal node)를 표시하는 마커 기호
        # pop/merge 로직에는 영향 없고, 트리 순회 출력 시에만 사용됨
        merged_node = Node('*', merged_freq)    
        merged_node.left = node1
        merged_node.right = node2
        heappush(heap, (merged_freq, merged_node))

    # 마지막 남은 루트 노드 반환
    # heappop()은 (빈도, Node) 튜플을 반환하므로
    # [1] 인덱스로 Node 객체만 추출
    return heappop(heap)[1]

########################################################################################
# DO NOT MODIFY THIS AREA!!
########################################################################################

def print_huffman_tree(root):
    path = []
    root.preorder(path)
    print("preorder =", path)
    path = []
    root.inorder(path)
    print("inorder =", path)


def test_huffman(n, s, f, expected_preorder=None, expected_inorder=None):
    print(f"문자 개수: {n}")
    print(f"문자: {s}")
    print(f"빈도: {f}")
    root = huffman(n, s, f)

    # Preorder(루트 → 왼쪽 → 오른쪽)와 Inorder(왼쪽 → 루트 → 오른쪽) 순회로
    # 허프만 트리가 올바르게 구성되었는지 검증
    path_pre = []
    root.preorder(path_pre)
    print(f"preorder: {path_pre}")
    path_in = []
    root.inorder(path_in)
    print(f"inorder: {path_in}")

    if expected_preorder is not None:
        if path_pre == expected_preorder:
            print("✅ preorder 일치")
        else:
            print("❌ preorder 불일치")

    if expected_inorder is not None:
        if path_in == expected_inorder:
            print("✅ inorder 일치")
        else:
            print("❌ inorder 불일치")

    print("-" * 40)


if __name__ == "__main__":
    print("**************Testing huffman()**************")

    print("######Example 1######")
    n1 = 6
    s1 = ['b', 'e', 'c', 'a', 'd', 'f']
    f1 = [5, 10, 12, 16, 17, 25]
    expected_pre1 = [('*', 85), ('*', 33), ('a', 16), ('d', 17), ('*', 52), ('f', 25), ('*', 27), ('c', 12), ('*', 15), ('b', 5), ('e', 10)]
    expected_in1 = [('a', 16), ('*', 33), ('d', 17), ('*', 85), ('f', 25), ('*', 52), ('c', 12), ('*', 27), ('b', 5), ('*', 15), ('e', 10)]
    test_huffman(n1, s1, f1, expected_pre1, expected_in1)

    print("######Example 2######")
    n2 = 4
    s2 = ['x', 'y', 'z', 'w']
    f2 = [3, 7, 8, 12]
    expected_pre2 = [('*', 30), ('w', 12), ('*', 18), ('z', 8), ('*', 10), ('x', 3), ('y', 7)]
    expected_in2 = [('w', 12), ('*', 30), ('z', 8), ('*', 18), ('x', 3), ('*', 10), ('y', 7)]
    test_huffman(n2, s2, f2, expected_pre2, expected_in2)

    print("######Example 3######")
    n3 = 5
    s3 = ['m', 'n', 'o', 'p', 'q']
    f3 = [2, 3, 7, 9, 13]
    expected_pre3 = [('*', 34), ('q', 13), ('*', 21), ('p', 9), ('*', 12), ('*', 5), ('m', 2), ('n', 3), ('o', 7)]
    expected_in3 = [('q', 13), ('*', 34), ('p', 9), ('*', 21), ('m', 2), ('*', 5), ('n', 3), ('*', 12), ('o', 7)]
    test_huffman(n3, s3, f3, expected_pre3, expected_in3)

########################################################################################
# END OF TEST CODE
########################################################################################

# You can add more cases
# Example 4 (Custom)
# test_huffman(n, s, f, expected_preorder, expected_inorder)
