# import __main__ as main
# from Helper.TimerLogger import CodeTimeLogging
# fileName = main.__file__
# fileName = fileName.split('\\')[-1]

# CodeTimeLogging(Flag='F', filename=fileName, Tag='Array', Difficult='Easy')


def uniqueMail(emails):
    seen = set()
    for idx in emails:
        name, domain = idx.split('@')
        if '+' in name:
            name = name.split('+')[0]
        seen.add(name.replace('.', '') + '@' + domain)
    return len(seen)


emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(uniqueMail(emails))
