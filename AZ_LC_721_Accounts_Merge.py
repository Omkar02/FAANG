# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Disjoint-Set', Difficult='Medium')


class UF:
    def __init__(self):
        self.ids = {}

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        self.ids[i] = j

    def find(self, p):
        if p not in self.ids:
            self.ids[p] = p

        while p != self.ids[p]:
            self.ids[p] = self.ids[self.ids[p]]
            p = self.ids[p]

        return p

    def accountsMerge(self, accounts):
        email_to_person = {}
        for acc in accounts:
            person = acc[0]
            for email in acc[1:]:
                email_to_person[email] = person
                self.union(acc[1], email)

        clusters = {}
        for email in email_to_person.keys():
            fVal = self.find(email)
            if fVal not in clusters:
                clusters[fVal] = []
            clusters[fVal].append(email)

        result = []
        for cluster in clusters.values():
            if cluster[0] in email_to_person:
                group = [email_to_person[cluster[0]]] + sorted(cluster)
                result.append(group)
        return result


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]

b = UF()
print(b.accountsMerge(accounts))
