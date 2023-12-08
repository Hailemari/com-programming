class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]
            files = parts[1:]

            for file in files:
                file_parts = file.split('(')
                file_name = file_parts[0]
                file_content = file_parts[1][:-1]

                content_map[file_content].append(directory + '/' + file_name)

        result = [group for group in content_map.values() if len(group) > 1]
        return result


            


                

        