class Merge:
    def Sort(self, array):
        """
        Sorts array.

        :param array: Array to merge
        :return: Void
        """
        auxiliaryArray = array.copy()  # Auxiliary array

        def MergePartitions(s1, e1, s2, e2, current):
            """
            Merge partitions: start1 → end1 & start2 → end2

            :param s1: start index of part 1
            :param e1: end index of part 1
            :param s2: start index of part 2
            :param e2: end index of part 2
            :param current: Current index of auxiliary array
            :return: Void
            """
            # If array finish
            if s1 > e1 and s2 > e2: return  # If both starts cross end, nothing to merge; so return

            if s1 > e1:  # If part 1 finishes, copy remaining part 2 items to auxiliary array
                for i in range(s2, e2 + 1):
                    auxiliaryArray[current] = array[i]
                    current += 1

                return

            if s2 > e2:  # If part 2 finishes, copy remaining part 1 items to auxiliary array
                for i in range(s1, e1 + 1):
                    auxiliaryArray[current] = array[i]
                    current += 1

                return

            # Pick the minimum of the 2 partitions
            # & add it to auxiliary array
            if array[s1] < array[s2]:  # If partition1 < partition2
                auxiliaryArray[current] = array[s1]
                current += 1
                s1 += 1
            elif array[s2] < array[s1]:  # If partition2 < partition1
                auxiliaryArray[current] = array[s2]
                current += 1
                s2 += 1
            else:  # array[s1] == array[s2]:
                # Add both items to auxiliary array
                auxiliaryArray[current] = array[s1]
                auxiliaryArray[current + 1] = array[s2]
                current += 2
                s1 += 1
                s2 += 1

            MergePartitions(s1, e1, s2, e2, current)  # Pick next merged item

        def Sort(start, end):
            """
            Sort index start → end

            :param start: start index
            :param end: end index
            :return: Void
            """
            # Solve small sub-problems
            if start == end: return

            # Divide
            mid = (start + end) // 2

            Sort(start, mid)  # Left part
            Sort(mid + 1, end)  # Right part

            # Combine
            # Array partitions in order
            if array[mid + 1] >= array[mid]:  # Right part >= left part
                return
            elif array[start] >= array[end]:  # Left part >= right part, move right to left part
                current = start
                for i in range(mid + 1, end + 1):  # 1st copy right part to auxiliary array
                    auxiliaryArray[current] = array[i]
                    current += 1

                for i in range(start, mid + 1):  # Then copy left part to auxiliary array
                    auxiliaryArray[current] = array[i]
                    current += 1
            else:
                MergePartitions(start, mid, mid + 1, end, start)  # Merge 2 sorted partitions

            # Copy array ← auxiliary
            for i in range(start, end + 1): array[i] = auxiliaryArray[i]

        Sort(0, len(array) - 1)  # Sort index 0 → end

    @staticmethod
    def Work():
        array = [2, 7, 4, 9, 7]

        Merge().Sort(array)
        print(array)
