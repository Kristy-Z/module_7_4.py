team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

print("В команде Мастера кода участников: %d !" % team1_num)
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {:.1f} с !".format(team2_time))

print(f"Команды решили {score_1} и {score_2} задач.")

challenge_result = 'Победа команды Волшебники данных!'
print(f'Результат битвы: {challenge_result}')

time_for_task = sum([team1_time, team2_time]) / tasks_total
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_for_task:.1f} секунды на задачу!")
