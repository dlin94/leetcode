class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]

        for i in range(0, max(len(v1), len(v2))):
            # Check up to the min length, returning the appropriate int if one
            # version is higher than the other
            if i < len(v1) and i < len(v2):
                if v1[i] > v2[i]:
                    return 1
                elif v2[i] > v1[i]:
                    return -1
            # Past the min length, so check for non-zero revision numbers
            elif i >= len(v1):
                if v2[i] != 0:
                    return -1
            elif i >= len(v2):
                if v1[i] != 0:
                    return 1

        # If we get here, then the versions are equal
        return 0
