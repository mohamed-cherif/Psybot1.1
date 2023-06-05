import schedule
import time


def graph(person):
    person.graph_home = person.graph_home.append((((person.depressive + person.suicide + person.cyberbullying) / 3
                                                   ) * 100) / person.total)
    person.graph_dep = person.graph_dep.append((person.depressive * 100) / person.total)
    person.graph_sui = person.graph_sui.append((person.suicide * 100) / person.total)
    person.graph_cyb = person.graph_cyb.append((person.cyberbullying * 100) / person.total)
    person.save()
    print("done")


def start_scheduler(person):
    # Schedule the task to run every minute
    schedule.every(1).minutes.do(graph(person))

    # Run the scheduled tasks continuously
    while True:
        schedule.run_pending()

