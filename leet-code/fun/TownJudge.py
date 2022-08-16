class Solution:
    def findJudge(self, n, trust):
        if n == 1:
            return 1

        members = set()
        trusts = {}
        trusted_by = {}

        for fro, to in trust:
            if fro not in trusts:
                trusts[fro] = {to}
            else:
                trusts[fro].add(to)

            if to not in trusted_by:
                trusted_by[to] = {fro}
            else:
                trusted_by[to].add(fro)
            
            members.add(fro)
            members.add(to)

        # Get the elements that do not trust anyone
        untrusting = []
        for member in members:
            if member not in trusts:
                untrusting.append(member)

        judge = []
        for member in untrusting:
            if member in trusted_by:
                if len(trusted_by[member]) == n - 1 and member not in trusted_by[member]:
                    judge.append(member)

        return judge[0] if len(judge) == 1 else -1;

print(Solution().findJudge(3, [[1,3],[2,3]]))