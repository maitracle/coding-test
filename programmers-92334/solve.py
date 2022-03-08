def solution(id_list, report, k):
    reported = {}
    mail_counts = {}

    for id in id_list:
        reported[id] = set([])
        mail_counts[id] = 0

    for report_item in report:
        reporter, abuser = report_item.split()
        reported[abuser].add(reporter)

    for abuser in reported:
        if len(reported[abuser]) >= k:
            for reporter in reported[abuser]:
                mail_counts[reporter] += 1

    return list(map(lambda id: mail_counts[id], id_list))
